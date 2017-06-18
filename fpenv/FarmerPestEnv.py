import random

import gym
from gym.spaces import Tuple, Discrete
from gym.utils import seeding

from fpenv.pest_generator.PestGenerator import PestGenerator2
import matplotlib.pyplot as plt
import numpy as np




# pojawianie sie owadow (jak poprzedni zginal)
# rozklady prawdopodobienstwa atrbytuy - klasy

# moze byc tak, ze rozne akcje moga zabijac, ale z roznym opoznieniem (Albo w ogole)

PEST_CLASSES = 8
PEST_ATTRIBUTES = 4
PEST_AMOUNT = 50


class FarmerPestEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def _close(self):
        avg = np.average(self.history[3:], axis=0)

        initial = list(enumerate(avg))
        x, y = list(map(lambda l: l[0], initial)), list(map(lambda l: l[1], initial))
        plt.plot(x, y)
        plt.show()

    def __init__(self):
        super().__init__()
        self.pg = PestGenerator2()
        self.pests = [PestInEnv(x, True, self.pg.generate()) for x in range(PEST_AMOUNT)]

        # pest can be only killed with specific substance
        # e.g.: farmer decides to kill pest with ID using substance SUBST -> action: (SUBST, ID)
        self.action_space = Tuple((Discrete(PEST_CLASSES), Discrete(PEST_AMOUNT)))
        self.history = []
        self.killed_per_step = []

    def _step(self, action):
        assert self.action_space.contains(action), "%r (%s) invalid" % (action, type(action))
        klass, id = action
        reward = 0
        if self.pests[id].pest.klass == klass and self.pests[id].alive:
            reward = 1
            self.pests[id].alive = False

        done = len([x for x in self.pests if x.alive]) == 0

        self.killed_per_step.append(len([x for x in self.pests if not x.alive]))
        return self._pest_array_to_state(), reward, done, {}

    def _reset(self):
        self.pests = [PestInEnv(x, True, self.pg.generate()) for x in range(PEST_AMOUNT)]
        self.history.append(self.killed_per_step)
        self.killed_per_step = []
        return self._pest_array_to_state()

    def _seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def _render(self, mode='human', close=False):
        print("=================================")
        print("ALIVE:")
        for pestInEnv in filter(lambda x: x.alive, self.pests):
            print("Class: {} -> attributes: {}".format(pestInEnv.pest.klass, pestInEnv.pest.attributes))
        print("KILLED:")
        for pestInEnv in filter(lambda x: not x.alive, self.pests):
            print("Class: {} -> attributes: {}".format(pestInEnv.pest.klass, pestInEnv.pest.attributes))


    @staticmethod
    def _class_assigner():
        return lambda attributes: int(divmod(attributes[0], 1./PEST_CLASSES)[0])

    def _pest_array_to_state(self):
        list = [pestState for pestState in map(lambda x: {"id": x.id, "attrs": x.pest.attributes}, [x for x in self.pests if x.alive])]
        random.shuffle(list)
        return list


class PestInEnv(object):
    def __init__(self, id, alive, pest):
        super().__init__()
        self.id = id
        self.alive = alive
        self.pest = pest
