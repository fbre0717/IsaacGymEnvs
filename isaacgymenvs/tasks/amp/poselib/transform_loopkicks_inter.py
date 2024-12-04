import torch
import math
from poselib.core.rotation3d import quat_mul_norm
from poselib.skeleton.skeleton3d import SkeletonState, SkeletonMotion
from poselib.visualization.common import plot_skeleton_state, plot_skeleton_motion_interactive
from scipy.interpolate import CubicSpline
import numpy as np

def adjust_jump_height(motion: SkeletonMotion, key_frames=None) -> SkeletonMotion:
    """
    스플라인 보간법을 사용하여 점프 동작의 Z축 높이를 보정합니다.
    
    동작 원리:
    1. 주요 키프레임들(시작, 최고점, 착지)의 Z축 값을 기준으로 새로운 높이 곡선을 생성합니다.
    2. 시작과 착지 지점의 높이를 동일하게 맞추고, 그 사이의 값들을 부드럽게 보간합니다.
    
    매개변수:
        motion: 보정할 모션 데이터
        key_frames: [시작 프레임, 최고점 프레임, 착지 프레임] 리스트. 
                   None이면 자동으로 검출합니다.
    
    반환:
        높이가 보정된 새로운 모션 데이터
    """
    # 모션 데이터 복사
    adjusted_translation = motion.root_translation.clone()
    num_frames = len(adjusted_translation)
    
    # 키프레임이 지정되지 않은 경우 자동 검출
    if key_frames is None:
        z_values = adjusted_translation[:, 2].numpy()
        start_frame = 0
        peak_frame = np.argmax(z_values)  # 최고점 프레임
        end_frame = num_frames - 1
        key_frames = [start_frame, peak_frame, end_frame]
    
    # 키프레임에서의 Z축 값
    key_z_values = adjusted_translation[key_frames, 2].numpy()
    
    # 시작과 끝 높이를 같게 설정 (더 낮은 값으로)
    target_ground_height = min(key_z_values[0], key_z_values[-1])
    
    # 새로운 Z값 설정
    new_key_z_values = np.array([
        target_ground_height,  # 시작 높이
        key_z_values[1],      # 최고점 높이는 유지
        target_ground_height   # 착지 높이
    ])
    
    # 스플라인 보간 생성
    cs = CubicSpline(key_frames, new_key_z_values)
    
    # 모든 프레임에 대해 새로운 Z값 계산
    all_frames = np.arange(num_frames)
    new_z_values = cs(all_frames)
    
    # 보정된 Z값 적용
    adjusted_translation[:, 2] = torch.tensor(new_z_values, dtype=adjusted_translation.dtype)
    
    # 새로운 모션 데이터 생성
    adjusted_motion = SkeletonMotion.from_skeleton_state(
        SkeletonState.from_rotation_and_root_translation(
            skeleton_tree=motion.skeleton_tree,
            r=motion.local_rotation,
            t=adjusted_translation,
            is_local=True
        ),
        fps=motion.fps
    )
    
    return adjusted_motion


def create_rotation_quat(angle_degrees, axis='x'):
    angle_rad = math.radians(angle_degrees)
    c = math.cos(angle_rad / 2)
    s = math.sin(angle_rad / 2)
    
    quat = torch.zeros(4)
    if axis.lower() == 'x':
        quat[0], quat[3] = s, c
    elif axis.lower() == 'y':
        quat[1], quat[3] = s, c
    elif axis.lower() == 'z':
        quat[2], quat[3] = s, c
    return quat

def transform_motion(motion: SkeletonMotion, frame_beg=-1, frame_end=-1, rot_x=90, rot_z=0, trans_x=0, trans_y=0, trans_z=0) -> SkeletonMotion:
    # 시작 프레임 설정: -1이면 처음부터 시작
    if frame_beg == -1:
        frame_beg = 0
        
    # 끝 프레임 설정: -1이면 마지막 프레임까지 사용
    if frame_end == -1:
        frame_end = motion.local_rotation.shape[0]
    
    # 프레임 범위 선택
    local_rotation = motion.local_rotation[frame_beg:frame_end, ...]
    root_translation = motion.root_translation[frame_beg:frame_end, ...]
    
    quat_x = create_rotation_quat(rot_x, 'x')
    quat_z = create_rotation_quat(rot_z, 'z')
    
    motion_rotation = local_rotation.clone()
    motion_translation = root_translation.clone()
    
    for frame in range(len(motion_rotation)):
        motion_rotation[frame, 0] = quat_mul_norm(quat_z, quat_mul_norm(quat_x, motion_rotation[frame, 0]))
    
    motion_translation[:, 0] += trans_x
    motion_translation[:, 1] += trans_y
    motion_translation[:, 2] += trans_z
    
    return SkeletonMotion.from_skeleton_state(
        SkeletonState.from_rotation_and_root_translation(
            skeleton_tree=motion.skeleton_tree,
            r=motion_rotation,
            t=motion_translation,
            is_local=True
        ),
        fps=motion.fps
    )

if __name__ == "__main__":
    fbx_path = "data/loopkicks/raiz0.fbx"
    adjust = False

    motion = SkeletonMotion.from_fbx(
        fbx_file_path=fbx_path,
        root_joint="Hips",
        fps=30
    )

    transformed_motion = transform_motion(
        motion,
        frame_beg=391,
        frame_end=427,
        rot_x=90, 
        rot_z=0, 
        trans_x=-1,
        trans_y=1.5, 
        trans_z=8.7
    )
    npy_path = fbx_path.replace(".fbx", ".npy")

    if adjust:
        # 점프 높이 보정 적용
        final_motion = adjust_jump_height(
            transformed_motion
            # key_frames=[0, 20, 32]  # 예시 키프레임
        )
        final_motion.to_file(npy_path)
        plot_skeleton_motion_interactive(final_motion)
    else:
        transformed_motion.to_file(npy_path)
        plot_skeleton_motion_interactive(transformed_motion)
    
    print(f"Saved to: {npy_path}")


# cheat360 0~60
# fulltwist0 0~60
# backflip 0~72
# raiz0 0~50

###shosei
# btwist 174~218
# corks 261~288
# dcorks 349~378