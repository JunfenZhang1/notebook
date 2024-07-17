import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建t向量
t = np.arange(-1, 1.01, 0.01)

# 使用meshgrid创建x和y矩阵
x, y = np.meshgrid(t, t)

# 计算z值
z = (x**2 * y) / (x**4 + y**2)

# 创建3D图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 使用surf函数的等价物 - plot_surface
surf = ax.plot_surface(x, y, z)

# 添加坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 设置标题
ax.set_title('3D Surface Plot')

# 显示图形
plt.show()