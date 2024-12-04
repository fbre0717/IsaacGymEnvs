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
fbx_file = "data/gainer_wonder.fbx"
motion = SkeletonMotion.from_fbx(
    fbx_file_path=fbx_file,
    root_joint="Hips",
    fps=30
)

# X축 90도, Z축 90도 회전을 위한 쿼터니언
rotation_quat_x = create_rotation_quat(90, 'x')
rotation_quat_z = create_rotation_quat(90, 'z')

# 마지막 프레임의 로컬 회전값에 X축과 Z축 회전 순차적으로 적용
final_rotation = motion.local_rotation[-1].clone()
final_rotation[0] = quat_mul_norm(rotation_quat_z, 
                    quat_mul_norm(rotation_quat_x, final_rotation[0]))
# Translation 수정 (Y축 -1, Z축 +1)
root_translation = motion.root_translation[-1].clone()
root_translation[1] = root_translation[1] - 0.95  # Y값에 -1 적용
root_translation[2] = root_translation[2] + 0.97  # Z값에 +1 적용

# 회전과 이동이 적용된 T-pose 생성
tpose = SkeletonState.from_rotation_and_root_translation(
    skeleton_tree=motion.skeleton_tree,
    r=final_rotation,  # 회전이 적용된 로컬 회전값
    t=root_translation,  # 수정된 루트 위치
    is_local=True  # 로컬 좌표계 사용
)

# T-pose 시각화 (선택사항)
plot_skeleton_state(tpose)
tpose.to_file("data/wonder_tpose.npy")