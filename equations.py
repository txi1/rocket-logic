import random

def generate_equation(complexity):

    possible_true_bases = ['p ∨ T','p ∨ ¬p', 'T', '¬F', 'p → p', 'T ∨ F', 'p ∨ (p ∨ T)']
    possible_false_bases = ['p ∧ F', 'p ∧ ¬p', 'F', '¬T', '¬p ↔ p', 'T ∧ F', 'p ∧ (p ∧ F)']
    possible_contingent_bases = ['p', '¬p', 'p ∧ (p ∨ T)', 'p ∧ (p ∨ F)', 'p ∨ (p ∧ T)', 'p ∨ (p ∧ F)']

    random_number = random.randint(1,3)
    if random_number == 1:
        base = random.choice(possible_true_bases)
        return complicate_equation(base,complexity,possible_true_bases, possible_false_bases, possible_contingent_bases), 'T'
    elif random_number == 2:
        base = random.choice(possible_false_bases)
        return complicate_equation(base,complexity,possible_true_bases, possible_false_bases, possible_contingent_bases), 'F'
    else:
        base = random.choice(possible_contingent_bases)
        return complicate_equation(base,complexity,possible_true_bases, possible_false_bases, possible_contingent_bases), 'p'
    

def complicate_equation(current_equation, complexity, true_expressions, false_expressions, contingent_expressions):
    if complexity == 1:
        return current_equation
    else:
        equation_as_list = current_equation.split()
        new_equation = ''
        seed = random.randint(1,2)
        for item in equation_as_list:
            if seed == 2:
                if 'F' in item:
                    item = item.replace('F', f'({random.choice(false_expressions)})')
                elif 'T' in item:
                    item = item.replace('T', f'({random.choice(true_expressions)})')
                elif 'p' in item:
                    item = item.replace('p', f'({random.choice(contingent_expressions)})')
            new_equation = new_equation + item + ' '
            if seed == 2:
                seed = 1
            else:
                seed+=1
        return complicate_equation(new_equation,complexity-1,true_expressions,false_expressions,contingent_expressions)

a = generate_equation(2)
print(a)