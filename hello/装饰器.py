# coding: utf-8
import time

def log_time(log_label):
    def wrapper_func(func):
        def wrapper_param(*args, **kwargs):
            start_time = time.clock()
            ref = func(*args, **kwargs)
            end_time = time.clock()
            run_time = end_time - start_time
            print('{log_label}:{run_time}'.format(log_label=log_label, run_time=run_time))
            return ref

        return wrapper_param

    return wrapper_func


"""
@log_time()
语法糖不会影响程序功能，只是让代码更好看而已
让 run_function 等价于 run_function = log_time(run_function)
"""


@log_time('计算CPU时间')
def run_function(count=100000):
    for i in xrange(count):
        pass
        # print(i)

# run_function 等价于 run_function = log_time('cost cpu time')(run_function)
# log_time('cost cpu time') 的返回结果是 wrapper_func
# log_time('cost cpu time')(run_function) 的返回结果是 wrapper_param
# 调用 wrapper_param() 得到 run_function 的结果


if __name__ == '__main__':
    run_function(100000)
    run_function()
