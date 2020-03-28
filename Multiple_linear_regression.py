import numpy as np
# 线性回归函数
from sklearn.linear_model import LinearRegression
# 用于切分数据集
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# 加载鸢尾花数据集
iris = load_iris()
# 使用鸢尾花的data和target作为x和y
X, y = iris.data, iris.target

lr = LinearRegression()
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.25,
                                                    random_state=0)
lr.fit(X_train, y_train)
print("权重:", lr.coef_)
print("截距:", lr.intercept_)
y_hat = lr.predict(X_test)
print(
    "拟合函数:",
    'y={}x1+{}x2+{}x3+{}x4+{}'.format(lr.coef_[0], lr.coef_[1], lr.coef_[2],
                                      lr.coef_[3], lr.intercept_))
