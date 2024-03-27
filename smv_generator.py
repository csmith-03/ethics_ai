def generate_smv_file(num_actions):
    # defines the states based on the number of actions
    states = ['Oa{}Pa{}'.format(i, j) for i in range(1, num_actions + 1) for j in range(1, num_actions + 1)]
    
    with open('generated_model.smv', 'w') as file:
        file.write('MODULE main\n')
        file.write('VAR\n')
        file.write('    s : {')
        file.write(', '.join(states))
        file.write('};\n\n')
        
        file.write('ASSIGN\n')
        file.write('    init(s) := {};\n\n'.format(states[0]))
        
        file.write('    next(s) :=\n')
        file.write('        case\n')
        
        # defines state transitions for each action
        for i in range(num_actions):
            for j in range(num_actions):
                current_state = 'Oa{}Pa{}'.format(i + 1, j + 1)
                next_state = 'Oa{}Pa{}'.format((i + 1) % num_actions + 1, (j + 2) % num_actions + 1)
                file.write(f'            s = {current_state} : {next_state};\n')
        
        file.write('        esac;\n')

def print_states(num_actions):
    states = ['Oa{}Pa{}'.format(i, j) for i in range(1, num_actions + 1) for j in range(1, num_actions + 1)]
    print("States:")
    for state in states:
        print(state)

# specifies the number of actions
num_actions = 5

# generates the SMV file
generate_smv_file(num_actions)

# prints out the states
print_states(num_actions)
