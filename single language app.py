import random
import time

mandarin_phrases = [
    {"chinese": "你好", "english": "Hello"},
    {"chinese": "谢谢", "english": "Thank you"},
    {"chinese": "对不起", "english": "Sorry"},
    {"chinese": "请", "english": "Please"},
    {"chinese": "是的", "english": "Yes"},
    {"chinese": "不是", "english": "No"},
    {"chinese": "再见", "english": "Goodbye"},
    {"chinese": "你叫什么名字？", "english": "What is your name?"},
    {"chinese": "我叫___", "english": "My name is ___"},
    {"chinese": "多少钱？", "english": "How much does it cost?"},
    {"chinese": "请帮我", "english": "Please help me"},
    {"chinese": "我不懂", "english": "I don't understand"},
    {"chinese": "可以吗？", "english": "Is it okay?"},
    {"chinese": "我喜欢", "english": "I like"},
    {"chinese": "我不喜欢", "english": "I don't like"},
    {"chinese": "很好", "english": "Very good"},
    {"chinese": "不错", "english": "Not bad"},
    {"chinese": "对不对？", "english": "Is it correct?"},
    {"chinese": "有问题吗？", "english": "Any problems?"},
    {"chinese": "我明白了", "english": "I understand"},
    {"chinese": "不明白", "english": "I don't understand"},
    {"chinese": "请再说一遍", "english": "Please say it again"},
    {"chinese": "在哪里？", "english": "Where is it?"},
    {"chinese": "什么时候？", "english": "When?"},
    {"chinese": "为什么？", "english": "Why?"},
    {"chinese": "怎么样？", "english": "How is it?"},
    {"chinese": "我想吃__", "english": "I want to eat __"},
    {"chinese": "我需要帮助", "english": "I need help"},
    {"chinese": "我会说一点儿中文", "english": "I can speak a little Chinese"},
    {"chinese": "谢谢你的帮助", "english": "Thank you for your help"},
]
def quiz_user(mandarin_phrases, num_questions=15):
    random.shuffle(mandarin_phrases)
    score = 0

    for i in range(min(num_questions, len(mandarin_phrases))):
        phrase = mandarin_phrases[i]
        start_time = time.time()
        print(f"\nQuestion {i + 1}: What is the English translation of '{phrase['chinese']}'?")
        user_answer = input("Your answer: ").strip().lower()
        end_time = time.time()
        response_time = round(end_time - start_time, 2)

        correct_answer = phrase['english'].lower()

        if user_answer == correct_answer:
            print(f"Correct! You answered in {response_time} seconds.")
            score += 1
        else:
            print(f"You're wrong! The answer is '{phrase['english']}'.")

    print(f"\nQuiz complete! Your score: {score}/{min(num_questions, len(mandarin_phrases))}")
    if score >= min(num_questions, len(mandarin_phrases)) * 0.8:
        print("Great job! You are doing well.")
    else:
        print("Keep practicing to improve your score.")

def main():
    print("Welcome to Bootleg Duolingo - The Duo with the better booty:>")
    input("Press enter to begin!")
    quiz_user(mandarin_phrases, num_questions=15)

if __name__ == "__main__":
    main()
