import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
    
pic = [1.0,1.0,1.0,1.0,1.0]
plt.barh(range(5), pic, height=0.7, color='green', alpha=0.8)
plt.yticks(range(5), ['测试集1', '测试集2', '测试集3', '测试集4', '测试集5'])

plt.xlim(0.0,1.5)
plt.xlabel("覆盖率")
plt.title("各测试集覆盖率比对")
for x, y in enumerate(pic):
    plt.text(y + 0.2, x - 0.1, '%s' % y)
plt.show()
