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
            "input": ["sims", "s"],
            "answer": 3
        },
        {
            "input": ["find the river", "e"],
            "answer": 12
        },
        {
            "input": ["hi", " "],
            "answer": None,
            "explanation": "No space in a given line."
        },
        {
            "input": ["hi mayor", " "],
            "answer": None,
            "explanation": "Only one space in a give line, we are looking for the second one"
        },
        {
            "input": ["hi mr Mayor", " "],
            "answer": 5
        }
    ],
    "Extra": [
        {
            "input": ["hi", "i"],
            "answer": None,
        },
        {
            "input": ["abc", "d"],
            "answer": None
        },
        {
            "input": ["see you", "e"],
            "answer": 2
        },
        {
            "input": ["three occurrences", "r"],
            "answer": 10
        }
    ]
}
