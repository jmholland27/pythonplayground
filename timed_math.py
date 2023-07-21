import random
import time

operators = ['+', '-', '*']
min_number = 1
max_number = 12
number_of_problems = 10
correct = 0

def generate_problem(oper, min_num, max_num):
    operator = random.choice(oper)
    num1 = random.randrange(min_number, max_number + 1)
    num2 = random.randrange(min_number, max_number + 1)

    return operator, num1, num2

start_time = time.time()

for i in range(number_of_problems):
    operator, num1, num2 = generate_problem(operators, min_number, max_number)

    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    
    response = float(input(f'{num1} {operator} {num2} = '))

    if response == answer:
        correct += 1

end_time = time.time()
total_time = end_time - start_time

print(f'Number of correct answers was {correct}')
time.sleep(2)
print(f'It took {total_time:.2f} seconds to answer the questions')