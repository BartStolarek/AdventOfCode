# Advent of Code 2024 - Day 1 Part 1 Solution

def get_input() -> str:
    """Get the input data from the file.

    Returns:
        str: A string containing the input data.
    """
    with open("2024/1/input1.txt", "r", encoding="utf-8") as file:
        return file.read().strip()


def parse_input(input_data: str) -> tuple:
    """Parse the input data into two lists of integers,
    one for the left side and one for the right side.
    
    Sorts both lists in ascending order.

    Args:
        input_data (str): A string of input data where each line contains two integers

    Returns:
        tuple: A tuple containing two lists of integers
    """
    l_list, r_list = [], []
    for line in input_data.splitlines():
        # Split the line into two parts and convert them to integers
        left = int(line.split("   ")[0])
        right = int(line.split("   ")[1])

        # Append the integers to their respective lists
        l_list.append(left)
        r_list.append(right)

    # Sort both lists in ascending order
    l_list.sort()
    r_list.sort()

    return l_list, r_list


def calculate_distance(l_list: list, r_list: list) -> int:
    """For each pair of integers from the two lists,
    calculate the absolute difference and sum them up.

    Args:
        l_list (list): list of integers from the left side
        r_list (list): list of integers from the right side

    Returns:
        int: The total distance calculated as the sum of absolute differences
    """
    total_distance = 0
    for left, right in zip(l_list, r_list):
        total_distance += abs(left - right)
    return total_distance


raw_input = get_input()

left_list, right_list = parse_input(raw_input)

print(calculate_distance(left_list, right_list))
