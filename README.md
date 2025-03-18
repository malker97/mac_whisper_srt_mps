# mac_whisper_mps

**mac_whisper_mps** 是一个专为 macOS 设计的工具，它允许 OpenAI / Hugging Face 蒸馏版 Whisper 在 Mac 上调用 MPS（Metal Performance Shaders）GPU 进行加速，从而大幅提高视频转文字（Speech-to-Text, STT）的处理速度。

## ✨ 主要功能
- **MPS GPU 加速**：利用 Apple Metal Performance Shaders (MPS) 提升 Whisper 模型的推理速度，相比纯 CPU 推理更快更高效。
- **多格式支持**：支持处理多种视频/音频格式，如 MP4、MOV、MP3、WAV 等。
- **SRT 字幕文件导出**：自动将转录的文本保存为 `.srt` 格式，方便直接用于视频字幕。
- **高兼容性**：兼容 MacBook、Mac Studio、Mac mini 等 M1/M2/M3/M4 系列芯片设备，充分发挥 Apple Silicon 的计算能力。

## 🚀 快速开始

### 1️⃣ 安装依赖
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### 2️⃣ 运行示例
#### 2.1 运行路径配置
```python
# Example usage
directory_path = "./"
pipe = load_model()
process_audio_files(directory_path, pipe)

```
当前代码默认会把当前路径下的mp4文件转换为srt文件，可以根据需要修改代码中 `directory_path = "./"`。
#### 2.2 运行模型选择
当前代码中默认配置的是 Hugging Face 的 `distil-whisper/distil-large-v3` 模型，该模型仅支持英文语音转文字。如果需要转换其他语言，可以在 `run.py` 中修改模型配置，如果多语种模型，可以考虑使用openai/whisper-large-v3。
```python
def load_model():
    device = "mps:0"
    torch_dtype = torch.float16  # if torch.cuda.is_available() else torch.float32
    model_id = "distil-whisper/distil-large-v3"
```
#### 2.3 运行
```bash
python run.py
```
