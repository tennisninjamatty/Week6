# Copy each function in Jupyter noteboook. Read the function and try to understand
# what is the function doing. Think of some examples you can test it out with.
#


def sum_positive_numbers(numbers: list[int], threshold: int) -> int:
    """Count the number of instances in a list that is greater than the threshold   

    Args:
        numbers (list[int]): The list of numbers to look into
        threshold (int): The threshold to check the value against

    Returns:
        int: the number of values that are in list greater than threshold
    """
    count = 0
    for num in numbers:
        if num > 0 and num >= threshold:
            count += 1
    return count


def find_first_occurrence(s: str, target_char: str) -> int:
    """Finding the first occurence of a character in a string

    Args:
        s (str): The string
        target_char (str): The character being searched for

    Returns:
        int: The index at which the character appears
    """
    index = -1
    for i in range(len(s)):
        if s[i] == target_char:
            index = i
            break
        else:
            index = -1
    return index


def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key not in merged_dict:
            merged_dict[key] = value
        else:
            merged_dict = dict1.copy()
    return merged_dict


def filter_words_by_length(words_list: list[str], min_length: int) -> list[str]:
    filtered_words = []
    for word in words_list:
        if len(word) >= min_length:
            filtered_words.append(word)
        else:
            filtered_words = []
    return filtered_words


def calculate_average_grades(
    students_grades: list[float], passing_score: float
) -> float:
    total = 0
    count = 0
    for grade in students_grades:
        if grade >= passing_score:
            total += grade
            count += 1
        else:
            total = 0
            count = 0
    if count > 0:
        return total / count
    else:
        return 0
