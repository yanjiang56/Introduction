import random

# 一些搞笑格言的列表
funny_quotes = [
    "人生苦短，代码来凑。",
    "你今天的bug，就是明天的知识。",
    "保持冷静并继续编程。",
    "吃饭睡觉打代码。",
    "Debug到天亮，终于找到一个逗号。",
    "敲代码如喝咖啡，越苦越上瘾。",
    "世界那么大，代码却总是运行不起来。",
    "生活是调试的过程，错误总在最后一行。"
]

# 随机生成搞笑格言
def generate_funny_quote():
    return random.choice(funny_quotes)

# 主程序
if __name__ == "__main__":
    print("随机搞笑格言生成器：")
    print("今天你的格言是：")
    print(generate_funny_quote())