import autoit
import time
from Autoit01.data import csv01

wuqi00 = ('尖针', '佛珠', '龙心', '宝石', '光剑',
          '法杖', '布甲', '双刀', '琵琶', '飞轮',
          '雷剑')

# wuqi00 = ('尖针', '佛珠', '宝石', '布甲', '双刀', '琵琶', '雷剑')


def needle(x, y, wait_time):
    autoit.win_activate('英雄战争 | 在线动作类 RPG - Google Chrome')
    time.sleep(1)
    autoit.mouse_click('left', x, y, 1, 1)
    print('点击任务')
    time.sleep(1)
    autoit.mouse_click('left', 1193, 675, 1, 1)
    print('确认敌人')
    time.sleep(1)
    autoit.mouse_click('left', 1352, 760, 1, 1)
    print('确认队伍')
    # ---------------------------------
    time.sleep(2)
    # ---------------------------------
    autoit.mouse_click('left', 1352, 740, 1, 1)
    print('自动')
    time.sleep(wait_time)
    autoit.mouse_click('left', 1054, 750, 1, 1)
    print('结束')
    time.sleep(1)
    pass


def single(wuqi01, time0=60):
    x = int(csv01.obtain_value(wuqi01, 'x'))
    y = int(csv01.obtain_value(wuqi01, 'y'))
    needle(x, y, time0)
    print('--' * 10 + '\n' + '单次刷%s图' % wuqi01)


def cycle_list(num=1, time0=60):
    for i in range(1, num + 1):
        for wuqi01 in wuqi00:
            x = int(csv01.obtain_value(wuqi01, 'x'))
            y = int(csv01.obtain_value(wuqi01, 'y'))
            needle(x, y, time0)
            print('--' * 10 + '\n' + '第' + str(i) + '轮刷图--' + wuqi01 + '--' * 10 + '\n')
    a = len(wuqi00) * num
    print(a * 6)


def cycle_one(wuqi, num=1, time0=70):
    for i in range(1, num + 1):
        x = int(csv01.obtain_value(wuqi, 'x'))
        y = int(csv01.obtain_value(wuqi, 'y'))
        needle(x, y, time0)
        print('--第%d次刷图--' % i)


if __name__ == "__main__":
    # cycle_one('宝石', 20, 60)
    cycle_one('佛珠', 15, 60)
    # cycle_one('大帽', 5, 80)  # 第四章
    # cycle_list(1, 100)
