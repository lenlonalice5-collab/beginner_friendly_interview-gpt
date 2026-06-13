import matplotlib.pyplot as plt


def create_trend_chart(scores):

    plt.figure(
        figsize=(8,5)
    )

    plt.plot(
        range(
            1,
            len(scores)+1
        ),
        scores,
        marker="o"
    )

    plt.title(
        "Interview Score Trend"
    )

    plt.xlabel(
        "Interview"
    )

    plt.ylabel(
        "Average Score"
    )

    plt.grid()

    plt.savefig(
        "score_trend.png"
    )

    plt.close()