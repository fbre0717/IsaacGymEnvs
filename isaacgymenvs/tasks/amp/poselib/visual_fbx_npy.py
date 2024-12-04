import os
import json

from poselib.skeleton.skeleton3d import SkeletonTree, SkeletonState, SkeletonMotion
from poselib.visualization.common import plot_skeleton_state, plot_skeleton_motion_interactive, plot_skeleton_motion

# source fbx file path
# fbx_file = "data/01_01_cmu.fbx"
# fbx_file = "data/gainer_wonder.fbx"
# fbx_file = "data/tdr_corks_wonder.fbx"
# import fbx file - make sure to provide a valid joint name for root_joint
# fbx_motion = SkeletonMotion.from_fbx(
#     fbx_file_path=fbx_file,
#     root_joint="Hips",
#     fps=60
# )
# plot_skeleton_motion_interactive(fbx_motion)



# npy_file = "data/amp_humanoid_backflip.npy"
# npy_file = "data/amp_humanoid_cartwheel.npy"
# npy_file = "data/tricking/gainer_wonder_amp.npy"
# npy_file = "data/tricking/amp_tdr_corks_wonder.npy"
# npy_file = "data/shosei/shosei_corks.npy"
# npy_file = "data/shosei/amp_shosei_dcorks2_nostep.npy"
# npy_file = "data/shosei/shosei_corks.npy"
# npy_file = "data/loopkicks/amp_backflip.npy"
# npy_file = "data/loopkicks/amp_fulltwist0.npy"
npy_file = "data/loopkicks/amp_cheat720 copy.npy"
# npy_file = "data/loopkicks/amp_raiz0.npy"


npy_motion : SkeletonMotion = SkeletonMotion.from_file(npy_file)
plot_skeleton_motion_interactive(npy_motion)
# plot_skeleton_motion(npy_motion)

# npy_file = "data/amp_humanoid_tpose.npy"
# npy_file = "data/wonder_tpose.npy"
# npy_state = SkeletonState.from_file(npy_file)
# plot_skeleton_state(npy_state)




