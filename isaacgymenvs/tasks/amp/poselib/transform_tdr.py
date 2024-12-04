import os
import json
import torch
import math
from poselib.core.rotation3d import quat_mul_norm
from poselib.skeleton.skeleton3d import SkeletonTree, SkeletonState, SkeletonMotion
from poselib.visualization.common import plot_skeleton_state, plot_skeleton_motion_interactive

# 회전을 위한 쿼터니언 생성 함수
def create_rotation_quat(angle_degrees, axis='x'):
    angle_rad = math.radians(angle_degrees)
    c = math.cos(angle_rad / 2)
    s = math.sin(angle_rad / 2)
    
    if axis.lower() == 'x':
        return torch.tensor([s, 0, 0, c])  # [x, y, z, w] 형식
    elif axis.lower() == 'z':
        return torch.tensor([0, 0, s, c])  # [x, y, z, w] 형식
    
    return torch.tensor([0, 0, 0, 1])  # 기본값: 회전 없음

# FBX에서 모션 데이터 로드
fbx_file = "data/tdr_corks_wonder.fbx"
motion = SkeletonMotion.from_fbx(
    fbx_file_path=fbx_file,
    root_joint="Hips",
    fps=30
)

# X축 90도, Z축 90도 회전을 위한 쿼터니언
rotation_quat_x = create_rotation_quat(90, 'x')
rotation_quat_z = create_rotation_quat(0, 'z')

# 모든 프레임의 로컬 회전값에 X축과 Z축 회전 순차적으로 적용
motion_rotation = motion.local_rotation.clone()
for frame in range(len(motion_rotation)):
    motion_rotation[frame, 0] = quat_mul_norm(rotation_quat_z,
                               quat_mul_norm(rotation_quat_x, motion_rotation[frame, 0]))

# Translation 수정 (Y축 -0.95, Z축 +0.97)
motion_translation = motion.root_translation.clone()
motion_translation[:, 1] = motion_translation[:, 1] + 0.5  # Y값에 -0.95 적용
motion_translation[:, 2] = motion_translation[:, 2] + 6.4  # Z값에 +0.97 적용

# 전체 모션 저장
transformed_motion = SkeletonMotion.from_skeleton_state(
    SkeletonState.from_rotation_and_root_translation(
        skeleton_tree=motion.skeleton_tree,
        r=motion_rotation,
        t=motion_translation,
        is_local=True
    ),
    fps=motion.fps
)

plot_skeleton_motion_interactive(transformed_motion)
transformed_motion.to_file("data/tdr_corks_wonder.npy")

# tdr 0~35 frame
# corcks 31~56 frame