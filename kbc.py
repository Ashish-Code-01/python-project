import random

gk_questions = [
    {
        "question": "What is the capital of Italy?",
        "options": ["A) Rome", "B) Madrid", "C) Athens", "D) Lisbon"],
        "answer": "A",
        "amount": 1000,
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["A) Oxygen", "B) Nitrogen", "C) Carbon Dioxide", "D) Hydrogen"],
        "answer": "C",
        "amount": 1000,
    },
    {
        "question": "Who invented the telephone?",
        "options": [
            "A) Alexander Graham Bell",
            "B) Thomas Edison",
            "C) Nikola Tesla",
            "D) Guglielmo Marconi",
        ],
        "answer": "A",
        "amount": 1000,
    },
    {
        "question": "Which is the longest river in the world?",
        "options": ["A) Amazon", "B) Nile", "C) Yangtze", "D) Mississippi"],
        "answer": "B",
        "amount": 1000,
    },
    {
        "question": "What is the square root of 144?",
        "options": ["A) 10", "B) 11", "C) 12", "D) 13"],
        "answer": "C",
        "amount": 1000,
    },
    {
        "question": "Which element has the chemical symbol 'Fe'?",
        "options": ["A) Fluorine", "B) Iron", "C) Francium", "D) Fermium"],
        "answer": "B",
        "amount": 1000,
    },
    {
        "question": "Who is known as the Father of Computers?",
        "options": [
            "A) Alan Turing",
            "B) Charles Babbage",
            "C) Bill Gates",
            "D) Steve Jobs",
        ],
        "answer": "B",
        "amount": 1000,
    },
    {
        "question": "Which planet has the most moons?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "D",
        "amount": 1000,
    },
    {
        "question": "What is the national animal of India?",
        "options": ["A) Lion", "B) Elephant", "C) Tiger", "D) Peacock"],
        "answer": "C",
        "amount": 1000,
    },
    {
        "question": "Which organ purifies blood in the human body?",
        "options": ["A) Heart", "B) Liver", "C) Kidney", "D) Lungs"],
        "answer": "C",
        "amount": 1000,
    },
    {
        "question": "Which is the largest desert in the world?",
        "options": ["A) Sahara", "B) Gobi", "C) Kalahari", "D) Antarctic"],
        "answer": "D",
        "amount": 1000,
    },
    {
        "question": "What is the boiling point of water at sea level?",
        "options": ["A) 90°C", "B) 95°C", "C) 100°C", "D) 105°C"],
        "answer": "C",
        "amount": 1000,
    },
    {
        "question": "Which country hosted the 2020 Summer Olympics?",
        "options": ["A) China", "B) Japan", "C) Brazil", "D) UK"],
        "answer": "B",
        "amount": 1000,
    },
    {
        "question": "What is the currency of the United Kingdom?",
        "options": ["A) Euro", "B) Pound Sterling", "C) Dollar", "D) Franc"],
        "answer": "B",
        "amount": 1000,
    },
    {
        "question": "Which bird is known for its beautiful tail feathers?",
        "options": ["A) Peacock", "B) Parrot", "C) Swan", "D) Eagle"],
        "answer": "A",
        "amount": 1000,
    },
    {
        "question": "Which is the smallest bone in the human body?",
        "options": ["A) Femur", "B) Stapes", "C) Ulna", "D) Tibia"],
        "answer": "B",
        "amount": 1000,
    },
    {
        "question": "Which Indian city is known as the Pink City?",
        "options": ["A) Jaipur", "B) Udaipur", "C) Jodhpur", "D) Bikaner"],
        "answer": "A",
        "amount": 1000,
    },
    {
        "question": "What is the main ingredient in guacamole?",
        "options": ["A) Tomato", "B) Avocado", "C) Onion", "D) Pepper"],
        "answer": "B",
        "amount": 1000,
    },
    {
        "question": "Which festival is known as the Festival of Lights?",
        "options": ["A) Holi", "B) Diwali", "C) Eid", "D) Christmas"],
        "answer": "B",
        "amount": 1000,
    },
    {
        "question": "Which is the largest ocean on Earth?",
        "options": ["A) Atlantic", "B) Indian", "C) Pacific", "D) Arctic"],
        "answer": "C",
        "amount": 1000,
    },
    {
        "question": "Which instrument measures atmospheric pressure?",
        "options": ["A) Thermometer", "B) Barometer", "C) Hygrometer", "D) Anemometer"],
        "answer": "B",
        "amount": 1000,
    },
    {
        "question": "What is the capital of Canada?",
        "options": ["A) Toronto", "B) Vancouver", "C) Ottawa", "D) Montreal"],
        "answer": "C",
        "amount": 1000,
    },
    {
        "question": "Which vitamin is produced when the skin is exposed to sunlight?",
        "options": ["A) Vitamin A", "B) Vitamin B", "C) Vitamin C", "D) Vitamin D"],
        "answer": "D",
        "amount": 1000,
    },
    {
        "question": "Who was the first man to walk on the moon?",
        "options": [
            "A) Neil Armstrong",
            "B) Buzz Aldrin",
            "C) Yuri Gagarin",
            "D) Michael Collins",
        ],
        "answer": "A",
        "amount": 1000,
    },
    {
        "question": "Which continent has the most countries?",
        "options": ["A) Asia", "B) Africa", "C) Europe", "D) South America"],
        "answer": "B",
        "amount": 1000,
    },
    {
        "question": "Which language has the most native speakers?",
        "options": ["A) English", "B) Hindi", "C) Mandarin Chinese", "D) Spanish"],
        "answer": "C",
        "amount": 1000,
    },
    {
        "question": "Which metal is liquid at room temperature?",
        "options": ["A) Mercury", "B) Lead", "C) Zinc", "D) Copper"],
        "answer": "A",
        "amount": 1000,
    },
    {
        "question": "Which Indian river is considered the holiest?",
        "options": ["A) Yamuna", "B) Ganga", "C) Brahmaputra", "D) Godavari"],
        "answer": "B",
        "amount": 1000,
    },
    {
        "question": "Which is the tallest mountain in the world?",
        "options": ["A) K2", "B) Kangchenjunga", "C) Mount Everest", "D) Lhotse"],
        "answer": "C",
        "amount": 1000,
    },
    {
        "question": "Which country gifted the Statue of Liberty to the USA?",
        "options": ["A) Germany", "B) France", "C) Italy", "D) Spain"],
        "answer": "B",
        "amount": 1000,
    },
    {
        "question": "Which blood group is known as the universal donor?",
        "options": ["A) A", "B) B", "C) AB", "D) O negative"],
        "answer": "D",
        "amount": 1000,
    },
    {
        "question": "Which is the largest internal organ in the human body?",
        "options": ["A) Brain", "B) Liver", "C) Lungs", "D) Heart"],
        "answer": "B",
        "amount": 1000,
    },
    {
        "question": "Which Indian state is known as the 'Spice Garden of India'?",
        "options": ["A) Kerala", "B) Tamil Nadu", "C) Karnataka", "D) Assam"],
        "answer": "A",
        "amount": 1000,
    },
    {
        "question": "Which planet has a prominent ring system?",
        "options": ["A) Mars", "B) Jupiter", "C) Saturn", "D) Uranus"],
        "answer": "C",
        "amount": 1000,
    },
    {
        "question": "Which is the fastest land animal?",
        "options": ["A) Lion", "B) Cheetah", "C) Horse", "D) Gazelle"],
        "answer": "B",
        "amount": 1000,
    },
    {
        "question": "What is the main language spoken in Brazil?",
        "options": ["A) Spanish", "B) Portuguese", "C) French", "D) English"],
        "answer": "B",
        "amount": 1000,
    },
    {
        "question": "Which is the most widely spoken language in the world?",
        "options": ["A) English", "B) Hindi", "C) Mandarin Chinese", "D) Spanish"],
        "answer": "C",
        "amount": 1000,
    },
    {
        "question": "Which Indian festival celebrates the victory of good over evil with bonfires?",
        "options": ["A) Diwali", "B) Holi", "C) Dussehra", "D) Lohri"],
        "answer": "D",
        "amount": 1000,
    },
    {
        "question": "Which is the most abundant gas in Earth's atmosphere?",
        "options": ["A) Oxygen", "B) Nitrogen", "C) Carbon Dioxide", "D) Hydrogen"],
        "answer": "B",
        "amount": 1000,
    },
    {
        "question": "Which country is famous for the Great Wall?",
        "options": ["A) Japan", "B) China", "C) Korea", "D) Mongolia"],
        "answer": "B",
        "amount": 1000,
    },
    {
        "question": "Which is the coldest place on Earth?",
        "options": ["A) Siberia", "B) Antarctica", "C) Greenland", "D) Alaska"],
        "answer": "B",
        "amount": 1000,
    },
    {
        "question": "Which Indian scientist won the Nobel Prize for Physics in 1930?",
        "options": [
            "A) C.V. Raman",
            "B) Homi Bhabha",
            "C) Vikram Sarabhai",
            "D) Satyendra Nath Bose",
        ],
        "answer": "A",
        "amount": 1000,
    },
    {
        "question": "Which is the largest island in the world?",
        "options": ["A) Greenland", "B) Australia", "C) Madagascar", "D) Borneo"],
        "answer": "A",
        "amount": 1000,
    },
    {
        "question": "Which is the most spoken language in India?",
        "options": ["A) Hindi", "B) Bengali", "C) Telugu", "D) Marathi"],
        "answer": "A",
        "amount": 1000,
    },
    {
        "question": "Which Indian city is known as the Silicon Valley of India?",
        "options": ["A) Hyderabad", "B) Pune", "C) Bengaluru", "D) Chennai"],
        "answer": "C",
        "amount": 1000,
    },
    {
        "question": "Which part of the plant conducts photosynthesis?",
        "options": ["A) Root", "B) Stem", "C) Leaf", "D) Flower"],
        "answer": "C",
        "amount": 1000,
    },
    {
        "question": "Which is the largest gland in the human body?",
        "options": ["A) Pancreas", "B) Thyroid", "C) Liver", "D) Adrenal"],
        "answer": "C",
        "amount": 1000,
    },
    {
        "question": "Which Indian state has the longest coastline?",
        "options": [
            "A) Maharashtra",
            "B) Tamil Nadu",
            "C) Gujarat",
            "D) Andhra Pradesh",
        ],
        "answer": "C",
        "amount": 1000,
    },
    {
        "question": "Which is the only planet that rotates on its side?",
        "options": ["A) Neptune", "B) Uranus", "C) Venus", "D) Mercury"],
        "answer": "B",
        "amount": 1000,
    },
    {
        "question": "Which Mughal emperor built the Taj Mahal?",
        "options": ["A) Akbar", "B) Jahangir", "C) Shah Jahan", "D) Aurangzeb"],
        "answer": "C",
        "amount": 1000,
    },
]

