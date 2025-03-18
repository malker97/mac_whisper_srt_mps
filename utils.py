# Below is an srt file, please adjust the transcribed text to make the pause more nature and friendly. Also change the timestamp accordingly

import json
from datetime import datetime, timedelta
import pysrt


# chunks example:
# {
#     {'timestamp': (0.56, 5.28), 'text': 'This week OpenAI released a new version of Whisper, their audio to text model.'},
# }
def format_srt_time(seconds):
    """将秒转换为 SRT 时间格式 hh:mm:ss,SSS"""
    if seconds is None:
        return "00:00:00,000"
    millisec = int((seconds % 1) * 1000)  # 取小数部分转换为 3 位毫秒
    time_str = str(timedelta(seconds=int(seconds)))  # 取整数部分
    hours, minutes, seconds = map(int, time_str.split(':'))
    return f"{hours:02}:{minutes:02}:{seconds:02},{millisec:03d}"

def chunks_to_srt(chunks, output_file="output.srt"):
    """将 chunks 列表转换为 SRT 格式并写入文件"""
    with open(output_file, "w", encoding="utf-8") as f:
        index = 1
        for chunk in chunks:
            start_time = format_srt_time(chunk["timestamp"][0])
            end_time = format_srt_time(chunk["timestamp"][1])
            text = chunk["text"].strip()  # 去掉前后空格，避免格式问题

            # **跳过无效时间戳**
            if start_time == "00:00:00,000" or end_time == "00:00:00,000":
                continue

            # 确保时间戳有效
            if chunk["timestamp"][0] >= chunk["timestamp"][1]:
                continue  # 跳过无效的时间戳

            f.write(f"{index}\n")
            f.write(f"{start_time} --> {end_time}\n")
            f.write(f"{text}\n\n")
            index += 1

    print(f"SRT 文件已保存为 {output_file}")

# 运行转换
# chunks_to_srt(chunks, "transcript.srt")