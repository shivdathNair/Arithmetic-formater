def arithmetic_arranger(problems):
    arranged_problems = ''

    # Checking for number of problems
    if len(problems) > 5:
        arranged_problems = 'Error: Too many problems.'
        return arranged_problems

    # Checking for operators in the problem and seperating them
    operators = []
    operators = list(map(lambda x: x.split()[1], problems))
    #print(len(operators))
    if set(operators) != {'+', '-'} and len(set(operators)) > 2:
        arranged_problems = 'Error: Operator must be '+' or '-'.'
        return arranged_problems

    # Seperating numbers in the problem
    numbers = []
    for i in problems:
        seperate = i.split()
        numbers.extend([seperate[0], seperate[2]])

    # Checking for digits and size of numbers
    for i in numbers:
        #print(i)
        if not i.isdigit():
            arranged_problems = "Error: Numbers must only contain digits."
            return arranged_problems
        #print(len(i))
        if len(i) > 4:
            arranged_problems = "Error: Numbers cannot be more than four digits."
            return arranged_problems



        
    

