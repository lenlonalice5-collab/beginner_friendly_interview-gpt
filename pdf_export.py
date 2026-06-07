from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def export_pdf(report_text):

    pdf = SimpleDocTemplate(
        "Interview_Report.pdf"
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "InterviewGPT Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(
            1,
            20
        )
    )

    content.append(
        Paragraph(
            report_text,
            styles["BodyText"]
        )
    )

    pdf.build(content)

    return "Interview_Report.pdf"