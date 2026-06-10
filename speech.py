import whisper

model = whisper.load_model("small")


def speech_to_text(audio_file):

    if audio_file is None:

        return "请先录音"

    try:

        result = model.transcribe(
            audio_file,
            language="zh",
            fp16=False
        )

        return result["text"]

    except Exception as e:

        return f"识别失败：{e}"