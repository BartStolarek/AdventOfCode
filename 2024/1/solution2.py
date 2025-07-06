# Advent of Code 2024 - Day 1 Part 2 Solution

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


def calculate_similarity_score(l_list: list, r_list: list) -> int:
    """Calculate the similarity score by multiplying each number in the left list
    by the number of times it appears in the right list, then summing all results.
    
    Args:
        l_list (list): List of integers from the left side
        r_list (list): List of integers from the right side
        
    Returns:
        int: The total similarity score
    """
    similarity_score = 0

    for left in l_list:
        # Count how many times this number appears in the right list
        count = r_list.count(left)
        # Add to similarity score: number * count
        similarity_score += count * left

    return similarity_score


# Main execution
raw_input = get_input()
parsed_left_list, parsed_right_list = parse_input(raw_input)
print(calculate_similarity_score(parsed_left_list, parsed_right_list))
