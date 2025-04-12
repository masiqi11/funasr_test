from funasr import AutoModel
import os

def test_offline_asr():
    # 创建模型（包含 VAD、标点和说话人识别功能）
    model = AutoModel(
        model="paraformer-zh",  
        vad_model="fsmn-vad", 
        vad_kwargs={"max_single_segment_time": 60000},
        punc_model="ct-punc"
    )

    # 测试音频文件
    wav_file = f"{model.model_path}/example/asr_example.wav"

    # 添加热词功能的识别
    res = model.generate(
        input=wav_file, 
        batch_size_s=300, 
        batch_size_threshold_s=60, 
        hotword='魔搭'  # 添加热词
    )
    print("非实时语音识别结果：")
    print(res)

if __name__ == "__main__":
    test_offline_asr() 