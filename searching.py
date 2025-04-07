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




def main():
    pass


if __name__ == '__main__':
    main()
    json_filename = "sequential.json"
    sequential_data  = read_data(json_filename, "unordered_numbers")
    print(sequential_data )