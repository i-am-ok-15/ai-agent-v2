import os

def abs_working_path(working_directory):
    return os.path.abspath(working_directory)

def abs_target_path(working_directory, directory):
    return os.path.normpath(os.path.join((abs_working_path(working_directory)), directory))