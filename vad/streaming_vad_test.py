from funasr import AutoModel
import soundfile
import os

def test_streaming_vad():
    # 配置参数
    chunk_size = 200  # ms
    model = AutoModel(model="fsmn-vad")

    # 读取音频
    wav_file = f"{model.model_path}/example/vad_example.wav"
    speech, sample_rate = soundfile.read(wav_file)
    chunk_stride = int(chunk_size * sample_rate / 1000)

    # 模拟实时处理
    cache = {}
    total_chunk_num = int(len((speech)-1)/chunk_stride+1)
    print("开始实时VAD检测：")
    print("输出说明：")
    print("- [[beg1, end1], ...] 表示检测到完整语音片段")
    print("- [[beg, -1]] 表示只检测到起始点")
    print("- [[-1, end]] 表示只检测到结束点")
    print("- [] 表示未检测到语音")
    
    for i in range(total_chunk_num):
        speech_chunk = speech[i*chunk_stride:(i+1)*chunk_stride]
        is_final = i == total_chunk_num - 1
        res = model.generate(
            input=speech_chunk, 
            cache=cache, 
            is_final=is_final, 
            chunk_size=chunk_size
        )
        if len(res[0]["value"]):
            print(f"第 {i+1}/{total_chunk_num} 段检测结果：")
            print(res)

if __name__ == "__main__":
    test_streaming_vad() 