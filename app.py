# app.py - 单词学习应用后端
def get_word_status(word):
    # 模拟从数据库获取单词状态
    return f"Word '{word}' is in 'learning' status."

print(get_word_status("apple"))