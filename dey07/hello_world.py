# 对世界说你好

# 提示用户输入他们的名字，并将输入存储在变量 user_name 中
user_name = input("请输入你的名字：")

# 使用字符串格式化输出问候语
print("Hello World! helo %s" % user_name)

# 使用 f-string 输出问候语
print(f"你好！{user_name}。")

# 输出多行文本
print("梦开始的地方。\n这是换行的地方。")

# 定义一个函数来打印问候语，增加前缀和颜色参数
def print_greeting(prefix, greeting, message, color):
    # ANSI 转义码重置颜色
    reset_color = "\033[0m"
    print(f"{color}{prefix} {greeting} {message}{reset_color}")

# 执行另一个打印函数，设置前缀和颜色
greeting_message = "你好"
target_message = "世界"
print_greeting("前缀:", greeting_message, target_message, "\033[32m")  # 绿色