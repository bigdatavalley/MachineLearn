import numpy as np
import matplotlib.pyplot as plt

# 在直线 y = 5x+3 附近生成随机点
X = np.arange(0, 5, 0.1)
Z = [5 * x + 3 for  x in X]
Y = [np.random.normal(z, 0.5) for z in Z] 
plt.plot(X, Y, 'ro')
plt.show()


# 使用最小二乘法的代码
from scipy.optimize import leastsq


# 需要拟合的函数func :指定函数的形状
def func(p, x):
    k, b = p
    return k * x + b


# 误差函数：
def error(p, x, y):
    # yi-y
    return func(p, x) - y


# 设置函数的初始参数
p0 = [1, 20]
Para = leastsq(error, p0, args=(X, Y))
print(Para)
k, b = Para[0]

_X = [0, 5]
_Y = [b + k * x for x in _X]

plt.plot(X, Y, 'ro', _X, _Y, 'b', linewidth=2)
plt.title("y = {}x + {}".format(k, b))
plt.show()
