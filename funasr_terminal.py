from funasr import AutoModel
import soundfile
import os
import sys
import time

class FunASRTerminal:
    def __init__(self):
        self.models = {}
        self.initialize_models()

    def initialize_models(self):
        """初始化所有需要的模型"""
        print("正在初始化模型...")
        try:
            # 初始化非实时语音识别模型
            self.models['offline_asr'] = AutoModel(
                model="paraformer-zh",
                vad_model="fsmn-vad",
                vad_kwargs={"max_single_segment_time": 60000},
                punc_model="ct-punc"
            )
            
            # 初始化实时语音识别模型
            self.models['streaming_asr'] = AutoModel(
                model="paraformer-zh-streaming"
            )
            
            # 初始化VAD模型
            self.models['vad'] = AutoModel(
                model="fsmn-vad"
            )
            
            # 初始化标点模型
            self.models['punc'] = AutoModel(
                model="ct-punc"
            )
            
            # 初始化时间戳模型
            self.models['timestamp'] = AutoModel(
                model="fa-zh"
            )
            
            print("模型初始化完成！")
        except Exception as e:
            print(f"模型初始化失败：{str(e)}")
            sys.exit(1)

    def test_offline_asr(self):
        """非实时语音识别测试"""
        print("\n=== 非实时语音识别测试 ===")
        wav_file = f"{self.models['offline_asr'].model_path}/example/asr_example.wav"
        print(f"使用音频文件：{wav_file}")
        
        res = self.models['offline_asr'].generate(
            input=wav_file,
            batch_size_s=300,
            batch_size_threshold_s=60
        )
        print("\n识别结果：")
        print(res)

    def test_streaming_asr(self):
        """实时语音识别测试"""
        print("\n=== 实时语音识别测试 ===")
        chunk_size = [0, 10, 5]
        encoder_chunk_look_back = 4
        decoder_chunk_look_back = 1

        wav_file = os.path.join(self.models['streaming_asr'].model_path, "example/asr_example.wav")
        speech, sample_rate = soundfile.read(wav_file)
        chunk_stride = chunk_size[1] * 960

        cache = {}
        total_chunk_num = int(len((speech)-1)/chunk_stride+1)
        print(f"音频总段数：{total_chunk_num}")
        
        for i in range(total_chunk_num):
            speech_chunk = speech[i*chunk_stride:(i+1)*chunk_stride]
            is_final = i == total_chunk_num - 1
            res = self.models['streaming_asr'].generate(
                input=speech_chunk,
                cache=cache,
                is_final=is_final,
                chunk_size=chunk_size,
                encoder_chunk_look_back=encoder_chunk_look_back,
                decoder_chunk_look_back=decoder_chunk_look_back
            )
            print(f"\n第 {i+1}/{total_chunk_num} 段识别结果：")
            print(res)
            time.sleep(0.1)  # 模拟实时效果

    def test_offline_vad(self):
        """非实时VAD测试"""
        print("\n=== 非实时VAD测试 ===")
        wav_file = f"{self.models['vad'].model_path}/example/vad_example.wav"
        print(f"使用音频文件：{wav_file}")
        
        res = self.models['vad'].generate(input=wav_file)
        print("\nVAD检测结果：")
        print("格式：[[起始时间(ms), 结束时间(ms)], ...]")
        print(res)

    def test_streaming_vad(self):
        """实时VAD测试"""
        print("\n=== 实时VAD测试 ===")
        chunk_size = 200
        wav_file = f"{self.models['vad'].model_path}/example/vad_example.wav"
        speech, sample_rate = soundfile.read(wav_file)
        chunk_stride = int(chunk_size * sample_rate / 1000)

        cache = {}
        total_chunk_num = int(len((speech)-1)/chunk_stride+1)
        print(f"音频总段数：{total_chunk_num}")
        
        for i in range(total_chunk_num):
            speech_chunk = speech[i*chunk_stride:(i+1)*chunk_stride]
            is_final = i == total_chunk_num - 1
            res = self.models['vad'].generate(
                input=speech_chunk,
                cache=cache,
                is_final=is_final,
                chunk_size=chunk_size
            )
            if len(res[0]["value"]):
                print(f"\n第 {i+1}/{total_chunk_num} 段检测结果：")
                print(res)
            time.sleep(0.1)  # 模拟实时效果

    def test_punctuation(self):
        """标点恢复测试"""
        print("\n=== 标点恢复测试 ===")
        test_texts = [
            "那今天的会就到这里吧 happy new year 明年见",
            "人工智能是计算机科学的一个分支它企图了解智能的实质并生产出一种新的能以人类智能相似的方式做出反应的智能机器",
            "深度学习是机器学习的分支是一种以人工神经网络为架构对数据进行表征学习的算法"
        ]

        for i, text in enumerate(test_texts, 1):
            print(f"\n测试文本 {i}:")
            print(f"原始文本: {text}")
            res = self.models['punc'].generate(input=text)
            print(f"添加标点: {res}")

    def test_timestamp(self):
        """时间戳预测测试"""
        print("\n=== 时间戳预测测试 ===")
        wav_file = f"{self.models['timestamp'].model_path}/example/asr_example.wav"
        text_file = f"{self.models['timestamp'].model_path}/example/text.txt"
        
        print(f"音频文件: {wav_file}")
        print(f"文本文件: {text_file}")
        
        res = self.models['timestamp'].generate(
            input=(wav_file, text_file),
            data_type=("sound", "text")
        )
        print("\n预测结果：")
        print(res)

    def test_hotword_recognition(self):
        """热词识别测试"""
        print("\n=== 热词识别测试 ===")
        wav_file = f"{self.models['offline_asr'].model_path}/example/asr_example.wav"
        print(f"使用音频文件：{wav_file}")
        
        # 测试不同的热词
        hotwords = ["魔搭", "阿里巴巴", "达摩院"]
        
        for hotword in hotwords:
            print(f"\n使用热词: {hotword}")
            res = self.models['offline_asr'].generate(
                input=wav_file,
                batch_size_s=300,
                batch_size_threshold_s=60,
                hotword=hotword
            )
            print("识别结果：")
            print(res)

    def show_menu(self):
        """显示主菜单"""
        print("\n" + "="*50)
        print("FunASR 功能测试终端")
        print("="*50)
        print("1. 非实时语音识别")
        print("2. 实时语音识别")
        print("3. 非实时VAD检测")
        print("4. 实时VAD检测")
        print("5. 标点恢复")
        print("6. 时间戳预测")
        print("7. 热词识别")
        print("8. 运行所有测试")
        print("0. 退出程序")
        print("="*50)

    def run(self):
        """运行终端界面"""
        while True:
            self.show_menu()
            choice = input("\n请选择要测试的功能 (0-8): ")
            
            if choice == '0':
                print("\n感谢使用，再见！")
                break
            elif choice == '1':
                self.test_offline_asr()
            elif choice == '2':
                self.test_streaming_asr()
            elif choice == '3':
                self.test_offline_vad()
            elif choice == '4':
                self.test_streaming_vad()
            elif choice == '5':
                self.test_punctuation()
            elif choice == '6':
                self.test_timestamp()
            elif choice == '7':
                self.test_hotword_recognition()
            elif choice == '8':
                print("\n开始运行所有测试...")
                self.test_offline_asr()
                self.test_streaming_asr()
                self.test_offline_vad()
                self.test_streaming_vad()
                self.test_punctuation()
                self.test_timestamp()
                self.test_hotword_recognition()
            else:
                print("\n无效的选择，请重新输入！")
            
            input("\n按回车键继续...")

if __name__ == "__main__":
    terminal = FunASRTerminal()
    terminal.run() 