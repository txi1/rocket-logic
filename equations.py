import random

def generate_equation(complexity):

    possible_true_bases = ['p ∨ T','p ∨ ¬p', 'p → p', 'T ∨ F', 'p ∨ (p ∨ T)']
    possible_false_bases = ['p ∧ F', 'p ∧ ¬p', '¬p ↔ p', 'T ∧ F', 'p ∧ (p ∧ F)']
    possible_contingent_bases = ['p ∧ (p ∨ T)', 'p ∧ (p ∨ F)', 'p ∨ (p ∧ T)', 'p ∨ (p ∧ F)']

    random_number = random.randint(1,3)
    if random_number == 1:
        base = random.choice(possible_true_bases)
        return convert(complicate_equation(base,complexity,possible_true_bases, possible_false_bases, possible_contingent_bases)), 'T'
    elif random_number == 2:
        base = random.choice(possible_false_bases)
        return convert(complicate_equation(base,complexity,possible_true_bases, possible_false_bases, possible_contingent_bases)), 'F'
    else:
        base = random.choice(possible_contingent_bases)
        return convert(complicate_equation(base,complexity,possible_true_bases, possible_false_bases, possible_contingent_bases)), 'p'
    

def complicate_equation(current_equation, complexity, true_expressions, false_expressions, contingent_expressions):
    if complexity == 1:
        return current_equation
    else:
        equation_as_list = current_equation.split()
        new_equation = replace_parts(current_equation,complexity,true_expressions,false_expressions,contingent_expressions)

        return complicate_equation(new_equation,complexity-1,true_expressions,false_expressions,contingent_expressions)

def replace_parts(to_change,changes,true_expressions,false_expressions,contingent_expressions):
    for x in range(changes):
        location_of_letters = find('T',to_change) + find('F',to_change) + find('p',to_change)
        if len(location_of_letters):
            a = random.choice(location_of_letters)
            original_length = len(to_change)
            if to_change[a] == 'T':
                if random.randint(1,2) == 2:
                    to_change = to_change[0:a] + '('+random.choice(true_expressions)+')' + to_change[a+1:]
                else:
                    to_change = to_change[0:a] + '¬('+random.choice(false_expressions)+')' + to_change[a+1:]
                difference = len(to_change)-original_length
                for item in location_of_letters:
                    if item > a:
                        item+=difference
                location_of_letters.pop(location_of_letters.index(a))
            elif to_change[a] == 'F':
                if random.randint(1,2) == 2:
                    to_change = to_change[0:a] + '('+random.choice(false_expressions)+')' + to_change[a+1:]
                else:
                    to_change = to_change[0:a] + '¬('+random.choice(true_expressions)+')' + to_change[a+1:]
                difference = len(to_change)-original_length
                for item in location_of_letters:
                    if item > a:
                        item+=difference
                location_of_letters.pop(location_of_letters.index(a))
            elif to_change[a] == 'p':
                to_change = to_change[0:a] +'('+random.choice(contingent_expressions)+')' + to_change[a+1:]
                difference = len(to_change)-original_length
                for item in location_of_letters:
                    if item > a:
                        item+=difference
                location_of_letters.pop(location_of_letters.index(a))
    return to_change

def convert(equation):
    equation = equation.replace('∨','V')
    equation = equation.replace('∧','^')
    equation = equation.replace('→','-<')
    equation = equation.replace('↔', '>-<')
    return equation

def find(target,equation):
    return [i for i, ltr in enumerate(equation) if ltr == target]


a,b = generate_equation(2)
8
