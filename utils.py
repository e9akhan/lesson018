"""
    Module name :- utils.py
    Method(s) :- formatting(number),
    simple_interest(principal, time, rate),
    compound_interest(principal, time, rate),
    compound_interest_with_payments(principal, payment, term, rate, end_of_period=False),
    savings_calculator(present_value, future_value, term, rate, end_of_period=True),
    check(data1, data2, **kwargs),
    join(file1_data, file2_data, **kwargs),
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


def check(data1, data2, **kwargs):
    """
    Check whether the key is present in both data.

    Args:-
        data1(list) :- Data from file 1.
        data2(list) :- Data from file 2.
        **kwargs(dict) :- keys

    Return
        data if key is present else False
    """
    for key in kwargs.values():
        if data1[key.lower()] != data2[key.lower()]:
            return False

    return data1, data2


def join(file1_data, file2_data, **kwargs):
    """
    Perform join operation on file1_data and file2_data.

    Args:-
        file1_data(list) :- Data from file 1.
        file2_data(list) :- Data from file 2.

    Return
        file1_data(list) :- Modified data of File 1.
        data_list(list) :- Common data
        keys(list) :- common keys.
    """
    for key in kwargs.values():
        if (
            key.lower() not in file1_data[0].keys()
            or key.lower() not in file2_data[0].keys()
        ):
            return None

    data_list = []

    for data1 in file1_data:
        for data2 in file2_data:
            if check(data1, data2, **kwargs):
                data1.update(data2)
                data_list.append(data1)

    return file1_data, data_list, data_list[0].keys()


def files_innerjoin(filename1, filename2, **kwargs):
    """
    Create a csv file with data from common keys.

    Args:-
        filename1(str) :- Name of file 1.
        filename2(str) :- Name of file 2.

    Return
        Data with common keys.
    """
    if not kwargs:
        return None

    with open(filename1, "r", encoding="utf-8") as f1:
        csvreader = csv.DictReader(f1)
        file1_data = list(csvreader)

    with open(filename2, "r", encoding="utf-8") as f2:
        csvreader = csv.DictReader(f2)
        file2_data = list(csvreader)

    output = join(file1_data, file2_data, **kwargs)

    if not output:
        return None

    with open("result.csv", "w", encoding="utf-8") as result:
        csvwriter = csv.DictWriter(result, fieldnames=output[2])
        csvwriter.writeheader()
        csvwriter.writerows(output[1])

    return output[1]


def files_leftouterjoin(filename1, filename2, **kwargs):
    """
    Create a csv file with data from file1 and common keys in file2.

    Args:-
        filename1(str) :- Name of file 1.
        filename2(str) :- Name of file 2.

    Return
        Data from file1 and file2 of common keys.
    """
    if not kwargs:
        return None

    with open(filename1, "r", encoding="utf-8") as f1:
        csvreader = csv.DictReader(f1)
        file1_data = list(csvreader)

    with open(filename2, "r", encoding="utf-8") as f2:
        csvreader = csv.DictReader(f2)
        file2_data = list(csvreader)

    output = join(file1_data, file2_data, **kwargs)

    if not output:
        return None

    with open("result.csv", "w", encoding="utf-8") as result:
        csvwriter = csv.DictWriter(result, fieldnames=output[2])
        csvwriter.writeheader()
        csvwriter.writerows(output[0])

    return output[0]


def files_rightouterjoin(filename1, filename2, **kwargs):
    """
    Create a csv file with data from file2 and common keys in file1.

    Args:-
        filename1(str) :- Name of file 1.
        filename2(str) :- Name of file 2.

    Return
        Data from file2 and file1 of common keys.
    """
    if not kwargs:
        return None

    with open(filename1, "r", encoding="utf-8") as f1:
        csvreader = csv.DictReader(f1)
        file1_data = list(csvreader)

    with open(filename2, "r", encoding="utf-8") as f2:
        csvreader = csv.DictReader(f2)
        file2_data = list(csvreader)

    output = join(file2_data, file1_data, **kwargs)

    if not output:
        return None

    with open("result.csv", "w", encoding="utf-8") as result:
        csvwriter = csv.DictWriter(result, fieldnames=output[2])
        csvwriter.writeheader()
        csvwriter.writerows(output[0])

    return output[0]


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
    print(files_innerjoin("sample1.csv", "sample2.csv", key="Name"))
    print(files_leftouterjoin("sample1.csv", "sample2.csv", key="Name"))
    print(files_rightouterjoin("sample1.csv", "sample2.csv", key="Name"))
    print(list_to_dict([{"name": "a", "age": 21}, {"name": "b", "age": 43}]))
    print(dict_to_list({"name": ["a", "b"], "age": [21, 43]}))
    print(split_file("sample3.csv", ["city", "is_married"]))
