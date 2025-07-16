# Python "Guess the Output" Questions
# ================================

questions = [
    {
        "question": """1. What's the output of this code?
x = [1, 2, 3]
y = x
x = [4, 5, 6]
print(y)""",
        "options": ["a) [4, 5, 6]", "b) [1, 2, 3]", "c) None", "d) Error"],
        "correct": "b",
        "explanation": "When x is reassigned, it doesn't affect y. y still points to the original list [1, 2, 3]",
    },
    {
        "question": """2. Guess the output:
print(2 * 3 ** 2)""",
        "options": ["a) 12", "b) 18", "c) 36", "d) 6"],
        "correct": "b",
        "explanation": "** has higher precedence than *. So 3**2 = 9, then 2*9 = 18",
    },
    {
        "question": """3. What will this print?
x = [1, 2, 3]
print(x * 2)""",
        "options": [
            "a) [2, 4, 6]",
            "b) [1, 2, 3, 1, 2, 3]",
            "c) Error",
            "d) [1, 1, 2, 2, 3, 3]",
        ],
        "correct": "b",
        "explanation": "* with lists repeats the list elements, doesn't multiply the values",
    },
    {
        "question": """4. What's the output?
def f(x, l=[]):
    l.append(x)
    return l
print(f(1))
print(f(2))""",
        "options": ["a) [1] [2]", "b) [1] [1, 2]", "c) [1, 2] [1, 2]", "d) Error"],
        "correct": "b",
        "explanation": "Default list argument is created once and reused in subsequent calls",
    },
    {
        "question": """5. What will be printed?
print('ab' in 'abcd' in 'abcde')""",
        "options": ["a) True", "b) False", "c) Error", "d) None"],
        "correct": "b",
        "explanation": "This is evaluated as ('ab' in 'abcd') and ('abcd' in 'abcde'). First part is True, second is False",
    },
    {
        "question": """6. Output of:
a = [1, 2, 3, 4]
print(a[-1::-2])""",
        "options": ["a) [4, 2]", "b) [1, 3]", "c) [4, 3, 2, 1]", "d) Error"],
        "correct": "a",
        "explanation": "Starts from last element, steps backward by 2",
    },
    {
        "question": """7. What gets printed?
print(type(1/2))""",
        "options": [
            "a) <class 'int'>",
            "b) <class 'float'>",
            "c) <class 'number'>",
            "d) Error",
        ],
        "correct": "b",
        "explanation": "In Python 3, division always returns a float",
    },
    {
        "question": """8. Guess the output:
print('{:02d}'.format(1))""",
        "options": ["a) 1", "b) 01", "c) 2d1", "d) Error"],
        "correct": "b",
        "explanation": ":02d formats number with leading zeros, minimum 2 digits",
    },
    {
        "question": """9. What's printed?
d = {'a': 1, 'b': 2}
print(list(d))""",
        "options": ["a) ['a', 'b']", "b) [1, 2]", "c) [('a',1), ('b',2)]", "d) Error"],
        "correct": "a",
        "explanation": "Converting a dictionary to list gives list of its keys",
    },
    {
        "question": """10. Output of:
a = [1,2,3]
b = [1,2,3]
print(a is b)""",
        "options": ["a) True", "b) False", "c) Error", "d) None"],
        "correct": "b",
        "explanation": "'is' checks identity, not equality. These are different list objects with same values",
    },
    {
        "question": """11. What's the output?
print(0 or 1 and 2 or 3)""",
        "options": ["a) 0", "b) 1", "c) 2", "d) 3"],
        "correct": "c",
        "explanation": "and has higher precedence than or. 1 and 2 evaluates to 2, then 0 or 2 or 3 evaluates to 2",
    },
    {
        "question": """12. Guess what prints:
x = 'abc'
print(x[len(x)-1:-len(x)-1:-1])""",
        "options": ["a) 'abc'", "b) 'cba'", "c) ''", "d) Error"],
        "correct": "b",
        "explanation": "This slices from last char to first char in reverse order",
    },
    {
        "question": """13. What's printed?
print(sum([1, 2, 3, 4], 10))""",
        "options": ["a) 20", "b) [10, 1, 2, 3, 4]", "c) Error", "d) None"],
        "correct": "a",
        "explanation": "sum() can take a start value as second argument, adds it to sum of list",
    },
    {
        "question": """14. Output of:
print('hello'[::-1].title())""",
        "options": ["a) 'Olleh'", "b) 'olleH'", "c) 'OLLEH'", "d) 'Hello'"],
        "correct": "a",
        "explanation": "First reverses string, then capitalizes first letter",
    },
    {
        "question": """15. What prints?
print(chr(ord('A') + 32))""",
        "options": ["a) 'a'", "b) 'A'", "c) 97", "d) Error"],
        "correct": "a",
        "explanation": "ord('A') gets ASCII value, +32 converts to lowercase, chr() converts back to character",
    },
]


def run_output_quiz():
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

    print(f"\nFinal Score: {score}/{len(questions)}")
    print(f"Percentage: {(score/len(questions))*100}%")


if __name__ == "__main__":
    print("Welcome to Python Output Quiz!")
    print("============================")
    run_output_quiz()