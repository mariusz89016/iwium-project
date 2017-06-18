from gym.envs.registration import register

register(
    id='FarmerPest-v0',
    entry_point='fpenv.FarmerPestEnv:FarmerPestEnv',
    kwargs={}
)