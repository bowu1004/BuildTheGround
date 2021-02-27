# Eigenvalues and Eigenvectors, Rank/Trace

---

## + 特征值个数等于矩阵的维数，其中，不等于0且不同的特征值个数为矩阵的秩。

## + 对于Normal Equation优化方法（vs梯度下降法）来说可能出现matrix is singular即矩阵不可逆。
+ 第一种情况：出现了两个相似的特征，这个两个特征可以用一个线性关系进行表示。例如，米和英尺，这两个都是用来描述长度的单位，且他们之间可以进行相互转化，如果特征值同时出现他们两个，就会出现矩阵不可逆的情况。
  + 解决方法：去掉任意一个即可。
+ 第二种情况：特征dim特别多，但是数据集的数量N特别少, e.g. N>dim。
  + 解决方法：增加数据集或**减少特征dim**。降维之后再加model就是这个道理。

## + Normal Equation优化方法 vs 梯度下降法
+ Normal Equation optimization method:
  + no need of iteration;
  + no need of learning rate;
  + O({feature dim}^3);
+ GD method: O({k*{feature dim}}^2)

## + [NLP中Word2Vec模型详解](https://zhuanlan.zhihu.com/p/44127907)
