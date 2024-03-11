import random
import time

languages = {
    'mandarin': [
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
    ],
    'spanish': [
        {"spanish": "Hola", "english": "Hello"},
        {"spanish": "Adiós", "english": "Goodbye"},
        {"spanish": "Por favor", "english": "Please"},
        {"spanish": "Gracias", "english": "Thank you"},
        {"spanish": "Lo siento", "english": "I'm sorry"},
        {"spanish": "Sí", "english": "Yes"},
        {"spanish": "No", "english": "No"},
        {"spanish": "¿Cómo estás?", "english": "How are you?"},
        {"spanish": "Estoy bien", "english": "I am fine"},
        {"spanish": "Mucho gusto", "english": "Nice to meet you"},
        {"spanish": "¿Cómo te llamas?", "english": "What is your name?"},
        {"spanish": "Me llamo___", "english": "My name is___"},
        {"spanish": "¿Cuántos años tienes?", "english": "How old are you?"},
        {"spanish": "Tengo ___ años", "english": "I am ___ years old"},
        {"spanish": "¿Dónde vives?", "english": "Where do you live?"},
        {"spanish": "Vivo en ___", "english": "I live in ___"},
        {"spanish": "¿Qué haces?", "english": "What are you doing?"},
        {"spanish": "Trabajo", "english": "I am working"},
        {"spanish": "Me gusta", "english": "I like it"},
        {"spanish": "No me gusta", "english": "I don't like it"},
        {"spanish": "Entiendo", "english": "I understand"},
        {"spanish": "No entiendo", "english": "I don't understand"},
        {"spanish": "¿Qué dijiste?", "english": "What did you say?"},
        {"spanish": "¿Qué pasa?", "english": "What's happening?"},
        {"spanish": "Buenos días", "english": "Good morning"},
        {"spanish": "Buenas tardes", "english": "Good afternoon"},
        {"spanish": "Buenas noches", "english": "Good evening/night"},
        {"spanish": "Hasta luego", "english": "See you later"},
        {"spanish": "¿Cuánto cuesta?", "english": "How much does it cost?"},
        {"spanish": "Ayúdame, por favor", "english": "Help me, please"},
    ],
    
    'french': [
        {"french": "Bonjour", "english": "Hello"},
        {"french": "Au revoir", "english": "Goodbye"},
        {"french": "S'il vous plaît", "english": "Please"},
        {"french": "Merci", "english": "Thank you"},
        {"french": "Excusez-moi", "english": "Excuse me/I'm sorry"},
        {"french": "Oui", "english": "Yes"},
        {"french": "Non", "english": "No"},
        {"french": "Comment ça va?", "english": "How are you?"},
        {"french": "Ça va bien", "english": "I am well"},
        {"french": "Enchanté(e)", "english": "Nice to meet you"},
        {"french": "Comment tu t'appelles?", "english": "What is your name?"},
        {"french": "Je m'appelle___", "english": "My name is___"},
        {"french": "Quel âge as-tu?", "english": "How old are you?"},
        {"french": "J'ai ___ ans", "english": "I am ___ years old"},
        {"french": "Où habites-tu?", "english": "Where do you live?"},
        {"french": "J'habite à___", "english": "I live in ___"},
        {"french": "Que fais-tu?", "english": "What are you doing?"},
        {"french": "Je travaille", "english": "I am working"},
        {"french": "J'aime ça", "english": "I like it"},
        {"french": "Je n'aime pas ça", "english": "I don't like it"},
        {"french": "Je comprends", "english": "I understand"},
        {"french": "Je ne comprends pas", "english": "I don't understand"},
        {"french": "Qu'est-ce que tu as dit?", "english": "What did you say?"},
        {"french": "Qu'est-ce qui se passe?", "english": "What's happening?"},
        {"french": "Bonjour (le matin)", "english": "Good morning"},
        {"french": "Bon après-midi", "english": "Good afternoon"},
        {"french": "Bonne soirée", "english": "Good evening"},
        {"french": "À bientôt", "english": "See you soon"},
        {"french": "Combien ça coûte?", "english": "How much does it cost?"},
        {"french": "Aidez-moi, s'il vous plaît", "english": "Help me, please"},
    ],
}

def quiz_user(phrases, num_questions=10):
    random.shuffle(phrases)
    score = 0

    for i in range(min(num_questions, len(phrases))):
        phrase = phrases[i]
        language_key = list(phrase.keys())[0]
        translation_key = 'english' if language_key != 'english' else None
        start_time = time.time()

        print(f"\nQuestion {i + 1}: What is the English translation of '{phrase[language_key]}' in {language_key.capitalize()}?")
        user_answer = input("Your answer: ").strip().lower()
        end_time = time.time()
        response_time = round(end_time - start_time, 2)

        correct_answer = phrase[translation_key].lower() if translation_key else None

        if user_answer == correct_answer:
            print(f"Correct! You answered in {response_time} seconds.")
            score += 1
        else:
            print(f"You're wrong! The answer is '{correct_answer}'.")

    print(f"\nQuiz complete! Your score: {score}/{min(num_questions, len(phrases))}")
    if score >= min(num_questions, len(phrases)) * 0.8:
        print("Great job! You are doing well.")
    else:
        print("Keep practicing to improve your score.")

def main():
    print("Welcome to Bootleg Duolingo - The Duo with the better booty:>")
    
    # Language selection
    print("\nChoose a language:")
    for i, lang in enumerate(languages.keys(), 1):
        print(f"{i}. {lang.capitalize()}")
    
    language_choice = int(input("Enter the number of your chosen language: "))
    
    if 1 <= language_choice <= len(languages):
        selected_language = list(languages.keys())[language_choice - 1]
        print(f"\nYou have selected {selected_language.capitalize()}.\n")
        quiz_user(languages[selected_language], num_questions=15)
    else:
        print("Invalid language choice. Exiting.")

if __name__ == "__main__":
    main()
