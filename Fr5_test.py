'''
 @Author: Prince Wang 
 @Date: 2024-02-22 
 @Last Modified by:   Prince Wang 
 @Last Modified time: 2023-10-24 23:04:04 
'''


from stable_baselines3 import A2C,PPO,DDPG,TD3
from stable_baselines3.common.vec_env import DummyVecEnv,SubprocVecEnv
from Fr5_env import FR5_Env
import time
import os
from stable_baselines3.common.utils import set_random_seed
from stable_baselines3.common.logger import configure
from utils.arguments import get_args

if __name__ == '__main__':
    args, kwargs = get_args()
    env = FR5_Env(gui=args.gui)
    env.render()
    model = PPO.load(args.model_path)
    # model = TD3.load("F:\\Pycharm_project\\RL\\models\\TD3\\TD3-run-eposide270.zip")
    # model = DDPG.load("F:\\Pycharm_project\\RL\\models\\DDPG\\DDPG-run-eposide282.zip")
    test_num = args.test_num  # 测试次数
    success_num = 0  # 成功次数
    print("测试次数：",test_num)
    for i in range(test_num):
        state,_ = env.reset()
        done = False 
        score = 0
        # time.sleep(3)
        
        while not done:
            # action = env.action_space.sample()     # 随机采样动作
            action, _ = model.predict(observation=state,deterministic=True)
            # print("state:",state)
            # print("action:",action)
            state, reward, done, _,info = env.step(action=action)
            score += reward
            # env.render()
            time.sleep(0.01)

        if info['is_success']:
            success_num += 1
        print("奖励：",score)
    success_rate = success_num/test_num
    print("成功率：",success_rate)
    env.close()

