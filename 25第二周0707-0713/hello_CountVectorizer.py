from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    'this is a sample text',
    'this text is another example text',
    'this is just another text',
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus).toarray()

print(X)

# [[0 0 1 0 1 1 1]
#  [1 1 1 0 0 2 1]
#  [1 0 1 1 0 1 1]]

# 012 统计在文本向量中出现次数
# 即使文本长度不一，向量化后每个文本向量一样，比较方便
