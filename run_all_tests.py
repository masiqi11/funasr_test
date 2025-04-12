import os
import sys

# 添加当前目录到系统路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from asr.offline_asr_test import test_offline_asr
from asr.streaming_asr_test import test_streaming_asr
from vad.offline_vad_test import test_offline_vad
from vad.streaming_vad_test import test_streaming_vad
from punc.punctuation_test import test_punctuation
from timestamp.timestamp_test import test_timestamp

def run_all_tests():
    print("="*50)
    print("开始运行 FunASR 功能测试")
    print("="*50)

    # 1. 非实时语音识别测试
    print("\n1. 非实时语音识别测试")
    print("-"*30)
    test_offline_asr()

    # 2. 实时语音识别测试
    print("\n2. 实时语音识别测试")
    print("-"*30)
    test_streaming_asr()

    # 3. 非实时VAD测试
    print("\n3. 非实时VAD测试")
    print("-"*30)
    test_offline_vad()

    # 4. 实时VAD测试
    print("\n4. 实时VAD测试")
    print("-"*30)
    test_streaming_vad()

    # 5. 标点恢复测试
    print("\n5. 标点恢复测试")
    print("-"*30)
    test_punctuation()

    # 6. 时间戳预测测试
    print("\n6. 时间戳预测测试")
    print("-"*30)
    test_timestamp()

    print("\n"+"="*50)
    print("所有测试完成")
    print("="*50)

if __name__ == "__main__":
    run_all_tests() 