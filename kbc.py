import random

gk_questions = (
    {
        "question": "What is the capital of France?",
        "options": ["A) Paris", "B) London", "C) Rome", "D) Berlin"],
        "answer": "A",
        "amoumt": 1000,
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": [
            "A) Charles Dickens",
            "B) William Shakespeare",
            "C) Mark Twain",
            "D) Jane Austen",
        ],
        "answer": "B",
        "amoumt": 1000,
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B",
        "amoumt": 1000,
    },
    {
        "question": "What is the largest mammal?",
        "options": ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Hippopotamus"],
        "answer": "B",
        "amoumt": 1000,
    },
    {
        "question": "Who discovered gravity?",
        "options": [
            "A) Albert Einstein",
            "B) Isaac Newton",
            "C) Galileo Galilei",
            "D) Nikola Tesla",
        ],
        "answer": "B",
        "amoumt": 1000,
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["A) China", "B) Japan", "C) Thailand", "D) South Korea"],
        "answer": "B",
        "amoumt": 1000,
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A) CO2", "B) H2O", "C) O2", "D) NaCl"],
        "answer": "B",
        "amoumt": 1000,
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": [
            "A) Vincent van Gogh",
            "B) Pablo Picasso",
            "C) Leonardo da Vinci",
            "D) Michelangelo",
        ],
        "answer": "C",
        "amoumt": 1000,
    },
    {
        "question": "Which is the smallest continent?",
        "options": ["A) Europe", "B) Australia", "C) Antarctica", "D) South America"],
        "answer": "B",
        "amoumt": 1000,
    },
    {
        "question": "What is the hardest natural substance?",
        "options": ["A) Gold", "B) Iron", "C) Diamond", "D) Silver"],
        "answer": "C",
        "amoumt": 1000,
    },
)

wining_amount = 0
for i in range(5):
    random_number = random.randint(1, 10)
    print(gk_questions[random_number]["question"], "\n")
    print(gk_questions[random_number]["options"], "\n")
    User_answer = input("Enter your options? (A, B, C, D) : ")
    User_answer = User_answer[0].upper()
    Original_answer = gk_questions[random_number]["answer"]
    if User_answer == Original_answer:
        print("Your Answer is Correct ! \n")
        amount = gk_questions[random_number]["amoumt"]
        wining_amount = wining_amount + amount
        print(wining_amount, "\n")
    else:
        print("Your answer is Wrong ! \n")
        print(gk_questions[random_number]["question"] , "\n")
        print(gk_questions[random_number]["options"], "\n")
        User_answer = input(" \n Enter your options? (A, B, C, D) : ")
        User_answer = User_answer[0].upper()
