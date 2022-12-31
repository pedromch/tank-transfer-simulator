import pandas as pd
from numpy import int64, float64
from os import path
from constants import *
from utils import get_pipe_fitting_options_file_path

def validate(h1, h2, rho, mi, Di, L, eps, pipe_fittings, pump_curve_file_path):
    check_all_number(h1, h2, rho, mi, Di, L, eps)
    check_all_positive(rho, mi, Di, L)
    check_all_higher_or_equal_to_value(eps, value=0)
    validate_pipe_fitting(pipe_fittings)
    validate_pump_curve(pump_curve_file_path)


def check_all_positive(*args):
    for item in args:
        if item <= 0:
            raise Exception(f"{item} is invalid. A positive number was expected.")


def check_all_higher_or_equal_to_value(*args, value):
    for item in args:
        if item < value:
            raise Exception(f"{item} is invalid. A number higher or equal than {value} was expected.")


def check_all_number(*args):
    for item in args:
        if type(item) not in (float, int):
            raise Exception(f"{type(item)} is invalid. A number was expected.")


def is_valid_list(value, empty_is_valid = False):
    is_list = type(value) == list
    if not is_list:
        raise Exception(f"{type(value)} is invalid. A list was expected.")
    
    is_empty = len(value) == 0
    if is_empty and not empty_is_valid:
        raise Exception("The list can't be empty.")

    
def check_is_valid_dict(value, empty_is_valid = False):
    is_dict = type(value) == dict
    if not is_dict:
        raise Exception(f"{type(value)} is invalid. A dict was expected")
    
    is_empty = len(value) == 0
    if is_empty and not empty_is_valid:
        raise Exception("The dict can't be empty.")

    
def check_is_valid_str(value, empty_is_valid = False):
    is_str = type(value) == str
    if not is_str:
        raise Exception(f"{type(value)} is invalid. A string was expected")
    
    is_empty = len(value) == 0
    if is_empty and not empty_is_valid:
        raise Exception("The string can't be empty.")
    
    
def validate_pipe_fitting(pipe_fittings):
    
    check_is_valid_dict(pipe_fittings, True)
    
    file_path = get_pipe_fitting_options_file_path()
    
    options = pd.read_csv(file_path).id.values

    for key, value in pipe_fittings.items():
        
        check_all_number(value)
        
        check_all_positive(value)
        
        if not key in options:
            raise Exception(f"Invalid key in pipe fittings. Choose types based on the {ASSETS_FOLDER_NAME}/{PIPE_FITTINGS_OPTIONS_FILE_NAME}.")


def check_file_path_exists(file_path):
    if not path.exists(file_path):
        raise Exception(f"The file path '{file_path}' does not exist.")
    

def check_extension(file_path, extension):
    if file_path.split(".")[-1] != extension:
        raise Exception(f"The file path '{file_path}' is invalid. A .{extension} file was expected.") 
        
        
def validate_pump_curve(pump_curve_file_path):
    
    check_is_valid_str(pump_curve_file_path)
    
    check_file_path_exists(pump_curve_file_path)
    
    check_extension(pump_curve_file_path, "csv")
    
    pump_curve_df = pd.read_csv(pump_curve_file_path)
    columns_name = pump_curve_df.columns.values.tolist() 

    if columns_name != [PUMP_CURVE_HEAD_COLUMN_NAME, PUMP_CURVE_VOLUMETRIC_FLOW_COLUMN_NAME]:
        raise Exception(f"The '{path.basename(pump_curve_file_path)}' file does not match the template structure in {ASSETS_FOLDER_NAME}/{PUMP_CURVE_TEMPLATE_FILE_NAME}.")
    
    for column_name in columns_name:
        column = pump_curve_df[column_name]
        if len(column) < 3:
            raise Exception("At least three data points are needed for the pump curve.")
        
        column_type = column.dtype
        if column_type not in (int64, float64):
            raise Exception(f"{column_type} data type is invalid. Only numbers are accepted as pump curve data. Check if all data entries are numbers without surrounding quotes and with a dot as the decimal separator if applicable.")
        
    all_columns_have_the_same_length = len(set((pump_curve_df.count().values))) == 1
    if not all_columns_have_the_same_length:
        raise Exception(f"All columns of '{path.basename(pump_curve_file_path)}' need to have the same length.")


if __name__ == "__main__":
    # print(is_positive(1, 2, 3, 4.5))
    # print(is_positive('1', 2, 4))
    # print(is_positive(-1, 4, 6))
    # print(is_valid_list([], False))
    # validate([1,24,5], {3:4},'')
    # validate_pipe_fitting({})
    validate_pump_curve(r'c:\Users\pedro.machado\Desktop\project_1\assets\pump_curve_test.csv')