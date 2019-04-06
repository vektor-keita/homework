# -*- coding: utf-8 -*-

"""
二分法による計算
√２をf(x)= x**2 - 2 = 0
を解く事で求める
"""

a = 2.0


def function(x):
    """
    f(x)= x**2 - a
    :param x double
    :return double 関数の戻り値
        関数の引数
    """
    return x * x - a


class MethodError(Exception):
    pass


def bisection_method(start, end):
    """
    :param start: double
    :param end: double
    :return: double
        2分法によるf(x) = 0 の解
    """
    left = start
    right = end
    k = (left - right)/2.0

    if function(left)*function(right) > 0:
        raise MethodError("引数の値が不正です。")

    while abs(function(k)) > 1.0e-10:
        if function(left)*function(k) > 0:
            left = k
        else:
            right = k

        k = (left + right)/2.0

    return k


if __name__ == '__main__':
    result = bisection_method(0.5, 2.0)
    print(result)


