# follow-up blogs
Please visit the author's blog at https://zhuanlan.zhihu.com/MLstudy.

E.g.

1. [scikit-learn源码之线性模型](https://zhuanlan.zhihu.com/p/55238718):
+ LinearRegression：普通线性回归，最小二乘法求解
+ Lasso：+L1正则化，坐标下降法求解
+ Ridge：+L2正则化，多种求解方法，如svd：奇异值分解法，比cholesky更适合计算奇异矩阵；cholesky：使用标准的scipy.linalg.solve方法；sparse_cg：共轭梯度法，scipy.sparse.linalg.cg,适合大数据的计算；lsqr：最小二乘法，scipy.sparse.linalg.lsqr；sag：随机平均梯度下降法，在大数据下表现良好。
+ LogisticRegression：普通logistic分类，多种求解方法
+ LogisticRegressionCV：类似LogisticRegression，区别为Regularizaiton参数C由交叉验证求出