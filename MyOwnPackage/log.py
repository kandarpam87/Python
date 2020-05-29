from datetime import datetime


def print_log(s="", type="Info"):
    print(datetime.now(), " | ", __name__, " | ", type, " | ", s)

def print_info(s):
    print_log(s, "Info")

def print_warn(s):
    print_log(s, "Warn")

def print_error(s):
    print_log(s, "Error")

def print_seperator(c='-', count=40):
    print(c*count)

if(__name__ == '__main__'):
    print_error("Error Message")
    print_seperator()
    print_warn("Warning Message")
    print_seperator()
    print_info("Info Message")