wining_amount = 0
life_line = 3
for i in range(5):
    random_number = random.randint(1, 50)
    print(gk_questions[random_number]["question"], "\n")
    print(gk_questions[random_number]["options"], "\n")
    User_answer = input("Enter your options? (A, B, C, D) : ")
    print("\n")
    User_answer = User_answer[0].upper()
    Original_answer = gk_questions[random_number]["answer"]
    if User_answer == Original_answer:
        print("Your Answer is Correct ! \n")
        print(f"Your {life_line} life line is remaning! \n")
        amount = gk_questions[random_number]["amoumt"]
        wining_amount = wining_amount + amount
        print("you are winning 1000 rs \n")
    else:
        life_line = life_line - 1
        print("Your answer is Wrong ! \n")
        print(f"Your {life_line} life line is remaning! \n")
        if life_line == 0:
            break
        print(gk_questions[random_number]["question"], "\n")
        print(gk_questions[random_number]["options"], "\n")
        User_answer = input("Enter your options? (A, B, C, D) : ")
        print("\n")
        User_answer = User_answer[0].upper()
        Original_answer = gk_questions[random_number]["answer"]
        if User_answer == Original_answer:
            print("Your Answer is Correct ! \n")
            amount = gk_questions[random_number]["amoumt"]
            wining_amount = wining_amount + amount
            print("you are winning 1000 rs \n")
        else:
            print("Still wrong, Move to next question \n")
print(f"Game Over!, Your winning amount is {wining_amount}")
