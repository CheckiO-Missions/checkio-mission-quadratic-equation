"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[2, 4, 6]],
            "answer": "2*x**2 - 20*x + 48 = 0",
            "explanation": "ordinary case"
        },
        {
            "input": [[-2, 4, 6]],
            "answer": "-2*x**2 + 20*x - 48 = 0",
            "explanation": "minus a"
        },
        {
            "input": [[2, 4, -4]],
            "answer": "2*x**2 - 32 = 0",
            "explanation": "x1 = -x2"
        },
        {
            "input": [[2, 4, 0]],
            "answer": "2*x**2 - 8*x = 0",
            "explanation": "x2 = 0"
        },
        {
            "input": [[2, 0]],
            "answer": "2*x**2 = 0",
            "explanation": "x1 = x2 = 0"
        },
        {
            "input": [[2, 4]],
            "answer": "2*x**2 - 16*x + 32 = 0",
            "explanation": "x1 = x2"
        }
    ],
    "Extra": [
        {
            "input": [[1, 0]],
            "answer": "x**2 = 0"
        },
        {
            "input": [[-1, 0]],
            "answer": "-x**2 = 0"
        },
        {
            "input": [[1, 1]],
            "answer": "x**2 - 2*x + 1 = 0"
        },
        {
            "input": [[-1, 1]],
            "answer": "-x**2 + 2*x - 1 = 0"
        },
        {
            "input": [[1, 1, 0]],
            "answer": "x**2 - x = 0"
        },
        {
            "input": [[1, 1, -1]],
            "answer": "x**2 - 1 = 0"
        }
    ]
}
