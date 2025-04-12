from funasr import AutoModel

def test_punctuation():
    # 创建标点模型
    model = AutoModel(model="ct-punc")

    # 测试文本列表
    test_texts = [
        "那今天的会就到这里吧 happy new year 明年见",
        "人工智能是计算机科学的一个分支它企图了解智能的实质并生产出一种新的能以人类智能相似的方式做出反应的智能机器",
        "深度学习是机器学习的分支是一种以人工神经网络为架构对数据进行表征学习的算法"
    ]

    print("标点恢复测试结果：")
    for i, text in enumerate(test_texts, 1):
        print(f"\n测试文本 {i}:")
        print(f"原始文本: {text}")
        res = model.generate(input=text)
        print(f"添加标点: {res}")

if __name__ == "__main__":
    test_punctuation() 