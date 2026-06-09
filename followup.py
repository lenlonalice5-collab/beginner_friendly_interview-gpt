from ollama import chat


def generate_followup(
    question,
    answer
):

    prompt = f"""
你是一位资深技术面试官。

原问题：

{question}

候选人回答：

{answer}

请判断：

1. 回答优秀
2. 回答一般
3. 回答较差

如果需要继续追问：

直接输出追问问题。

如果不需要追问：

输出：

NO_FOLLOWUP
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

    return response["message"]["content"]