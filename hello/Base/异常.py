# coding: utf-8

import os;


def get_int1(string):
    try:
        result = int(string)
    except(ValueError, TypeError) as e:
        print(e)
        result = 0
    return result


def get_int2(string):
    try:
        result = int(string)
        has_exception = False
    except(ValueError, TypeError):
        has_exception = True
        result = 0
    finally:
        print('一定会执行')
    return has_exception, result


has_exception, result = get_int2('exception')



def main():
    filename = 'number.txt'
    # if os.path.exists(filename):
    #     file = open(filename)
    #     try:
    #         numbers = [get_int1(line) for line in file.readlines()]
    #     finally:
    #         file.close()
    # else:
    #     print('%s 不存在' % filename)
    #     numbers = []
    # return  numbers

    if os.path.exists(filename):
        #with 代码块结束后会自动调用 file.close() 方法关闭文件
        with open(filename) as file:
            numbers = [get_int1(line) for line in file.readlines()]
    else:
        print('%s 不存在' % filename)
        numbers = []
    return numbers


if __name__ == '__main__':
    print(main())