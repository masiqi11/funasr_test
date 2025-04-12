# README (English)

# FunASR Test Suite

This repository contains a collection of test scripts for the FunASR project. The tests are organized into different modules, each focusing on a specific functionality of the FunASR system.

## Project Structure

```
funasr_terminal.py
run_all_tests.py
asr/
    offline_asr_test.py
    streaming_asr_test.py
punc/
    punctuation_test.py
timestamp/
    timestamp_test.py
vad/
    offline_vad_test.py
    streaming_vad_test.py
```

### Modules

- **ASR (Automatic Speech Recognition)**:
  - `offline_asr_test.py`: Tests for offline ASR functionality.
  - `streaming_asr_test.py`: Tests for streaming ASR functionality.

- **Punctuation**:
  - `punctuation_test.py`: Tests for punctuation restoration.

- **Timestamp**:
  - `timestamp_test.py`: Tests for timestamp generation.

- **VAD (Voice Activity Detection)**:
  - `offline_vad_test.py`: Tests for offline VAD functionality.
  - `streaming_vad_test.py`: Tests for streaming VAD functionality.

## How to Run Tests

1. **Run all tests**:
   Use the `run_all_tests.py` script to execute all test cases in the repository:
   ```bash
   python run_all_tests.py
   ```

2. **Run individual tests**:
   Navigate to the specific module folder and execute the desired test script:
   ```bash
   python <test_script_name>.py
   ```

## Requirements

- Python 3.9 or higher
- Required dependencies (install via `pip`):
  ```bash
  pip install -r requirements.txt
  ```

---

# README (中文)

# FunASR 测试套件

此仓库包含 FunASR 项目的测试脚本集合。测试脚本按模块组织，每个模块专注于 FunASR 系统的特定功能。

## 项目结构

```
funasr_terminal.py
run_all_tests.py
asr/
    offline_asr_test.py
    streaming_asr_test.py
punc/
    punctuation_test.py
timestamp/
    timestamp_test.py
vad/
    offline_vad_test.py
    streaming_vad_test.py
```

### 模块说明

- **ASR（自动语音识别）**:
  - `offline_asr_test.py`: 离线 ASR 功能测试。
  - `streaming_asr_test.py`: 流式 ASR 功能测试。

- **标点恢复**:
  - `punctuation_test.py`: 标点恢复功能测试。

- **时间戳**:
  - `timestamp_test.py`: 时间戳生成功能测试。

- **VAD（语音活动检测）**:
  - `offline_vad_test.py`: 离线 VAD 功能测试。
  - `streaming_vad_test.py`: 流式 VAD 功能测试。

## 如何运行测试

1. **运行所有测试**:
   使用 `run_all_tests.py` 脚本运行仓库中的所有测试用例：
   ```bash
   python run_all_tests.py
   ```

2. **运行单个测试**:
   进入特定模块文件夹并执行所需的测试脚本：
   ```bash
   python <test_script_name>.py
   ```

## 环境要求

- Python 3.9 或更高版本
- 所需依赖（通过 `pip` 安装）：
  ```bash
  pip install -r requirements.txt
  ```