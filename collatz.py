import termplotlib as tpl
import numpy as np

def print_collatz_sequence(start_number):
    numbers = []
    numbers.append(int(start_number))
    while start_number != 1:
        if start_number % 2 == 0:
            start_number = start_number/2
            numbers.append(int(start_number))
        else:
            start_number = start_number * 3 + 1
            numbers.append(int(start_number))
    print(f'{numbers}, {len(numbers)}')

def get_collatz_sequence(start_number):
    numbers = []
    numbers.append(int(start_number))
    while start_number != 1:
        if start_number % 2 == 0:
            start_number = start_number/2
            numbers.append(int(start_number))
        else:
            start_number = start_number * 3 + 1
            numbers.append(int(start_number))
    return numbers

def main():
    try:
        # Accept input from the user.
        user_input = input("Enter a number: ")
        start_number = int(user_input)
        numbers = get_collatz_sequence(start_number)
        x = np.arange(len(numbers))

        # Print the sequence.
        print(f'{numbers}, {len(numbers)}')

        # Plot the graph.
        fig = tpl.figure()
        fig.plot(x, numbers, label='Collatz', width=90)
        fig.show()
        
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()

