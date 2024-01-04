"""
    Module name :- utils.py
    Method(s) :- format(number),
    simple_interest(principal, time, rate),
    compound_interest(principal, time, rate),
    compound_interest_with_payments(principal, payment, term, rate, end_of_period=False),
    savings_calculator(present_value, future_value, term, rate, end_of_period=True),
    create_dict_with_keys(data, keys),
    extract_data_and_common_keys(filename1, filename2),
    files_innerjoin(filename1, filename2, **kwargs),
    files_leftouterjoin(filename1, filename2, **kwargs),
    files_rightouterjoin(filename1, filename2, **kwargs),
    list_to_dict(data: list),
    dict_to_list(data: dict),
    split_file(filename, split_cols: list)
"""

import csv


def formatting(number):
    """
    Format number in Indian format upto 2 decimal place

    Args:-
        number(int) :- Number in integer format

    Return
        Number formatted in Indian format upto 2 decimal places.
    """
    number = round(number, 2)

    if "." in str(number):
        integer, frac = str(number).split(".")
    else:
        integer, frac = str(number), ""

    for i in range(len(integer) - 3, 0, -2):
        integer = integer[:i] + "," + integer[i:]

    if frac:
        frac = "." + frac

    return integer + frac


def simple_interest(principal, time, rate):
    """
    Find simple interest over a period of time.

    Args:-
        principal(int) :- Principal amount.
        time(int) :- Period of ivestment.
        rate(float) :- Rate of interest.

    Return
        Total amount.
    """
    return formatting(principal * (1 + time * rate))


def compound_interest(principal, time, rate):
    """
    Find compound interest over a period of time.

    Args:-
        principal(int) :- Principal amount.
        time(int) :- Period of ivestment.
        rate(float) :- Rate of interest.

    Return
        Total amount.
    """
    return formatting(principal * ((1 + rate) ** time))


def compound_interest_with_payments(
    principal, payment, term, rate, end_of_period=False
):
    """
    Find compound interest with annual payments over a period of time.

    Args:-
        principal(int) :- Principal amount.
        time(int) :- Period of ivestment.
        rate(float) :- Rate of interest.
        end_of_period(bool) :- Payment made at end of period.

    Return
        Total principal.
    """
    amount = 0

    if not end_of_period:
        principal += payment

    for _ in range(1, term):
        amount = principal * (rate)
        principal += amount + payment

    return formatting(principal)


def savings_calculator(present_value, future_value, term, rate, end_of_period=True):
    """
    Find the amount to be paid at intervals to get future_value.

    Args:-
        present_value(float) :- Current amount.
        future_value(float) :- Future amount.
        term(int) :- Peroid of investment
        rate(float) :- Rate of interest.
        end_of_period(bool) :- Payment made at end of period.

    Return
        Payments to be paid at intervals to get the desired amount.
    """
    if not end_of_period:
        rate /= 1 + rate
    net_value = future_value - present_value * ((1 + rate) ** term)
    principal = net_value / ((1 + rate) ** term - 1)

    return formatting(principal)


def create_dict_with_keys(data, keys):
    """
    Create dictionary with guven keys.

    Args:-
        data(list) :- List of dictionaries.
        keys(list) :- Keys of dictionary

    Return
        Dictionary with given key.
    """
    results = []

    for entry in data:
        dictionary = {}
        for key in keys:
            if key in entry:
                dictionary[key] = entry[key]
            else:
                dictionary[key] = None

        results.append(dictionary)

    return results


def extract_data_and_common_keys(filename1, filename2):
    """
    Extract data from the files and find common keys.

    Args:-
        filename1(str) :- Name of file 1.
        filename2(str) :- Name of file 2.

    Return
        Data from both files and common keys.
    """
    with open(filename1, "r", encoding="utf-8") as f:
        csvreader = csv.DictReader(f)
        file1_data = list(csvreader)

    with open(filename2, "r", encoding="utf-8") as f2:
        csvreader = csv.DictReader(f2)
        file2_data = list(csvreader)

    common_keys = file1_data[0].keys() & file2_data[0].keys()

    return file1_data, file2_data, common_keys


def files_innerjoin(filename1, filename2):
    """
    Create a csv file with data from common keys.

    Args:-
        filename1(str) :- Name of file 1.
        filename2(str) :- Name of file 2.

    Return
        Data with common keys.
    """
    file1_data, file2_data, common_keys = extract_data_and_common_keys(
        filename1, filename2
    )

    data = create_dict_with_keys(file1_data, common_keys) + create_dict_with_keys(
        file2_data, common_keys
    )

    with open("results.csv", "w", encoding="utf-8") as results:
        csvwriter = csv.DictWriter(results, fieldnames=common_keys)
        csvwriter.writeheader()
        csvwriter.writerows(data)

    return data


