import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans', 'Arial Unicode MS', 'Microsoft YaHei']  # 优先使用SimHei
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 设置画布
fig, ax = plt.subplots(figsize=(10, 6))

# 节点位置
nodes = {
    "Query (Q)": (0, 0),
    "Encoder (可微)": (2, 1.5),
    "Retriever (检索)": (4, 1.5),
    "Docs": (6, 1.5),
    "Generator (生成器)": (4, -1.5),
    "Answer": (6, -1.5),
    "Subquery (子查询, 不可微)": (2, -1.5)
}

# 画节点
for node, (x, y) in nodes.items():
    ax.scatter(x, y, s=1000, color="lightblue" if "不可微" not in node else "salmon", zorder=3)
    ax.text(x, y, node, ha="center", va="center", fontsize=10, wrap=True)

# 连线
def draw_arrow(start, end, text="", style="-", color="black"):
    ax.annotate(
        "", xy=end, xycoords="data", xytext=start, textcoords="data",
        arrowprops=dict(arrowstyle="->", color=color, lw=2, linestyle=style)
    )
    if text:
        mx, my = (start[0]+end[0])/2, (start[1]+end[1])/2
        ax.text(mx, my+0.2, text, ha="center", fontsize=9, color=color)

# 连续可微路径（蓝色）
draw_arrow(nodes["Query (Q)"], nodes["Encoder (可微)"], "Embedding", color="blue")
draw_arrow(nodes["Encoder (可微)"], nodes["Retriever (检索)"], "可微梯度", color="blue")
draw_arrow(nodes["Retriever (检索)"], nodes["Docs"], "Top-k", color="blue")
draw_arrow(nodes["Docs"], nodes["Generator (生成器)"], "拼接输入", color="blue")
draw_arrow(nodes["Generator (生成器)"], nodes["Answer"], "生成答案", color="blue")

# 不可微路径（红色，子查询）
draw_arrow(nodes["Query (Q)"], nodes["Subquery (子查询, 不可微)"], "离散采样", color="red", style="--")
draw_arrow(nodes["Subquery (子查询, 不可微)"], nodes["Retriever (检索)"], "检索子查询", color="red", style="--")

# 图例
blue_patch = mpatches.Patch(color='lightblue', label='可微节点 (梯度能传递)')
red_patch = mpatches.Patch(color='salmon', label='不可微节点 (梯度断开)')
ax.legend(handles=[blue_patch, red_patch], loc="lower right")

ax.set_xlim(-1, 7)
ax.set_ylim(-3, 3)
ax.axis("off")
plt.title("RAG 中的梯度流动：哪些地方可微，哪些地方不可微", fontsize=14)

# 保存文件
output_path = "rag_gradient_flow.png"
plt.savefig(output_path, dpi=300, bbox_inches="tight")
plt.close()

print(f"图片已保存到: {output_path}")