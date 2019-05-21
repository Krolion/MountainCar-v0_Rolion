def comp(x, y):
    return (score[x] > score[y])

import gym
import random
from operator import itemgetter
mut = 500
pool_size = 400
new_pool = 1000
sharp = 1
sep = 10
cntr = 0
time_l = 100
survivors = 20
number = 2786
flag = 0
env = gym.make('MountainCar-v0')
q = 1
file = open("Q.txt", "r")
s = file.readlines()
s = [x.strip().split(" ") for x in s]
tact = [list(map(int,x)) for x in s]
file.close()
fscore = 0
for i in range(100):
    kappa_d = -1
    kappa_s = 0
    observation = env.reset()
    for t in range(time_l + 50):
        action = env.action_space.sample()
        if (t == 0):
            sp = int(4.99*sep*(observation[0] + 0.6))
        if (t < 100):
            observation, reward, done, info = env.step(int(tact[sp][t]))
        else:
            observation, reward, done, info = env.step(1)
        kappa_d = max(observation[0],kappa_d)
        kappa_s += reward
        if done:
            break
    fscore = max(fscore,kappa_s)
print(str(fscore))
