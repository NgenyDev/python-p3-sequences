def print_fibonacci(length):
    if length <= 0:
        print([])  # Return an empty list if the length is less than or equal to 0
        return
    elif length == 1:
        print([0])
        return

    # Initialize the first two terms
    a, b = 0, 1
    fibonacci_list = [a]

    # Generate the Fibonacci sequence
    for _ in range(1, length):
        fibonacci_list.append(b)
        a, b = b, a + b

    # Print the Fibonacci sequence as a list
    print(fibonacci_list)
