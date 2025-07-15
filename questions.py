# Python Tricky Questions Quiz
# ==========================

questions = [
    {
        "question": "1. What will be the output of: list('123') + '4'",
        "options": [
            "a) ['1', '2', '3', '4']",
            "b) [1, 2, 3, 4]",
            "c) TypeError: can only concatenate list (not 'str') to list",
            "d) '1234'",
        ],
        "correct": "c",
        "explanation": "You cannot concatenate a string to a list. list('123') creates ['1','2','3']",
    },
    {
        "question": "2. What is the value of 1 + True + False?",
        "options": ["a) True", "b) 2", "c) 1", "d) TypeError"],
        "correct": "b",
        "explanation": "True is 1 and False is 0 in numeric context",
    },
    {
        "question": "3. What happens when you run: print(0.1 + 0.2 == 0.3)",
        "options": ["a) True", "b) False", "c) Error", "d) None"],
        "correct": "b",
        "explanation": "Due to floating-point precision in Python, 0.1 + 0.2 is slightly different from 0.3",
    },
    {
        "question": "4. What is the output of: [1,2,3,4][1:-1]",
        "options": ["a) [1,2,3]", "b) [2,3]", "c) [2,3,4]", "d) [1,2]"],
        "correct": "b",
        "explanation": "Slice [1:-1] starts from index 1 and goes up to second-to-last element",
    },
    {
        "question": "5. What is the result of: 'python'[::-1].startswith('n')",
        "options": ["a) True", "b) False", "c) SyntaxError", "d) TypeError"],
        "correct": "b",
        "explanation": "'python'[::-1] is 'nohtyp', which doesn't start with 'n'",
    },
    {
        "question": "6. What happens when you execute: x = [1,2,3]; y = x; x.append(4); print(y)",
        "options": ["a) [1,2,3]", "b) [1,2,3,4]", "c) Error", "d) None"],
        "correct": "b",
        "explanation": "Lists are mutable and y references the same list as x",
    },
    {
        "question": "7. What is the output of: print(type(type(int)))",
        "options": [
            "a) <class 'int'>",
            "b) <class 'type'>",
            "c) <class 'object'>",
            "d) TypeError",
        ],
        "correct": "b",
        "explanation": "type(int) returns the type class, and type(type) is still type",
    },
    {
        "question": "8. What will len(set([1,2,2,3,3,3,4])) return?",
        "options": ["a) 7", "b) 4", "c) TypeError", "d) 3"],
        "correct": "b",
        "explanation": "Set removes duplicates, leaving only unique elements",
    },
    {
        "question": "9. What is the output of: print(2*'3' + '4')",
        "options": ["a) 10", "b) '334'", "c) TypeError", "d) '64'"],
        "correct": "b",
        "explanation": "String multiplication repeats the string, then concatenates",
    },
    {
        "question": "10. What happens: def func(x=[]):\\n    x.append(1)\\n    return x",
        "options": [
            "a) Creates a new list each time",
            "b) Returns [1] every time",
            "c) Accumulates values with each call",
            "d) Raises an error",
        ],
        "correct": "c",
        "explanation": "Default arguments are created once when function is defined",
    },
    {
        "question": "11. What is the output of: print(1 if True else 2 if True else 3)",
        "options": ["a) 1", "b) 2", "c) 3", "d) SyntaxError"],
        "correct": "a",
        "explanation": "The first True condition is evaluated, rest is ignored",
    },
    {
        "question": "12. What is {True: 'yes', 1: 'no', 1.0: 'maybe'}",
        "options": [
            "a) {True: 'yes', 1: 'no', 1.0: 'maybe'}",
            "b) {True: 'maybe'}",
            "c) SyntaxError",
            "d) ValueError",
        ],
        "correct": "b",
        "explanation": "True, 1, and 1.0 are considered the same dictionary key",
    },
    {
        "question": "13. What is the output of: print(''.join(['1', '2', '3'])[::-1])",
        "options": ["a) ['3', '2', '1']", "b) '321'", "c) '123'", "d) TypeError"],
        "correct": "b",
        "explanation": "Joins list into string '123' then reverses it",
    },
    {
        "question": "14. What happens: x = [1,2]; x += [3,4]; print(x)",
        "options": ["a) [1,2,3,4]", "b) Error", "c) [1,2,[3,4]]", "d) [1,2]"],
        "correct": "a",
        "explanation": "+= with lists performs list extension, not append",
    },
    {
        "question": "15. What is the value of: 5 > 4 > 3",
        "options": ["a) True", "b) False", "c) SyntaxError", "d) TypeError"],
        "correct": "a",
        "explanation": "This is equivalent to 5 > 4 and 4 > 3",
    },
    {
        "question": "16. What is printed: a = [1,2,3]; a.append(a); print(len(a))",
        "options": ["a) 3", "b) 4", "c) Infinite", "d) Error"],
        "correct": "b",
        "explanation": "List contains 3 numbers plus itself as fourth element",
    },
    {
        "question": "17. What is the output of: print(bool('False'))",
        "options": ["a) False", "b) True", "c) 'False'", "d) Error"],
        "correct": "b",
        "explanation": "Any non-empty string is True when converted to boolean",
    },
    {
        "question": "18. What happens: print(tuple('hello'))",
        "options": [
            "a) ('hello')",
            "b) ('h','e','l','l','o')",
            "c) TypeError",
            "d) ['h','e','l','l','o']",
        ],
        "correct": "b",
        "explanation": "tuple() converts iterable to tuple of its elements",
    },
    {
        "question": "19. What is the output: print(eval('2+3'))",
        "options": ["a) '2+3'", "b) 5", "c) Error", "d) None"],
        "correct": "b",
        "explanation": "eval() evaluates a string as Python expression",
    },
    {
        "question": "20. What is returned by: min(max(False,True), True)",
        "options": ["a) False", "b) True", "c) 0", "d) 1"],
        "correct": "b",
        "explanation": "max(False,True) returns True, then min(True,True) returns True",
    },
]


def run_quiz():
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        answer = input("\nYour answer (a/b/c/d): ").lower()
        if answer == q["correct"]:
            print("Correct! ✓")
            print("Explanation:", q["explanation"])
            score += 1
        else:
            print("Wrong! ✗")
            print(f"The correct answer was: {q['correct']}")
            print("Explanation:", q["explanation"])

    print(f"\nFinal Score: {score}/20")
    print(f"Percentage: {(score/20)*100}%")


if __name__ == "__main__":
    print("Welcome to the Python Tricky Questions Quiz!")
    print("==========================================")
    run_quiz()
