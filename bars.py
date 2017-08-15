import json
import os
import math


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='cp866') as file_handler:
        return json.load(file_handler)


def validate_data(loaded_data, longitude, latitude):
    validate_error = 0
    if loaded_data is None:
        validate_error = 1
        print('Wrong filepath or wrong filename')
    try:
        latitude = float(latitude)
        longitude = float(longitude)
    except ValueError:
        validate_error = 1
        print('Wrong latitude or longitude')
    if not validate_error:
        return 1


def get_seats_count_and_name(loaded_data):
    seats_and_name = [
        (datas.get("SeatsCount"), datas.get("Name"))for datas in loaded_data]
    return seats_and_name


def get_biggest_bar(seats_and_name):
    return max(seats_and_name)[1]


def get_smallest_bar(seats_and_name):
    return min(seats_and_name)[1]


def get_closest_bar(loaded_data, longitude, latitude):
    coord_diff_and_name = [
        ((math.fabs(float(datas.get("Longitude_WGS84")))- float(longitude))
        + (math.fabs(float(datas.get("Latitude_WGS84")))- float(latitude)), 
        datas.get("Name")) for datas in loaded_data
    ]
    return min(coord_diff_and_name)[1]


if __name__ == '__main__':
    _filepath = input('Enter filepath to file: ')
    _longitude = input('Enter current longitude: ')
    _latitude = input('Enter current latitude: ')
    _data = load_data(_filepath)
    _validate_data = validate_data(_data, _longitude, _latitude)
    if _validate_data:
        _seats_count_and_name = get_seats_count_and_name(_data)
        _output = (
            (get_biggest_bar(_seats_count_and_name)),
            (get_smallest_bar(_seats_count_and_name)),
            (get_closest_bar(_data, _longitude, _latitude))
            )
        print('Biggest, smallest and closest bar: ')
        print(', '.join(_output))
