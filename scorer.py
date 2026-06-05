from ollama import chat

def score_answer(question, answer):

    prompt = f"""
你是AI面试官。

问题：
{question}

候选人回答：
{answer}

请输出：

评分（0-10）
优点
缺点
"""

    response = chat(
        model="qwen3:8b",
        messages=[
            {"role":"user","content":prompt}
        ]
    )

    return response["message"]["content"]