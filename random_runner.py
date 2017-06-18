import gym
import fpenv
import numpy as np

from fpenv.FarmerPestEnv import PEST_ATTRIBUTES, PEST_CLASSES
from fpenv.pest_generator.PestGenerator import STATE_SPACE_SIZE

env = gym.make('FarmerPest-v0')
env.reset()
num_episodes = 50

for i in range(num_episodes):
    print("episode: %d/%d" % (i, num_episodes))
    for j in range(300):
        env.step(env.action_space.sample())
    env.reset()

env.close()
