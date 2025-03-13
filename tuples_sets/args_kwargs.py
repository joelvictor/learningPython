# Basic args example (accepts multiple positional arguments)
def sum_numbers(*args):
    return sum(args)

# Basic kwargs example (accepts multiple keyword arguments)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Combining args and kwargs with regular parameters
def mixed_function(name, *args, default_value="Hello", **kwargs):
    print(f"Name: {name}")
    print(f"Args: {args}")
    print(f"Default value: {default_value}")
    print(f"Kwargs: {kwargs}")

# Example usage
if __name__ == "__main__":
    # Using args
    print(sum_numbers(1, 2, 3, 4, 5))  # Output: 15
    numbers = [1, 2, 3]
    print(sum_numbers(*numbers))  # Unpacking list into args

    # Using kwargs
    print_info(name="John", age=30, city="New York")

    # Using mixed function
    mixed_function(
        "Alice",                    # regular parameter
        1, 2, 3,                   # args
        default_value="Hi",        # default parameter
        job="developer",           # kwargs
        country="Canada"
    )