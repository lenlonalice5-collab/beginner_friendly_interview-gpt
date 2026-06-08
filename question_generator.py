from ollama import chat
from json_repair import repair_json
import json


def generate_questions(job_name):

    prompt = f"""
请为{job_name}生成5道面试题。

返回JSON数组：

[
    {{
        "skill":"技能",
        "question":"问题"
    }}
]
"""

    response = chat(
        model="qwen3:8b",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    text = response["message"]["content"]

    repaired = repair_json(text)

    return json.loads(repaired)