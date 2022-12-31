import pandas as pd
from numpy import pi
from os import path
from constants import ASSETS_FOLDER_NAME, PIPE_FITTINGS_OPTIONS_FILE_NAME

def get_pipe_fitting_options_file_path():
    parent_dir = path.dirname(path.dirname(__file__))
    file_path = path.abspath(path.join(parent_dir, ASSETS_FOLDER_NAME, PIPE_FITTINGS_OPTIONS_FILE_NAME))
    return file_path


def get_csv_as_dict(filepath):
    df = pd.read_csv(filepath)
    return {column_name: df[column_name].to_numpy() for column_name in df.columns.values.tolist()}


def get_circle_area(D):
    return pi*D**2/4

def per_hour_to_per_second(value):
    return value/3600

def per_second_to_per_hour(value):
    return value*3600