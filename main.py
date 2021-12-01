# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import pickle
import sys
sys.path.insert(1, "C:\\Users\\valer\\PycharmProjects\\Pack")
from ReadTxt import ReadTxt



def shell_sort(seq: dict, dct_key: str):
    counter = 1
    if len(seq) % 2 == 0:
        step = len(seq) // 2
    else:
        step = len(seq) // 2 + 1
    while step:
        for i, elem in enumerate(seq):
            while i >= step and seq[i - step][dct_key] > elem[dct_key]:
                if step == 44913:
                    counter += 1
                seq[i] = seq[i - step]
                i = i - step
            seq[i] = elem
        if step % 2 == 0:
            step = step // 2
        else:
            if step != 1:
                step = step // 2 + 1  # if step == 2 else int(step * 5.0 / 11)
            else:
                break


def check_sort_correct(seq: dict, dct_key: str):
    error_flag = False
    for i in range(len(seq) - 1):
        if seq[i + 1][dct_key] < seq[i][dct_key]:
            error_flag = True
            print("False ", i)
            print('This:', seq[i + 1][dct_key], "<", 'Previous:', seq[i][dct_key], '?')
    if not error_flag:
        print("The values are increasing")


def create_list_of_values(seq: dict, dct_key: str):
    list_of_value = []
    presence_flag = False
    for i, elem in enumerate(seq):
        for j in list_of_value:
            if elem[dct_key] == j:
                presence_flag = True
        if not presence_flag:
            list_of_value.append(elem[dct_key])
        presence_flag = False
    return list_of_value


valid_path = 'C:\\Lab_2\\23valid.txt'
pickle_path = 'C:\\Lab_3\\sorted.pickle'
data_list_of_dict = json.load(open(valid_path))
users_list = []
# list_of_values = create_list_of_values(data_list_of_dict, "age")
# print(list_of_values)
shell_sort(data_list_of_dict, "age")
check_sort_correct(data_list_of_dict, "age")
# list_of_values = create_list_of_values(data_list_of_dict, "age")
# print(list_of_values)
with open(pickle_path, "wb") as file:
    pickle.dump(data_list_of_dict, file)
with open(pickle_path, "rb") as file:
    data_after_pickle = pickle.load(file)
# print(data_after_pickle)
for i in data_after_pickle:
    users_list.append(ReadTxt(i['email'], i['height'], i['inn'], i['passport_series'], i['occupation'], i['age'],
                              i['academic_degree'], i['worldview'], i['address']))

# print(data_list_of_dict)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
