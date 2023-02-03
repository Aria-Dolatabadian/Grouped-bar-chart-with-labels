import matplotlib
import matplotlib.pyplot as plt
import numpy as np
labels = ['Chr1', 'Chr2', 'Chr3', 'Chr4', 'Chr5']
RLK_means = [20, 34, 30, 35, 27]
RLP_means = [25, 32, 34, 20, 25]
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, RLK_means, width, label='RLK')
rects2 = ax.bar(x + width/2, RLP_means, width, label='RLP')
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number')
ax.set_title('RLK and RLP across the chromosomes')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
autolabel(rects1)
autolabel(rects2)
fig.tight_layout()
plt.show()
