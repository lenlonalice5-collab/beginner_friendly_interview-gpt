import gradio as gr
from report import (generate_report,generate_skill_report)
from scorer import score_answer
from pdf_export import export_pdf
from history import (
    save_history,
    load_history
)
from radar_chart import create_radar_chart

from report import (
    generate_statistics,
    generate_skill_scores
)
from datetime import datetime
from question_generator import generate_questions
from followup import (
    generate_followup
)
from speech import speech_to_text

followup_count = 0

selected_job = "AI应用开发工程师"

question_list = generate_questions(
    selected_job
)

current_index = 0

results = []

interview_start_time = None

is_followup = False

current_question_text = ""

current_question_text = question_list[current_index]["question"]

def get_current_question():

    global current_index

    if current_index < len(question_list):

        return question_list[
            current_index
        ]["question"]

    return "面试结束"

def get_progress():

    total = len(question_list)

    current = min(
        current_index + 1,
        total
    )

    percent = int(
        current / total * 100
    )

    return (
        f"第 {current} 题 / 共 {total} 题"
        f"\n完成度：{percent}%"
    )

def quick_check(answer):

    if len(answer.strip()) < 20:

        return True

    return False

def submit_answer(answer):

    global current_index
    global results
    global interview_start_time
    global is_followup

    if is_followup:

        is_followup = False

        followup_count = 0

        current_index += 1

    else:

        pass

    if interview_start_time is None:
        interview_start_time = datetime.now()

    if current_index >= len(question_list):

        return (
            "面试结束",
            "已经没有题目了",
             get_progress()
             )
                  

    question = question_list[
        current_index
    ]["question"]

    score, feedback = score_answer(
        question,
        answer
    )

    followup = generate_followup(
    question,
    answer
    )

    if "NO_FOLLOWUP" not in followup:

        if followup_count < 1:

            followup_count += 1

            is_followup = True

            return (
                followup,
                feedback,
                get_progress()
            )

    if quick_check(answer):

        return (
        current_question_text,
        "回答过短，请补充更多细节。"
        )

    results.append(
    {
        "job": selected_job,
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
        save_history(results)

    return (
        next_question,
        feedback,
        get_progress()
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

def get_interview_duration():

    global interview_start_time

    if interview_start_time is None:
        return "0分钟"

    end_time = datetime.now()

    duration = end_time - interview_start_time

    minutes = round(
        duration.total_seconds() / 60,
        2
    )

    return f"{minutes}分钟"

def create_pdf():

    report = create_ai_report()

    stats = generate_statistics(
        results
    )

    duration = get_interview_duration()

    skill_scores = generate_skill_scores(
        results
    )

    create_radar_chart(
        skill_scores
    )

    export_pdf(
        report,
        stats,
        duration,
        selected_job
    )

    return "PDF已生成"

def switch_job(job):

    global selected_job
    global question_list
    global current_index
    global results

    selected_job = job

    question_list = generate_questions(job)

    current_index = 0

    results = []

    return (
    question_list[0]["question"],
    get_progress()
)

def regenerate_questions():

    global question_list
    global current_index

    question_list = generate_questions(
        selected_job
    )

    current_index = 0

    return (
    question_list[0]["question"],
    get_progress()
    )

def skip_question():

    global current_index

    current_index += 1

    if current_index >= len(question_list):

        return (
            "面试结束",
            get_progress()
        )

    return (
        question_list[current_index]["question"],
        get_progress()
    )

def convert_voice(audio_file):

    if audio_file is None:

        return ""

    return speech_to_text(
        audio_file
    )

with gr.Blocks() as demo:

    gr.Markdown(
        "# InterviewGPT V6.3"
    )

    job_input = gr.Textbox(
        value="AI应用开发工程师",
        label="岗位名称",
        placeholder="例如：Python开发工程师"
    )

    audio_input = gr.Audio(
        sources=["microphone"],
        type="filepath",
        label="语音回答"
    )

    progress_box = gr.Textbox(
        value=get_progress(),
        label="面试进度"
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

    voice_btn = gr.Button(
        "语音转文字"
    )

    submit_btn = gr.Button(
        "提交答案"
    )

    skip_btn = gr.Button(
        "跳过本题"
    )

    load_job_btn = gr.Button(
        "生成面试题"
    )

    regenerate_btn = gr.Button(
        "重新生成题目"
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

    pdf_btn = gr.Button(
        "导出PDF报告"
    )

    history_btn = gr.Button(
        "查看历史记录"
    )

    stats_btn = gr.Button(
        "查看详细统计"
    )

    history_box = gr.Textbox(
        label="历史记录",
        lines=15
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

    pdf_status = gr.Textbox(
        label="PDF状态"
    )

    statistics_box = gr.Textbox(
        label="面试统计"
    )

    voice_btn.click(
        convert_voice,
        inputs=audio_input,
        outputs=answer_box
    )

    submit_btn.click(
        submit_answer,
        inputs=answer_box,
        outputs=[
            question_box,
            feedback_box,
            progress_box
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

    pdf_btn.click(
        create_pdf,
        outputs=pdf_status
    )

    history_btn.click(
        load_history,
        outputs=history_box
    )

    stats_btn.click(
        lambda: generate_statistics(results),
        outputs=statistics_box
    )

    regenerate_btn.click(
    regenerate_questions,
    outputs=[
        question_box,
        progress_box
    ]
)

    load_job_btn.click(
        switch_job,
        inputs=job_input,
        outputs=[
            question_box,
            progress_box
        ]
    )

    skip_btn.click(
        skip_question,
        outputs=[
            question_box,
            progress_box
        ]
    )

    job_input.submit(
        switch_job,
        inputs=job_input,
        outputs=question_box
    )



demo.launch()