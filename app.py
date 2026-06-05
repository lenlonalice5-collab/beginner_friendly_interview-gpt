import gradio as gr
from questions import questions
from scorer import score_answer

def get_question():
    return questions[
        "AI应用开发工程师"
    ][0]["question"]

def evaluate(answer):

    question = questions[
        "AI应用开发工程师"
    ][0]["question"]

    return score_answer(
        question,
        answer
    )

with gr.Blocks() as demo:

    question_box = gr.Textbox(
        value=get_question(),
        label="面试题",
        interactive=False
    )

    answer_box = gr.Textbox(
        label="你的回答"
    )

    output_box = gr.Textbox(
        label="AI评价",
        lines=10
    )

    btn = gr.Button("提交")

    btn.click(
        evaluate,
        inputs=answer_box,
        outputs=output_box
    )

demo.launch()