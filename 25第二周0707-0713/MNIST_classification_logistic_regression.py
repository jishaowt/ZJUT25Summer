from matplotlib import pyplot as plt
from sklearn.datasets import fetch_openml
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
# 载入MNIST手写数字图片数据集
mnist = fetch_openml("mnist_784",version=1)

img0 = np.array(mnist.date)[0]
print(np.array(mnist.target)[0])
img0 = img0.reshape(28,28)
plt.imshow(img0, cmap="gray")
plt.show()

# 数据集预处理：标准归一化
# scaler = StandardScaler()
# X = scaler.fit_transform(mnist.data)

# 划分数据集为训练集与测试集
X_train,X_test,y_train,y_test = train_test_split(mnist.data, mnist.target,test_size=0.2, random_state=42)

# 创建逻辑回归模型
model = LogisticRegression(max_iter=100)

# 在训练集上训练模型
model.fit(X_train,y_train)

# 在测试集上预测模型
y_pred = model.predict(X_test)

# 输出模型的准确率
print("Accuracy:%.2f" %accuracy_score(y_test, y_pred))

print(model.predict([img0]))