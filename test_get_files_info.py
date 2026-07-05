from functions.get_file_info import get_file_info

def test_get_file_info():
    print(get_file_info("calculator", "."))
    print(get_file_info("calculator", "/bin"))
    print(get_file_info("calculator", "../"))
    print(get_file_info("calculator", "main.py"))

test_get_file_info()