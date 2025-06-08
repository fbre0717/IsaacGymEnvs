import torch
import math
from poselib.core.rotation3d import quat_mul_norm
from poselib.skeleton.skeleton3d import SkeletonState, SkeletonMotion
from poselib.visualization.common import plot_skeleton_state, plot_skeleton_motion_interactive
from scipy.interpolate import CubicSpline
import numpy as np

def adjust_jump_height(
    motion: SkeletonMotion, 
    key_frames=None, 
    target_max_height=None,
    height_scale=1.0,
    auto_detect_threshold=0.1
) -> SkeletonMotion:
    """
    키프레임들 사이에만 스플라인 보간을 적용하여 점프 높이를 조절합니다.
    키프레임 바깥의 프레임들은 가장 가까운 경계 키프레임의 값으로 설정됩니다.
    """
    adjusted_translation = motion.root_translation.clone()
    num_frames = len(adjusted_translation)
    all_frames = np.arange(num_frames)
    
    # 키프레임 자동 감지
    if key_frames is None:
        z_values = adjusted_translation[:, 2].numpy()
        z_velocity = np.gradient(z_values)
        start_candidates = np.where(np.abs(z_velocity) > auto_detect_threshold)[0]
        start_frame = start_candidates[0] if len(start_candidates) > 0 else 0
        end_frame = start_candidates[-1] if len(start_candidates) > 0 else num_frames - 1
        peak_frame = np.argmax(z_values)
        key_frames = [start_frame, peak_frame, end_frame]
    
    key_z_values = adjusted_translation[key_frames, 2].numpy()
    target_ground_height = min(key_z_values[0], key_z_values[-1])
    
    # 최대 높이 설정
    if target_max_height is not None:
        peak_height = target_max_height
    else:
        original_peak_height = key_z_values[1]
        peak_height = target_ground_height + (original_peak_height - target_ground_height) * height_scale
    
    new_key_z_values = np.array([
        target_ground_height,
        peak_height,
        target_ground_height
    ])
    
    # 새로운 Z값 배열 초기화
    new_z_values = np.zeros(num_frames)
    
    # 첫 키프레임 이전: 첫 키프레임 값으로 설정
    new_z_values[:key_frames[0]] = target_ground_height
    
    # 키프레임들 사이: 스플라인 보간 적용
    cs = CubicSpline(key_frames, new_key_z_values)
    new_z_values[key_frames[0]:key_frames[-1]+1] = cs(all_frames[key_frames[0]:key_frames[-1]+1])
    
    # 마지막 키프레임 이후: 마지막 키프레임 값으로 설정
    new_z_values[key_frames[-1]:] = target_ground_height
    
    # 보정된 Z값 적용
    adjusted_translation[:, 2] = torch.tensor(new_z_values, dtype=adjusted_translation.dtype)
    
    # 새로운 모션 생성
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
    fbx_path = "data/tricking/fullfull.fbx"

    adjust = True

    motion = SkeletonMotion.from_fbx(
        fbx_file_path=fbx_path,
        root_joint="Hips",
        fps=30
    )

    transformed_motion = transform_motion(
        motion,
        frame_beg=36,
        frame_end=60,
        rot_x=90, 
        rot_z=0, 
        trans_x=0,
        trans_y=0.6, 
        trans_z=4.4
    )
    npy_path = fbx_path.replace(".fbx", ".npy")

    if adjust:
        # 점프 높이 보정 적용
        final_motion = adjust_jump_height(
            transformed_motion, 
            key_frames=[2, 12, 22], 
            target_max_height=1.4
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
# btwist 174~218 h=1.4
# corks 261~288 h=1.4
# dcorks 349~378 h=1.4

### loopkicks
# raiz 0,53/20,29,38
# fulltwist 0,69/27,39,50
# cheat720 0,78/35,45,55 h=1.4

# raiz4 
# 22,29,35
# 16,40/6,13,19 h=1.4

# aerial_raizx4 => amp_fs_raizx4
# 28, 34, 42
# 22, 45/6,12,20 h=1.2 => 1.4

# shurikencutter 
# 8, 19, 30

# fullfull
# 38, 48, 58
# 36,61/2,12,22