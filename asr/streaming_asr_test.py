from funasr import AutoModel
import soundfile
import os

def test_streaming_asr():
    # 配置流式识别参数
    chunk_size = [0, 10, 5]  # 600ms延迟配置
    encoder_chunk_look_back = 4
    decoder_chunk_look_back = 1

    # 创建流式识别模型
    model = AutoModel(model="paraformer-zh-streaming")

    # 读取音频文件
    wav_file = os.path.join(model.model_path, "example/asr_example.wav")
    speech, sample_rate = soundfile.read(wav_file)
    chunk_stride = chunk_size[1] * 960  # 600ms

    # 模拟流式识别
    cache = {}
    total_chunk_num = int(len((speech)-1)/chunk_stride+1)
    print("开始实时语音识别：")
    for i in range(total_chunk_num):
        speech_chunk = speech[i*chunk_stride:(i+1)*chunk_stride]
        is_final = i == total_chunk_num - 1
        res = model.generate(
            input=speech_chunk, 
            cache=cache, 
            is_final=is_final, 
            chunk_size=chunk_size, 
            encoder_chunk_look_back=encoder_chunk_look_back, 
            decoder_chunk_look_back=decoder_chunk_look_back
        )
        print(f"第 {i+1}/{total_chunk_num} 段识别结果：")
        print(res)

if __name__ == "__main__":
    test_streaming_asr() 