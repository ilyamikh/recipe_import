import sys
from os import listdir
import csv


def load_data(folder):
    """Loads all the .csv files in the specified folder and returns a dictionary"""
    raw_data = dict()
    for file in listdir(folder):
        path = folder + file
        key = file[:-4]  # remove file extension from the key name
        raw_data[key] = open(path)

    return raw_data


def get_list(reader):
    """Takes csv reader output and returns a list of rows"""
    csv_list = list()
    for row in reader:
        csv_list.append(row)

    return csv_list


def parse_rows(raw_dict):
    """Takes a dictionary and returns a dictionary with same key and a list as value"""
    parsed_dict = dict()
    for key in raw_dict:
        parsed_dict[key] = get_list(csv.reader(raw_dict[key]))

    return parsed_dict