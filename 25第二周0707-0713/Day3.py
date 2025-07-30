from matplotlib import pyplot as plt
from sklearn.datasets import fetch_openml
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import time

try:
    # 载入MNIST手写数字图片数据集
    print("正在加载MNIST数据集...")
    mnist = fetch_openml("mnist_784", version=1)

    # 修正：使用正确的属性名
    img0 = np.array(mnist.data)[0]
    print(f"第一张图片的标签: {np.array(mnist.target)[0]}")

    # 显示第一张图片
    img0_vis = img0.reshape(28, 28)
    plt.imshow(img0_vis, cmap="gray")
    plt.title(f"Label: {mnist.target[0]}")
    plt.axis('off')

    # 修正：自动关闭绘图窗口
    plt.show(block=False)
    plt.pause(3)  # 显示3秒
    plt.close()

    # 数据集预处理：标准归一化
    print("正在进行数据预处理...")
    scaler = StandardScaler()
    X = scaler.fit_transform(mnist.data)

    # 划分数据集为训练集与测试集
    print("正在划分训练集和测试集...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, mnist.target, test_size=0.2, random_state=42
    )

    # 创建逻辑回归模型
    print("正在初始化逻辑回归模型...")
    model = LogisticRegression(max_iter=2000, verbose=1, n_jobs=-1)

    # 在训练集上训练模型
    print("开始训练模型 (这可能需要几分钟)...")
    start_time = time.time()
    model.fit(X_train, y_train)
    print(f"训练完成，耗时: {time.time() - start_time:.2f} 秒")

    # 在测试集上预测模型
    print("正在进行模型预测...")
    y_pred = model.predict(X_test)

    # 输出模型的准确率
    accuracy = accuracy_score(y_test, y_pred)
    print(f"模型准确率: {accuracy:.2%}")

    # 修正：使用正确预处理的图像进行预测
    img0_processed = scaler.transform([mnist.data[0]])
    prediction = model.predict(img0_processed)
    print(f"第一张图片的预测结果: {prediction[0]}")

except Exception as e:
    print(f"程序运行出错: {str(e)}")