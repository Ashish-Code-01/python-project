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
        "question": "10. What happens: def func(x=[]):\n    x.append(1)\n    return x",
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
    {
        "question": "21. What is the output of: print(int('100', 2))",
        "options": ["a) 100", "b) 4", "c) 2", "d) ValueError"],
        "correct": "b",
        "explanation": "int('100', 2) converts binary '100' to decimal, which is 4",
    },
    {
        "question": "22. What happens when you run: a = []; a.extend([1, [2, 3]]); print(a)",
        "options": ["a) [1, 2, 3]", "b) [1, [2, 3]]", "c) [[1, 2, 3]]", "d) Error"],
        "correct": "b",
        "explanation": "extend adds each element of the iterable to the list, not recursively",
    },
    {
        "question": "23. What is the output of: print('a' + 'b' is 'ab')",
        "options": ["a) True", "b) False", "c) SyntaxError", "d) TypeError"],
        "correct": "a",
        "explanation": "String literals are interned in Python, so 'a'+'b' and 'ab' reference the same object",
    },
    {
        "question": "24. What is the result of: print(round(2.5) + round(3.5))",
        "options": ["a) 6", "b) 7", "c) 5", "d) 6.0"],
        "correct": "a",
        "explanation": "Python rounds to the nearest even number when exactly halfway, so 2.5 rounds to 2 and 3.5 rounds to 4",
    },
    {
        "question": "25. What is the output of: print(sorted([3, 2, 1], reverse=True))",
        "options": ["a) [1, 2, 3]", "b) [3, 2, 1]", "c) Error", "d) None"],
        "correct": "b",
        "explanation": "sorted() with reverse=True sorts in descending order",
    },
    {
        "question": "26. What happens: print(list(range(5, 0, -1)))",
        "options": ["a) [5, 4, 3, 2, 1]", "b) [5, 4, 3, 2, 1, 0]", "c) []", "d) Error"],
        "correct": "a",
        "explanation": "range(5, 0, -1) counts down from 5 to 1 (0 is exclusive)",
    },
    {
        "question": "27. What is the output of: print(2 ** 3 ** 2)",
        "options": ["a) 64", "b) 512", "c) 8", "d) 36"],
        "correct": "b",
        "explanation": "Exponentiation is right-associative, so 2 ** 3 ** 2 is 2 ** (3 ** 2) = 2 ** 9 = 512",
    },
    {
        "question": "28. What is the result of: print(1 < 2 < 3 < 4 > 0)",
        "options": ["a) True", "b) False", "c) SyntaxError", "d) TypeError"],
        "correct": "a",
        "explanation": "Chained comparisons are evaluated as: 1 < 2 and 2 < 3 and 3 < 4 and 4 > 0",
    },
    {
        "question": "29. What is the output of: print(sum([1, 2, 3], 10))",
        "options": ["a) 16", "b) [10, 1, 2, 3]", "c) 6", "d) TypeError"],
        "correct": "a",
        "explanation": "The second argument to sum() is the start value, so 10 + 1 + 2 + 3 = 16",
    },
    {
        "question": "30. What happens: print(list(filter(None, [0, False, 1, '', 'a', []])))",
        "options": ["a) [1, 'a']", "b) [1, 'a', []]", "c) [0, False, 1, '', 'a', []]", "d) [1, '', 'a']"],
        "correct": "a",
        "explanation": "filter(None, iterable) returns only truthy values (1 and 'a')",
    },
    {
        "question": "31. What is the output of: print(chr(ord('A') + 32))",
        "options": ["a) 'a'", "b) 'A'", "c) ''", "d) Error"],
        "correct": "a",
        "explanation": "ord('A') is 65, adding 32 gives 97, and chr(97) is 'a' (ASCII conversion)",
    },
    {
        "question": "32. What is the result of: print(0 or 1 and 2)",
        "options": ["a) 0", "b) 1", "c) 2", "d) False"],
        "correct": "c",
        "explanation": "'and' has higher precedence than 'or', so 1 and 2 evaluates to 2, then 0 or 2 evaluates to 2",
    },
    {
        "question": "33. What happens: print(dict.fromkeys(['a', 'b', 'c'], 1))",
        "options": [
            "a) {'a': 1, 'b': 1, 'c': 1}",
            "b) {'a': 'a', 'b': 'b', 'c': 'c'}",
            "c) {'a': None, 'b': None, 'c': None}",
            "d) Error",
        ],
        "correct": "a",
        "explanation": "dict.fromkeys creates a dictionary with the given keys and value (1)",
    },
    {
        "question": "34. What is the output of: print(list(zip([1, 2], [3, 4, 5])))",
        "options": [
            "a) [(1, 3), (2, 4), (None, 5)]",
            "b) [(1, 3), (2, 4)]",
            "c) [(1, 3, None), (2, 4, None), (None, 5, None)]",
            "d) Error",
        ],
        "correct": "b",
        "explanation": "zip stops when the shortest iterable is exhausted",
    },
    {
        "question": "35. What is the result of: print(any([0, '', False, None, []]))",
        "options": ["a) True", "b) False", "c) None", "d) Error"],
        "correct": "b",
        "explanation": "any() returns True if at least one element is truthy, but all are falsy here",
    },
    {
        "question": "36. What happens: print(divmod(10, 3))",
        "options": ["a) 3.33", "b) (3, 1)", "c) 3", "d) (3.0, 1.0)"],
        "correct": "b",
        "explanation": "divmod returns a tuple of (quotient, remainder)",
    },
    {
        "question": "37. What is the output of: print(hash('hello') == hash('hello'))",
        "options": ["a) True", "b) False", "c) Error", "d) None"],
        "correct": "a",
        "explanation": "Same strings have the same hash value",
    },
    {
        "question": "38. What is the result of: print(set('mississippi'))",
        "options": [
            "a) {'m', 'i', 's', 'p'}",
            "b) {'mississippi'}",
            "c) {'m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i'}",
            "d) Error",
        ],
        "correct": "a",
        "explanation": "set() creates a set with unique characters from the string",
    },
    {
        "question": "39. What happens: print(float('inf') > 10**1000)",
        "options": ["a) True", "b) False", "c) OverflowError", "d) ValueError"],
        "correct": "a",
        "explanation": "Infinity is greater than any finite number, even very large ones",
    },
    {
        "question": "40. What is the output of: print(bin(5)[2:].zfill(4))",
        "options": ["a) '0101'", "b) '0b0101'", "c) '101'", "d) Error"],
        "correct": "a",
        "explanation": "bin(5) is '0b101', [2:] removes '0b', and zfill(4) pads with zeros to length 4",
    },
    {
        "question": "41. What is the result of: print(isinstance(lambda x: x, object))",
        "options": ["a) True", "b) False", "c) TypeError", "d) SyntaxError"],
        "correct": "a",
        "explanation": "In Python, everything is an object, including lambda functions",
    },
    {
        "question": "42. What happens: print(next(iter([1, 2, 3])))",
        "options": ["a) [1, 2, 3]", "b) 1", "c) StopIteration", "d) TypeError"],
        "correct": "b",
        "explanation": "next() returns the first item from the iterator",
    },
    {
        "question": "43. What is the output of: print(abs(-5) is 5)",
        "options": ["a) True", "b) False", "c) Error", "d) None"],
        "correct": "a",
        "explanation": "Small integers are interned in Python, so abs(-5) and 5 reference the same object",
    },
    {
        "question": "44. What is the result of: print(list(map(lambda x: x*2, range(3))))",
        "options": ["a) [0, 1, 2]", "b) [0, 2, 4]", "c) [0, 2, 4, 6]", "d) Error"],
        "correct": "b",
        "explanation": "map applies the lambda function to each element in range(3), doubling each value",
    },
    {
        "question": "45. What happens: print(complex(1, 2) * complex(3, 4))",
        "options": ["a) (3+8j)", "b) (-5+10j)", "c) (1+2j)", "d) Error"],
        "correct": "b",
        "explanation": "Complex multiplication: (1+2j)*(3+4j) = (1*3 - 2*4) + (1*4 + 2*3)j = -5 + 10j",
    },
    {
        "question": "46. What is the output of: print(globals()['__name__'])",
        "options": ["a) 'globals'", "b) '__main__'", "c) 'builtins'", "d) Error"],
        "correct": "b",
        "explanation": "__name__ is '__main__' when the script is run directly",
    },
    {
        "question": "47. What is the result of: print(hasattr(str, 'join'))",
        "options": ["a) True", "b) False", "c) AttributeError", "d) TypeError"],
        "correct": "a",
        "explanation": "The string class has a 'join' method",
    },
    {
        "question": "48. What happens: print(format(123, '08d'))",
        "options": ["a) '00000123'", "b) '123'", "c) '123.000'", "d) Error"],
        "correct": "a",
        "explanation": "format with '08d' pads with zeros to make the number 8 digits long",
    },
    {
        "question": "49. What is the output of: print(all([1, 2, 3, 0]))",
        "options": ["a) True", "b) False", "c) 1", "d) Error"],
        "correct": "b",
        "explanation": "all() returns True if all elements are truthy, but 0 is falsy",
    },
    {
        "question": "50. What is the result of: print(id(None) == id(None))",
        "options": ["a) True", "b) False", "c) TypeError", "d) NameError"],
        "correct": "a",
        "explanation": "None is a singleton in Python, so all references to None have the same id",
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

    print(f"\nFinal Score: {score}/50")
    print(f"Percentage: {(score/50)*100}%")


if __name__ == "__main__":
    print("Welcome to the Python Tricky Questions Quiz!")
    print("==========================================")
    run_quiz()
