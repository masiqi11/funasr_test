from funasr import AutoModel
import os

def test_offline_vad():
    # 创建 VAD 模型
    model = AutoModel(model="fsmn-vad")

    # 测试音频
    wav_file = f"{model.model_path}/example/vad_example.wav"
    res = model.generate(input=wav_file)
    print("非实时VAD检测结果：")
    print("格式说明：[[起始时间(ms), 结束时间(ms)], ...]")
    print(res)

if __name__ == "__main__":
    test_offline_vad() 