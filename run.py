import torch
import os
import datetime
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from utils import chunks_to_srt
import json

chunks = []
def load_model():
    device = "mps:0"
    torch_dtype = torch.float16  # if torch.cuda.is_available() else torch.float32
    model_id = "distil-whisper/distil-large-v3"

    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
    )
    model.to(device)

    processor = AutoProcessor.from_pretrained(model_id)
    pipe = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        torch_dtype=torch_dtype,
        device=device,
        chunk_length_s=25,
        return_timestamps=True,

    )
    
    return pipe

def process_audio_files(directory, pipe):
    
    
    # Process each MP4 file in the directory
    for file_name in os.listdir(directory):
        if file_name.endswith(".mp4"):
            start_time = datetime.datetime.now()
            file_path = os.path.join(directory, file_name)
            output_srt_path = os.path.splitext(file_path)[0] + ".srt"
            
            print(f"Processing: {file_name}")
            result = pipe(file_path)
            chunks_to_srt(result["chunks"], output_srt_path)
            chunks.append(result['chunks'])
            print(f"Saved SRT to: {output_srt_path}")

            end_time = datetime.datetime.now()
            print(f"Total time taken: {end_time - start_time}")

# Example usage
directory_path = "./"
pipe = load_model()
process_audio_files(directory_path, pipe)
