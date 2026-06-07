import matplotlib.pyplot as plt
import numpy as np


def create_radar_chart(skill_scores):

    labels = list(skill_scores.keys())

    values = list(skill_scores.values())

    values += values[:1]

    angles = np.linspace(
        0,
        2*np.pi,
        len(labels),
        endpoint=False
    ).tolist()

    angles += angles[:1]

    fig, ax = plt.subplots(
        figsize=(6, 6),
        subplot_kw=dict(polar=True)
    )

    ax.plot(
        angles,
        values,
        linewidth=2
    )

    ax.fill(
        angles,
        values,
        alpha=0.25
    )

    ax.set_xticks(angles[:-1])

    ax.set_xticklabels(labels)

    ax.set_ylim(0, 10)

    plt.savefig(
        "radar_chart.png"
    )

    plt.close()

    return "radar_chart.png"