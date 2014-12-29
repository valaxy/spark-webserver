# encoding=utf-8

# data是一个字典, 存储所有数据的状态
data = {}


def setData(time, value):
    data[time] = value


def getData(time):
    if time in data:
        return data[time]
    else:
        return None