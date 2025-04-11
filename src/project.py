# Grammar rules and parsing table
grammar = {
    'E': ['TQ'],
    'Q': ['+TQ', '-TQ', 'ɛ'],
    'T': ['FR'],
    'R': ['*FR', '/FR', 'ɛ'],
    'F': ['a', '(E)']
}

parsing_table = {
    'E': {'a': 'TQ', '(': 'TQ'},
    'Q': {'+': '+TQ', '-': '-TQ', ')': 'ɛ', '$': 'ɛ'},
    'T': {'a': 'FR', '(': 'FR'},
    'R': {'*': '*FR', '/': '/FR', ')': 'ɛ', '$': 'ɛ'},
    'F': {'a': 'a', '(': '(E)'}
}

# Function to simulate stack-based predictive parsing
def predictive_parser(input_string):
    stack = ['$']  # Initialize stack with end marker
    stack.append('E')  # Start symbol
    input_string += '$'  # Append end marker to input
    
    index = 0  # Pointer for input string
    stack_flow = []  # To store stack content after every step

    print(f"Input: {input_string}")
    while stack:
        stack_flow.append(stack.copy())  # Record the stack flow
        top = stack.pop()  # Pop the top of the stack
        current = input_string[index]
        
        # If top matches the current input symbol
        if top == current:
            print(f"Match: {current}")
            index += 1  # Move to the next input symbol
            
        # If top is a terminal and doesn't match current input
        elif top in parsing_table:
            rule = parsing_table[top].get(current)
            if rule:
                print(f"Apply Rule: {top} -> {rule}")
                if rule != 'ɛ':  # Push rule symbols onto the stack (in reverse order)
                    stack.extend(rule[::-1])
            else:
                print(f"Error: Unexpected symbol '{current}' at index {index}.")
                print(f"Stack: {stack_flow[-1]}")
                return "Output: String is not accepted/Invalid."
        else:
            print(f"Error: Unexpected stack top '{top}'.")
            print(f"Stack: {stack_flow[-1]}")
            return "Output: String is not accepted/Invalid."
    
    print(f"Stack: {stack_flow[-1]}")
    return "Output: String is accepted/Valid." if input_string[index] == '$' else "Output: String is not accepted/Invalid."

# Test the function with the given inputs
inputs = ["(a+a)$", "(a+a)e$", "(a*a)$"]
for input_str in inputs:
    print("\nTesting Input:", input_str)
    result = predictive_parser(input_str)
    print(result)