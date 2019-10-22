import gym
from gym import error, spaces, utils
from gym.utils import seeding


class TicTacToeEnviroment(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.observation_space = spaces.Discrete()

    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self, mode='human', close=False):
        pass


if __name__ == '__main__':
    print(gym.spaces.Discrete(9))