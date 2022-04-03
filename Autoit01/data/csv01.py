import csv
import os

root_path = os.path.abspath(os.path.dirname(__file__)).split('Autoit01')[0]
document = root_path + 'Autoit01\data\job.csv'


def obtain_all():
    # 获取全部数据
    with open(document, 'r') as f:
        reader = csv.reader(f)
        print(type(reader))

        for row in reader:
            print(row)


def obtain_line():
    # 获取某一行
    with open(document, 'r') as f:
        reader = csv.reader(f)
        result = list(reader)
        print(result[1])


def obtain_list():
    # 获取某一列
    with open(document, 'r') as f:
        reader = csv.reader(f)
        for i in reader:
            print(i[0])


def obtain_value(wuqi, xy):
    if wuqi == '尖针':
        wuqi_1 = 1
    elif wuqi == '佛珠':
        wuqi_1 = 2
    elif wuqi == '龙心':
        wuqi_1 = 3
    elif wuqi == '宝石':
        wuqi_1 = 4
    elif wuqi == '大帽':
        wuqi_1 = 5
    elif wuqi == '光剑':
        wuqi_1 = 6
    elif wuqi == '法杖':
        wuqi_1 = 7
    elif wuqi == '双刀':
        wuqi_1 = 8
    elif wuqi == '布甲':
        wuqi_1 = 9
    elif wuqi == '雷剑':
        wuqi_1 = 10
    elif wuqi == '琵琶':
        wuqi_1 = 11
    elif wuqi == '飞轮':
        wuqi_1 = 12
    elif wuqi == '护甲':
        wuqi_1 = 13
    elif wuqi == '魔球':
        wuqi_1 = 14

    if xy == 'x':
        x_y = 1
    elif xy == 'y':
        x_y = 2
    else:
        x_y = int(xy)

    with open(document, 'r') as f:
        reader = csv.reader(f)
        result = list(reader)
        # print(result)
        a = result[wuqi_1][x_y]
        a = int(a)
    return a


if __name__ == "__main__":
    obtain_value('宝石', 'x')
