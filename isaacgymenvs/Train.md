Use the following command lines for training the currently included AMP motions:  
(Walk is the default config motion, so doesn't need the motion file specified)  
`python train.py task=HumanoidAMP experiment=AMP_walk`  
`python train.py task=HumanoidAMP ++task.env.motion_file=amp_humanoid_run.npy experiment=AMP_run`  
`python train.py task=HumanoidAMP ++task.env.motion_file=amp_humanoid_dance.npy experiment=AMP_dance`

(Backflip and Hop require the LowGP training config)  
`python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_humanoid_backflip.npy experiment=AMP_backflip`  
`python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_humanoid_hop.npy experiment=AMP_hop`  

(Cartwheel requires hands in the contact body list and the LowGP training config; the default motion for the HumanoidAMPHands task is Cartwheel)
`python train.py task=HumanoidAMPHands train=HumanoidAMPPPOLowGP experiment=AMP_cartwheel`

### Setting
conda install pytorch==1.12.0 torchvision==0.13.0 torchaudio==0.12.0 cudatoolkit=11.6 -c pytorch -c conda-forge

### Location
cd Downloads/isaacgym/IsaacGymEnvs/isaacgymenvs
conda activate torch112-1

## gainer_wonder
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=gainer_wonder2_amp.npy experiment=AMP_gainer max_iterations=2000
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=gainer_wonder2_amp.npy experiment=AMP_gainer max_iterations=100 capture_video=True capture_video_freq=1500 capture_video_len=100 force_render=False

python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=gainer_wonder2_amp.npy experiment=AMP_gainer max_iterations=100 capture_video=True capture_video_freq=10 capture_video_len=60 force_render=False

python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=gainer_wonder2_amp.npy experiment=AMP_gainer checkpoint=runs/AMP_gainer_01-14-51-43/nn/AMP_gainer_01-14-51-45_1000.pth test=True num_envs=64
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=gainer_wonder2_amp.npy experiment=AMP_gainer checkpoint=runs/AMP_gainer_01-14-51-43/nn/AMP_gainer_01-14-51-45_2000.pth test=True num_envs=64
2000 Good

<!-- python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=gainer_wonder_amp.npy experiment=AMP_gainer checkpoint=runs/AMP_gainer_01-06-45-17/nn/AMP_gainer_01-06-45-19_500.pth -->

### example
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=gainer_wonder2_amp.npy experiment=AMP_gainer wandb_activate=True wandb_entity=nvidia wandb_project=rl_games
### real
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=gainer_wonder2_amp.npy experiment=AMP_gainer max_iterations=2000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP

### corks_wodner
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=corks_wonder_amp.npy experiment=AMP_corks max_iterations=5000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=corks_wonder_amp.npy experiment=AMP_corks checkpoint=runs/AMP_corks_01-15-38-34/nn/AMP_corks_01-15-38-36_2000.pth test=True num_envs=64
2000 Bad
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=corks_wonder_amp.npy experiment=AMP_corks max_iterations=5000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=corks_wonder_amp.npy experiment=AMP_corks checkpoint=runs/AMP_corks_01-18-09-49/nn/AMP_corks_01-18-09-53_5000.pth test=True num_envs=64
5000 Bad


### tdr_wonder
python train.py task=HumanoidAMPLeftHand train=HumanoidAMPPPOLowGP ++task.env.motion_file=tdr_wonder_amp.npy experiment=AMP_tdr max_iterations=2000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP
python train.py task=HumanoidAMPLeftHand train=HumanoidAMPPPOLowGP ++task.env.motion_file=tdr_wonder_amp.npy experiment=AMP_tdr checkpoint=runs/AMP_tdr_01-19-35-41/nn/AMP_tdr_01-19-35-45_2000.pth test=True num_envs=64
2000 Good

## shosei

### shosei btwist
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_shosei_btwist.npy experiment=AMP_btwist max_iterations=3000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_shosei_btwist.npy experiment=AMP_btwist checkpoint=runs/AMP_btwist_02-01-02-52/nn/AMP_btwist_02-01-02-55_3000.pth test=True num_envs=64

### shosei corks
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_shosei_corks.npy experiment=AMP_corks_height max_iterations=10000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_shosei_corks.npy experiment=AMP_corks checkpoint=runs/AMP_corks_02-01-57-20/nn/AMP_corks_02-01-57-24_7250.pth test=True num_envs=64

## Basic

python train.py task=HumanoidAMP experiment=AMP_walk max_iterations=1000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP
python train.py task=HumanoidAMP ++task.env.motion_file=amp_humanoid_run.npy experiment=AMP_run max_iterations=1000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP
python train.py task=HumanoidAMP ++task.env.motion_file=amp_humanoid_dance.npy experiment=AMP_dance max_iterations=1000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP

(Backflip and Hop require the LowGP training config)
### Backflip
<!-- HumanoidAMPPPOLowGP 1000, after 1000 -->
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_humanoid_backflip.npy experiment=AMP_backflip max_iterations=1000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_humanoid_backflip.npy experiment=AMP_backflip max_iterations=2000 checkpoint=runs/AMP_backflip_02-04-21-08/nn/AMP_backflip_02-04-21-11.pth wandb_activate=True wandb_entity=2020koh wandb_project=AMP
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_humanoid_backflip.npy experiment=AMP_backflip max_iterations=5000 checkpoint=runs/AMP_backflip_02-07-43-20/nn/AMP_backflip_02-07-43-23.pth wandb_activate=True wandb_entity=2020koh wandb_project=AMP

python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_humanoid_backflip.npy experiment=AMP_backflip checkpoint=runs/AMP_backflip_02-08-57-11/nn/AMP_backflip_02-08-57-14.pth test=True num_envs=64

### Hop
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_humanoid_hop.npy experiment=AMP_hop max_iterations=1000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP

(Cartwheel requires hands in the contact body list and the LowGP training config; the default motion for the HumanoidAMPHands task is Cartwheel)
python train.py task=HumanoidAMPHands train=HumanoidAMPPPOLowGP experiment=AMP_cartwheel max_iterations=1000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP


## LoopKicks

### cheat360
<!-- HumanoidAMPPPOLowGP 3000 -->
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_cheat360.npy experiment=AMP_cheat360 max_iterations=3000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_cheat360.npy experiment=AMP_cheat360 checkpoint=runs/AMP_cheat360_02-04-48-17/nn/AMP_cheat360_02-04-48-21.pth test=True num_envs=64


### fulltwist
<!-- HumanoidAMPPPOLowGP 3000 -->
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_fulltwist0.npy experiment=AMP_fulltwist max_iterations=3000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP checkpoint=runs/AMP_fulltwist_02-05-57-23/nn/AMP_fulltwist_02-05-57-27.pth test=True num_envs=64


### fulltwist AMP
<!-- default 1000 after HumanoidAMPPPOLowGP -->
python train.py task=HumanoidAMP ++task.env.motion_file=amp_fulltwist0.npy experiment=AMP_fulltwist max_iterations=3000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_fulltwist0.npy experiment=AMP_fulltwist max_iterations=3000 checkpoint=runs/AMP_fulltwist_02-08-01-20/nn/AMP_fulltwist_02-08-01-23_1000.pth wandb_activate=True wandb_entity=2020koh wandb_project=AMP


### Raiz
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_raiz0.npy experiment=AMP_raiz max_iterations=5000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_raiz0.npy experiment=AMP_raiz checkpoint=runs/AMP_raiz_02-10-55-49/nn/AMP_raiz_02-10-55-52.pth test=True num_envs=64

### Backflip
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_backflip.npy experiment=AMP_backflip max_iterations=5000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_backflip.npy experiment=AMP_backflip checkpoint=runs/AMP_backflip_02-09-41-55/nn/AMP_backflip_02-09-41-59.pth test=True num_envs=64



1. load default backflip
2. start custom backflip
3. start custom raiz


python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_humanoid_backflip.npy experiment=AMP_backflip max_iterations=5000 checkpoint=runs/AMP_backflip_02-07-43-20/nn/AMP_backflip_02-07-43-23.pth wandb_activate=True wandb_entity=2020koh wandb_project=AMP headless=True ; python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_backflip.npy experiment=AMP_backflip max_iterations=5000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP headless=True ; python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_raiz0.npy experiment=AMP_raiz max_iterations=5000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP headless=True



python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_humanoid_backflip.npy experiment=AMP_backflip checkpoint=runs/AMP_backflip_02-08-57-11/nn/AMP_backflip_02-08-57-14.pth test=True num_envs=64



### TDR Corks
python train.py task=HumanoidAMPLeftHand train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_tdr_corks_wonder.npy experiment=AMP_tdr_corks max_iterations=5000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP headless=True

python train.py task=HumanoidAMPLeftHand train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_tdr_corks_wonder.npy experiment=AMP_tdr_corks checkpoint=runs/AMP_tdr_corks_02-13-07-42/nn/AMP_tdr_corks_02-13-07-45.pth test=True num_envs=64



# Cubic Spline + Height Limit
### shosei corks
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_shosei_corks.npy experiment=AMP_corks_height checkpoint=runs/AMP_corks_height_02-19-23-26/nn/AMP_corks_height_02-19-23-30_2000.pth test=True num_envs=64
### shosei btwist
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_shosei_btwist.npy experiment=AMP_btwist_height max_iterations=3000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_shosei_btwist.npy experiment=AMP_btwist_height max_iterations=4000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP checkpoint=runs/AMP_btwist_height_02-20-02-45/nn/AMP_btwist_height_02-20-02-49.pth
### shosei dcorks
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_shosei_dcorks2_nostep.npy experiment=AMP_dcorks_height_nostep max_iterations=5000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP ; 



python train.py task=HumanoidAMP ++task.env.motion_file=amp_shosei_dcorks2_nostep.npy experiment=AMP_dcorks_height_nostep_AMP max_iterations=5000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP
python train.py task=HumanoidAMP ++task.env.motion_file=amp_shosei_dcorks2.npy experiment=AMP_dcorks_height_step_AMP max_iterations=5000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_shosei_dcorks2.npy experiment=AMP_dcorks_height_step_AMPLow max_iterations=5000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP

### Test
### amp_fulltwist0
python train.py task=HumanoidAMP ++task.env.motion_file=amp_fulltwist0.npy experiment=AMP_fulltwist checkpoint=runs/AMP_fulltwist_02-05-57-23/nn/AMP_fulltwist_02-05-57-27.pth test=True num_envs=64
### amp_humanoid_backflip
python train.py task=HumanoidAMP ++task.env.motion_file=amp_humanoid_backflip.npy checkpoint=runs/AMP_backflip_02-08-57-11/nn/AMP_backflip_02-08-57-14.pth test=True num_envs=64
### amp_backflip Bad
python train.py task=HumanoidAMP ++task.env.motion_file=amp_backflip.npy checkpoint=runs/AMP_backflip_02-09-41-55/nn/AMP_backflip_02-09-41-59.pth test=True num_envs=64
### corks1
python train.py task=HumanoidAMP ++task.env.motion_file=corks_wonder_amp.npy checkpoint=runs/AMP_corks_01-18-09-49/nn/AMP_corks_01-18-09-53.pth test=True num_envs=64
### corks2
python train.py task=HumanoidAMP ++task.env.motion_file=amp_shosei_corks.npy checkpoint=runs/AMP_corks_02-01-57-20/nn/AMP_corks_02-01-57-24_7250.pth test=True num_envs=64

### btwist height Good
python train.py task=HumanoidAMP ++task.env.motion_file=amp_shosei_btwist.npy checkpoint=runs/AMP_btwist_height_02-20-56-49/nn/AMP_btwist_height_02-20-56-53_4000.pth test=True num_envs=64
### corks height Good
python train.py task=HumanoidAMP ++task.env.motion_file=amp_shosei_corks.npy checkpoint=runs/AMP_corks_height_02-19-23-26/nn/AMP_corks_height_02-19-23-30_2000.pth test=True num_envs=64
### double corks height Good(default GP)
python train.py task=HumanoidAMP ++task.env.motion_file=amp_shosei_dcorks2_nostep.npy checkpoint=runs/AMP_dcorks_height_nostep_02-21-46-13/nn/AMP_dcorks_height_nostep_02-21-46-17_5000.pth test=True num_envs=64
python train.py task=HumanoidAMP ++task.env.motion_file=amp_shosei_dcorks2_nostep.npy checkpoint=runs/AMP_dcorks_height_nostep_AMP_02-23-19-39/nn/AMP_dcorks_height_nostep_AMP_02-23-19-42_5000.pth test=True num_envs=64
python train.py task=HumanoidAMP ++task.env.motion_file=amp_shosei_dcorks2.npy checkpoint=runs/AMP_dcorks_height_step_AMP_03-00-46-44/nn/AMP_dcorks_height_step_AMP_03-00-46-47_5000.pth test=True num_envs=64
python train.py task=HumanoidAMP ++task.env.motion_file=amp_shosei_dcorks2.npy checkpoint=runs/AMP_dcorks_height_step_AMPLow_03-02-04-59/nn/AMP_dcorks_height_step_AMPLow_03-02-05-02_5000.pth test=True num_envs=64


### Train
python train.py task=HumanoidAMP ++task.env.motion_file=amp_raiz0.npy experiment=AMP_raiz_GP max_iterations=5000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP headless=True ; python train.py task=HumanoidAMP ++task.env.motion_file=amp_fulltwist0.npy experiment=AMP_fulltwist_GP max_iterations=5000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP headless=True ; python train.py task=HumanoidAMP ++task.env.motion_file=amp_cheat720.npy experiment=AMP_cheat720_GP max_iterations=5000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP headless=True

### Test
python train.py task=HumanoidAMP ++task.env.motion_file=amp_raiz0.npy test=True num_envs=64 checkpoint=runs/AMP_raiz_GP_03-05-59-34/nn/AMP_raiz_GP_03-05-59-37.pth
python train.py task=HumanoidAMP ++task.env.motion_file=amp_fulltwist0.npy test=True num_envs=64 checkpoint=runs/AMP_fulltwist_GP_03-07-08-03/nn/AMP_fulltwist_GP_03-07-08-06.pth
python train.py task=HumanoidAMP ++task.env.motion_file=amp_cheat720.npy test=True num_envs=64 checkpoint=runs/AMP_cheat720_GP_03-08-20-12/nn/AMP_cheat720_GP_03-08-20-15.pth

### LowTrain
python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_raiz0.npy experiment=AMP_raiz_LowGP max_iterations=5000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP headless=True checkpoint=runs/AMP_raiz_GP_03-05-59-34/nn/AMP_raiz_GP_03-05-59-37_2000.pth ; python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_fulltwist0.npy experiment=AMP_fulltwist_LowGP max_iterations=5000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP headless=True checkpoint=runs/AMP_fulltwist_GP_03-07-08-03/nn/AMP_fulltwist_GP_03-07-08-06_2000.pth ; python train.py task=HumanoidAMP train=HumanoidAMPPPOLowGP ++task.env.motion_file=amp_cheat720.npy experiment=AMP_cheat720_LowGP max_iterations=5000 wandb_activate=True wandb_entity=2020koh wandb_project=AMP headless=True checkpoint=runs/AMP_cheat720_GP_03-08-20-12/nn/AMP_cheat720_GP_03-08-20-15_2000.pth

