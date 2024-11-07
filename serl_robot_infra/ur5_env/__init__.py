from gym.envs.registration import register
import numpy as np

register(
    id="UR5Env-Vision-v0",
    entry_point="franka_env.envs:UR5Env",
    max_episode_steps=100,
)

register(
    id="UR5PegInsert-Vision-v0",
    entry_point="franka_env.envs.peg_env:UR5PegInsert",
    max_episode_steps=100,
)

register(
    id="UR5PCBInsert-Vision-v0",
    entry_point="franka_env.envs.pcb_env:UR5PCBInsert",
    max_episode_steps=100,
)

register(
    id="UR5CableRoute-Vision-v0",
    entry_point="franka_env.envs.cable_env:UR5CableRoute",
    max_episode_steps=100,
)

register(
    id="UR5BinRelocation-Vision-v0",
    entry_point="franka_env.envs.bin_relocation_env:UR5BinRelocation",
    max_episode_steps=100,
)
