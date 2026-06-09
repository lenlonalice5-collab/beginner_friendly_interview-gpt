import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

# 设置中文字体和负号显示
rcParams['font.sans-serif'] = ['SimHei']  # 黑体
rcParams['axes.unicode_minus'] = False    # 解决负号显示

def create_radar_chart(skill_scores):
    labels = list(skill_scores.keys())
    values = list(skill_scores.values())
    values += values[:1]  # 闭合雷达图

    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    # 绘制雷达图
    ax.plot(angles, values, linewidth=2)
    ax.fill(angles, values, alpha=0.25)

    # 设置标签
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)  # 已设置全局中文字体

    ax.set_ylim(0, 10)

    plt.savefig("radar_chart.png")
    plt.close()

    return "radar_chart.png"