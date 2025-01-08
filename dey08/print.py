# 提示用户输入幸运数字并保存输入
lucky_number = input("请输入你的幸运数字: ")

# 定义两个变量
a, b = 0, 1

# 导入 random 模块
import random

# 标记是否找到了幸运数字
found_lucky_number = False

while b < 100:
    print(b, end=' ')
    a, b = b, a + b

    # 随机保留一条输出
    random_number = random.randint(1, 100)
    if random_number == 50:  # 修改为一个合理的条件，例如 50
        print("\n你的幸运数字是:", random_number)
        found_lucky_number = True
        break

# 如果没有找到幸运数字，输出失败消息
if not found_lucky_number:
    print("\n很遗憾，这次没有选中你的幸运数字。")
