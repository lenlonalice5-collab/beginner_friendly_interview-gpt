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

def generate_statistics(results):

    scores = [
        item["score"]
        for item in results
    ]

    avg_score = round(
        sum(scores)/len(scores),
        2
    )

    highest = max(scores)

    lowest = min(scores)

    return (
        f"平均分：{avg_score}\n"
        f"最高分：{highest}\n"
        f"最低分：{lowest}"
    )

def generate_skill_scores(results):

    skill_scores = {}

    for item in results:

        skill = item["skill"]

        score = item["score"]

        skill_scores[skill] = score

    return skill_scores