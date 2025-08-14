# 第三周和第四周学习一点python爬虫知识

# 爬虫：通过编写程序从互联网上获取资源


# 一个最基本的网页爬取程序
from urllib.request import urlopen
url = 'http://www.baidu.com'
rest1 = urlopen(url)

with open('firstbaidu.html', mode='wb') as f:
    data = rest1.read().decode("utf-8")
    # print(data)
    f.write(data)
print("over!")