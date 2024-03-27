import matplotlib.pyplot as plt

def generate_nusmv_file(filename, num_variables, num_transitions, variable_names=None):
    # Open the file in write mode
    with open(filename, 'w') as file:
        # Write MODULE declaration
        file.write('MODULE main\n')

        # Write VAR section
        file.write('VAR\n')
        
        # If variable names are provided, use them; otherwise, use default names a-z
        if variable_names:
            for var_name in variable_names:
                file.write(f'    {var_name} : boolean;  -- {var_name} variable\n')
        else:
            for i in range(num_variables):
                file.write(f'    {chr(ord("a") + i)} : boolean;  -- {chr(ord("a") + i)} variable\n')
                
        file.write('\n')

        # Write ASSIGN section
        file.write('ASSIGN\n')

        # Initialize each variable to FALSE
        for i in range(num_variables):
            if variable_names:
                file.write(f'    init({variable_names[i]}) := FALSE;  -- not {variable_names[i]}\n')
            else:
                file.write(f'    init({chr(ord("a") + i)}) := FALSE;  -- not {chr(ord("a") + i)}\n')
        file.write('\n')

        # Write TRANS section for each variable
        for i in range(num_variables):
            if variable_names:
                file.write(f'-- STATE {i + 1}: {variable_names[i]}\n')
                file.write(f'    next({variable_names[i]}) :=\n')
            else:
                file.write(f'-- STATE {i + 1}: {chr(ord("a") + i)}\n')
                file.write(f'    next({chr(ord("a") + i)}) :=\n')
            
            file.write('        case\n')

            # Generate transitions
            for j in range(num_transitions):
                if variable_names:
                    file.write(f'            TRUE : {variable_names[i]};\n')
                else:
                    file.write(f'            TRUE : {chr(ord("a") + i)};\n')
            file.write('        esac;\n\n')

        # Write DEFINE section
        file.write('DEFINE\n')
        file.write('    property := ')

        # Define property based on the combination of all variables
        for i in range(num_variables):
            if variable_names:
                file.write(f'!{variable_names[i]} & ')
            else:
                file.write(f'!{chr(ord("a") + i)} & ')
        file.write(';  -- Property: Describe your property here\n')

def get_input(prompt):
    # User input and get rid of whitespace
    value = input(prompt)
    return value.strip()

#############################
# Use MPL to visualize states

def plot_states(num_variables, variable_names=None):
    # Define the positions of the circles representing the states
    positions = [(i * 100, 0) for i in range(num_variables)]
    
    # Plot circles representing the states
    for i, pos in enumerate(positions):
        if variable_names:
            label = variable_names[i]
        else:
            label = chr(ord("a") + i)
        circle = plt.Circle(pos, 10, color='blue', fill=False)
        plt.gca().add_patch(circle)
        plt.text(pos[0], pos[1], label, ha='center', va='center', color='black')

    # Axis limits and remove axis ticks
    plt.xlim(-20, (num_variables - 1) * 100 + 20)
    plt.ylim(-20, 20)
    plt.axis('off')
    
    # Show the plot
    plt.title("State Diagram")
    plt.show()

##############################
# User input 
    
if __name__ == "__main__":
    # Get user input for the number of variables and transitions
    num_variables = int(get_input('Enter the number of variables: '))
    num_transitions = int(get_input('Enter the number of transitions: '))
    
    # Ask the user if they want to enter custom variable names
    use_custom_names = input('Do you want to enter custom variable names? (yes/no): ').strip().lower()

    # If the user chooses to enter custom names, ask for each variable name
    if use_custom_names == 'yes':
        variable_names = []
        for i in range(num_variables):
            name = get_input(f'Enter name for variable {i + 1}: ')
            variable_names.append(name)
    else:
        variable_names = None

    # Plot states
    plot_states(num_variables, variable_names)

    # Get user input for the filename
    filename = get_input('Enter the filename to save the NuSMV file: ')

    # Generate the NuSMV file
    generate_nusmv_file(filename, num_variables, num_transitions, variable_names)
    print(f"NuSMV file '{filename}' generated successfully!")