def files_leftouterjoin(filename1, filename2):
    """
    Create a csv file with data from file1 and common keys in file2.

    Args:-
        filename1(str) :- Name of file 1.
        filename2(str) :- Name of file 2.

    Return
        Data from file1 and file2 with common keys.
    """
    file1_data, file2_data, common_keys = extract_data_and_common_keys(
        filename1, filename2
    )
    keys = file1_data[0].keys()

    file1_data += create_dict_with_keys(file2_data, keys)

    with open("results.csv", "w", encoding="utf-8") as results:
        csvwriter = csv.DictWriter(results, fieldnames=keys)
        csvwriter.writeheader()
        csvwriter.writerows(file1_data)

    return file1_data


def files_rightouterjoin(filename1, filename2):
    """
    Create a csv file with data from file2 and common keys in file1.

    Args:-
        filename1(str) :- Name of file 1.
        filename2(str) :- Name of file 2.

    Return
        Data from file2 and file1 with common keys.
    """
    file1_data, file2_data, common_keys = extract_data_and_common_keys(
        filename1, filename2
    )
    keys = file2_data[0].keys()

    file2_data += create_dict_with_keys(file1_data, keys)

    with open("results.csv", "w", encoding="utf-8") as results:
        csvwriter = csv.DictWriter(results, fieldnames=keys)
        csvwriter.writeheader()
        csvwriter.writerows(file2_data)

    return file2_data


def list_to_dict(data: list):
    """
    Convert list of dictionaries to dictionary of lists.

    Args:-
        data(list) :- List of dictionaries.

    Return
        Dictionaries of lists.
    """
    dictionary = {}

    for employee in data:
        for key, value in employee.items():
            if key in dictionary:
                dictionary[key] += [value]
            else:
                dictionary[key] = [value]

    return dictionary


def dict_to_list(data: dict):
    """
    Convert dictionary of lists to list of dictionaries.

    Args:-
        data(dict) :- Dictionary of lists.

    Return
        List of dictionaries.
    """
    n = len(data[list(data.keys())[0]])

    return [{key: value[i] for key, value in data.items()} for i in range(n)]


def split_file(filename, split_cols: list):
    """
    Split data from large csv files to separate csv files as per split_cols.

    Args:-
        filename(str) :- Name of file.
        split_cols(list) :- List of keys.
    """

    with open(filename, "r", encoding="utf-8") as f:
        csvreader = csv.DictReader(f)
        file_data = list(csvreader)

    cities = {data[split_cols[0]] for data in file_data}
    keys = file_data[0].keys() - split_cols

    for city in cities:
        married_list, unmarried_list = [], []

        married_city_filename = f"{city}" + "_married.csv"
        unmarried_city_filename = f"{city}" + "_unmarried.csv"

        for entry in file_data:
            dictionary = {}

            if city in entry[split_cols[0]]:
                for key in keys:
                    dictionary[key] = entry[key]

                if not "unmarried" in entry[split_cols[1]]:
                    married_list.append(dictionary)
                else:
                    unmarried_list.append(dictionary)

                with open(married_city_filename, "w", encoding="utf-8") as f:
                    csvwriter = csv.DictWriter(f, fieldnames=keys)
                    csvwriter.writeheader()
                    csvwriter.writerows(married_list)

                with open(unmarried_city_filename, "w", encoding="utf-8") as f:
                    csvwriter = csv.DictWriter(f, fieldnames=keys)
                    csvwriter.writeheader()
                    csvwriter.writerows(unmarried_list)

    return married_list, unmarried_list


if __name__ == "__main__":
    print(simple_interest(123456, 23, 0.08))
    print(compound_interest(123456, 23, 0.08))
    print(compound_interest_with_payments(0, 368970.52, 35, 0.10))
    print(savings_calculator(0, 1e8, 35, 0.10))
    print(files_innerjoin("sample1.csv", "sample2.csv"))
    print(files_leftouterjoin("sample1.csv", "sample2.csv"))
    print(files_rightouterjoin("sample1.csv", "sample2.csv"))
    print(list_to_dict([{"name": "a", "age": 21}, {"name": "b", "age": 43}]))
    print(dict_to_list({"name": ["a", "b"], "age": [21, 43]}))
    print(split_file("sample3.csv", ["city", "is_married"]))
