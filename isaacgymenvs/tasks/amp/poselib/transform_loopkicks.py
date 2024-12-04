import torch
import math
from poselib.core.rotation3d import quat_mul_norm
from poselib.skeleton.skeleton3d import SkeletonState, SkeletonMotion
from poselib.visualization.common import plot_skeleton_state, plot_skeleton_motion_interactive

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
    fbx_path = "data/shosei/shosei_corks.fbx"

    motion = SkeletonMotion.from_fbx(
        fbx_file_path=fbx_path,
        root_joint="Hips",
        fps=30
    )

    transformed_motion = transform_motion(
        motion,
        frame_beg=261,
        frame_end=288,
        rot_x=90, 
        rot_z=0, 
        trans_x=0.5,
        trans_y=0.5, 
        trans_z=9.4
    )

    npy_path = fbx_path.replace(".fbx", ".npy")
    transformed_motion.to_file(npy_path)
    print(f"Saved to: {npy_path}")
    plot_skeleton_motion_interactive(transformed_motion)


# cheat360 0~60
# fulltwist0 0~60
# backflip 0~72
# raiz0 0~50

###shosei
# btwist 174~218
# corks 261~288