import gym
import fpenv
import numpy as np

from fpenv.FarmerPestEnv import PEST_ATTRIBUTES, PEST_CLASSES
from fpenv.pest_generator.PestGenerator import STATE_SPACE_SIZE
from fpenv.utils import from_attrs_to_Q_state

# zeby byla mozliwosc narysowania wykresu
# 50 powtorzen dla danego algorytmu
#
# agent w czasi ejednej gry sie nie nauczy
#
# n gier - i pozniej powtorzyc


env = gym.make('FarmerPest-v0')

Q = np.zeros([STATE_SPACE_SIZE, PEST_CLASSES])
lr = 0.8  # 0.8
gamma = 0.0  # 0.95
reward_list = []
num_episodes = 50

for i in range(num_episodes):
    print("episode: %d/%d" % (i, num_episodes))
    s = env.reset()
    attrs = s[0]['attrs']
    idx = s[0]['id']
    state_in_Q = from_attrs_to_Q_state(attrs)
    rAll = 0
    done = False
    j = 0
    while j < 300:
        j += 1
        a = np.argmax(Q[state_in_Q, :] + np.random.randn(1, PEST_CLASSES) * (1. / (i + 1)))
        s1, reward, done, _ = env.step((a, idx))
        # if done:
        #     break
        try:
            attrs = s1[0]['attrs']
            idx = s1[0]['id']
        except Exception as e:
            print(s1)
        state_in_Q1 = from_attrs_to_Q_state(attrs)
        Q[state_in_Q, a] += lr * (reward + gamma * np.max(Q[state_in_Q1, :]) - Q[state_in_Q, a])
        rAll += reward
        state_in_Q = state_in_Q1

    reward_list.append(rAll)

print("Score over time: " + str(sum(reward_list) / num_episodes))
print("Q table")
print(Q)
