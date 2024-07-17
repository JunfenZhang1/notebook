from sympy import symbols, limit

# 定义符号
x, y, h = symbols('x y h')

# 定义函数f(x, y)
def f(x, y):
    return x**2 * y / (x**4 + y**2) if (x, y) != (0, 0) else 0

# 计算偏导数
df_dx_00 = limit((f(h, 0) - f(0, 0)) / h, h, 0)
df_dy_00 = limit((f(0, h) - f(0, 0)) / h, h, 0)

(df_dx_00, df_dy_00)