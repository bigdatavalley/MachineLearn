import numpy as np
# 线性回归函数
from sklearn.linear_model import LinearRegression
# 用于切分数据集
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# 加载鸢尾花数据集
iris = load_iris()
# 使用花瓣长和花瓣宽作为x,y
X, y = iris.data[:, 2].reshape(-1, 1), iris.data[:, 3]

lr = LinearRegression()
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.25,
                                                    random_state=0)
lr.fit(X_train, y_train)
print("权重:", lr.coef_)
print("截距:", lr.intercept_)
y_hat = lr.predict(X_test)
print("拟合函数:", 'y={}x+{}'.format(lr.coef_[0], lr.intercept_))

import matplotlib.pyplot as plt

# mac下使用中文
plt.rcParams["font.family"] = 'Arial Unicode MS'
# win下使用中文
# plt.rcParams["font.family"] = 'SimHei'
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["font.size"] = 15

plt.figure(figsize=(10, 6), dpi=300)
plt.scatter(X_train, y_train, c='orange', label='训练集')
plt.scatter(X_test, y_test, c='blue', marker='D', label='测试集')
plt.plot(X, lr.predict(X), 'r-')
plt.legend()
plt.xlabel("花瓣长")
plt.ylabel("花瓣宽")

plt.figure(figsize=(15, 6), dpi=300)
plt.plot(y_test, label="真实值", color='r', marker='o')
plt.plot(y_hat, label="预测值", ls='--', color='g', marker='o')
plt.xlabel("测试集数据序号")
plt.ylabel("数据值")
plt.legend()
