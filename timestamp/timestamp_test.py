from funasr import AutoModel
import os

def test_timestamp():
    # 创建时间戳模型
    model = AutoModel(model="fa-zh")

    # 准备音频和文本文件
    wav_file = f"{model.model_path}/example/asr_example.wav"
    text_file = f"{model.model_path}/example/text.txt"

    print("时间戳预测测试：")
    print(f"音频文件: {wav_file}")
    print(f"文本文件: {text_file}")

    # 生成时间戳
    res = model.generate(
        input=(wav_file, text_file), 
        data_type=("sound", "text")
    )
    print("\n预测结果：")
    print(res)

if __name__ == "__main__":
    test_timestamp() 