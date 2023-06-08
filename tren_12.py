math_examples = [
    {'examples': '23 + 48',
     'answer': ['70', '51', '71', '25'],
     'right_answer': 3},
    {'examples': '5 * 13',
     'answer': ['17', '75', '65', '55'],
     'right_answer': 3},
    {'examples': '2**10',
     'answer': ['1024', '512', '2048', '20'],
     'right_answer': 1},
    {'examples': '123 - 48',
     'answer': ['62', '75', '65', '54'],
     'right_answer': 2},
    {'examples': '3 - 3 * 3',
     'answer': ['-6', '0', '6', '9'],
     'right_answer': 1},
    {'examples': '84 / 7 - 5',
     'answer': ['17', '7', '42', '12'],
     'right_answer': 2},
    {'examples': '2 + 2',
     'answer': ['1', '2', '3', '4'],
     'right_answer': 4},
    {'examples': '15**2',
     'answer': ['5', '225', '30', '125'],
     'right_answer': 2},
    {'examples': '16 * 4 / 8',
     'answer': ['8', '0.5', '16', '320'],
     'right_answer': 3},
    {'examples': '0**0',
     'answer': ['1', '0', '2', '10'],
     'right_answer': 1}
]
lent = 0
for question in math_examples:
    for y in range(4):
        for answer in question['answer']:
            print(answer)
            if int(answer) == eval(question['examples']):
                pass

    break