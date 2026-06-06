import gradio as gr
from report import (generate_report,generate_skill_report)
from questions import questions
from scorer import score_answer
question_list = questions[
    "AI应用开发工程师"
]

current_index = 0

results = []
def get_current_question():

    global current_index

    if current_index < len(question_list):

        return question_list[
            current_index
        ]["question"]

    return "面试结束"
def submit_answer(answer):

    global current_index
    global results

    if current_index >= len(question_list):

        return (
            "面试结束",
            "已经没有题目了"
        )

    question = question_list[
        current_index
    ]["question"]

    score, feedback = score_answer(
        question,
        answer
    )

    results.append(
    {
        "skill": question_list[current_index]["skill"],
        "question": question,
        "answer": answer,
        "score": score
    }
    )

    current_index += 1

    if current_index < len(question_list):

        next_question = question_list[
            current_index
        ]["question"]

    else:

        next_question = "面试结束"

    return (
        next_question,
        feedback
    )
def create_ai_report():

    global results

    if len(results) == 0:
        return "暂无面试记录"

    return generate_report(results)
def create_skill_report():

    global results

    if len(results) == 0:
        return "暂无成绩"

    return generate_skill_report(results)
def show_result():

    if len(results) == 0:

        return "暂无成绩"

    total = sum(
        r["score"]
        for r in results
    )

    avg = total / len(results)

    report = f"""
    已完成题目数：{len(results)}

    平均分：{avg:.1f}
    """

    return report
with gr.Blocks() as demo:

    gr.Markdown(
        "# InterviewGPT V2"
    )

    question_box = gr.Textbox(
        value=get_current_question(),
        label="当前题目"
    )

    answer_box = gr.Textbox(
        label="你的回答",
        lines=5
    )

    feedback_box = gr.Textbox(
        label="AI评价",
        lines=10
    )

    submit_btn = gr.Button(
        "提交答案"
    )

    report_btn = gr.Button(
        "查看成绩"
    )
    ai_report_btn = gr.Button(
    "生成面试报告"
    )

    skill_btn = gr.Button(
    "能力画像"
    )
    ai_report_box = gr.Textbox(
    label="AI面试报告",
    lines=15
    )

    skill_box = gr.Textbox(
    label="能力画像",
    lines=10
    )

    report_box = gr.Textbox(
        label="成绩统计"
    )

    submit_btn.click(
        submit_answer,
        inputs=answer_box,
        outputs=[
            question_box,
            feedback_box
        ]
    )

    report_btn.click(
        show_result,
        outputs=report_box
    )
    ai_report_btn.click(
        create_ai_report,
        outputs=ai_report_box
    )
    skill_btn.click(
        create_skill_report,
        outputs=skill_box
    )





demo.launch()