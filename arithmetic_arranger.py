def arithmetic_arranger(problems):
    arranged_problems = ''
    
    if len(problems) > 5:
        arranged_problems = 'Error: Too many problems.'
        return arranged_problems

    operators = []
    operators = list(map(lambda x: x.split()[1], problems))
    #print(len(operators))
    if set(operators) != {'+', '-'} and len(set(operators)) > 2:
        arranged_problems = 'Error: Operator must be '+' or '-'.'
        return arranged_problems

    numbers = []
    for i in problems:
        seperate = i.split()
        numbers.extend([seperate[0], seperate[2]])
        
    

