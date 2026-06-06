from ollama import chat

def generate_report(results):

    prompt = f"""
你是一名资深AI技术面试官。

以下是候选人的面试记录：

{results}

请输出：

【总体评价】

【优势分析】

【不足分析】

【学习建议】

【录用建议】

控制在300字以内。
"""

    response = chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
def generate_skill_report(results):

    report = ""

    for item in results:

        report += (
            f"{item['skill']}: "
            f"{item['score']}/10\n"
        )

    return report