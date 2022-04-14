
# 时间 ： 2020/7/20 17:03
# 作者 ： Dixit
# 文件 ： main_versus.py
# 项目 ： moziAIBT
# 版权 ： 北京华戍防务技术有限公司

from mozi_ai_sdk.bt_test.env.env import Environment
from mozi_ai_sdk.bt_test.env import etc
from mozi_ai_sdk.bt_test.utils.bt_agent_antiship import CAgent
import argparse
import sys
import os
import traceback

#  设置墨子安装目录下bin目录为MOZIPATH，程序会自动启动墨子
os.environ['MOZIPATH'] = 'D:\\mozi_server\\Mozi\\MoziServer\\bin'

parser = argparse.ArgumentParser()
parser.add_argument("--avail_ip_port", type=str, default='127.0.0.1:6060')
parser.add_argument("--platform_mode", type=str, default='versus1')
parser.add_argument("--side_name", type=str, default='红方')
parser.add_argument("--agent_key_event_file", type=str, default=None)
AREA = [('20.78','127.35'),('23.82','138.62'),('18.68','135.53'),('17.1','131.2')]

def run(env, side_name=None):
    """
       行为树运行的起始函数
       :param env: 墨子环境
       :param side_name: 推演方名称
       :return:
       """
    if not side_name:
        side_name = '红方'
    # 连接服务器，产生mozi_server
    env.start()
    # 实例化智能体
    agent = CAgent()

    # 重置函数，加载想定,拿到想定发送的数据
    env.scenario = env.reset()
    side = env.scenario.get_side_by_name(side_name)
    # 初始化行为树
    agent.init_bt(env, side_name, 0, '')
    step_count = 0
    while True:
        # 更新动作
        agent.update_bt(side_name, env.scenario)
        env.step()
        print(f"'推演步数：{step_count},本方得分：{side.iTotalScore}")
        step_count += 1
        if env.is_done():
            print('推演已结束！')
            sys.exit(0)
        else:
            pass


def main():

    args = parser.parse_args()
    if args.platform_mode == 'versus':
        print('比赛模式')
        ip_port = args.avail_ip_port.split(":")
        ip = ip_port[0]
        port = ip_port[1]
        # 是否传入决策步长需讨论
        env = Environment(ip, port, duration_interval=etc.DURATION_INTERVAL, app_mode=1,
                          agent_key_event_file=args.agent_key_event_file, platform_mode=args.platform_mode)
        run(env, args.side_name)
    else:
        print('默认开发模式')
        env = Environment(etc.SERVER_IP, etc.SERVER_PORT, etc.PLATFORM, etc.SCENARIO_NAME, etc.SIMULATE_COMPRESSION,
                          etc.DURATION_INTERVAL, etc.SYNCHRONOUS, etc.app_mode)

        run(env)


try:
    main()
except Exception as e:
    # error_file = open(__file__.replace('main_versus.py', 'error.log'), 'w', encoding='utf-8')
    error_file = open('error.log', 'w', encoding='utf-8')
    exc_type, exc_value, exc_obj = sys.exc_info()
    traceback.print_exc(file=error_file)
    sys.exit()
