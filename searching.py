import os
import json
# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as file:
        data = json.load(file)
        if field in data.keys():
            return data[field]
        else:
            print(f"Field {field} does not exist.")
            return None

def linear_search(list_of_numbers, number):
    indexes = []
    for index, element in enumerate(list_of_numbers):
        if element == number:
            indexes.append(index)
        else:
            pass
    return {"positions": indexes, "count": len(indexes)}

def pattern_search(sequence, pattern):
    set_of_indexes = set()
    pattern_length = len(pattern)
    for idx in range(0, len(sequence) - pattern_length):
        pattern_similarity = 0
        for idx_pattern, pattern_element in enumerate(pattern):
            if sequence[idx + idx_pattern] == pattern_element:
                pattern_similarity += 1
            else:
                break
            if pattern_similarity == pattern_length:
                set_of_indexes.add(idx + pattern_length // 2-1)
            else:
                pass
        return set_of_indexes

def pattern_search_while(sequence, pattern):
    pos = set()
    index = 0
    while index < len(sequence) - len(pattern):
        if sequence[index:index + len(pattern)] == pattern:
            index += 1
    return pos

def binary_search(sequence, searched_number):
    left = 0
    right = len(sequence) - 1
    while right >= left:
        middle = (left + right) // 2
        print(sequence[middle])
        if sequence[middle] == searched_number:
            return middle
        elif sequence[middle] > searched_number:
            right = middle - 1
        elif sequence[middle] < searched_number:
            left = middle + 1
    return None





def main():
    json_filename = "sequential.json"
    key_of_sequence = "dna_sequence"
    sequential_data = read_data(json_filename, key_of_sequence)
    print(sequential_data)

    found_numbers = linear_search(sequential_data,"A")
    print(found_numbers)

    data = pattern_search(sequential_data, "AAG")
    print(data)



if __name__ == '__main__':
    searched_index = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12], 9)
    main()
