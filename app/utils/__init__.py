from pathlib import Path


def get_project_root():
    return Path(__file__).parent.parent.parent


def print_dict(my_dict):
    for key, value in my_dict.items():
        print(f'{key}: {value}')


def print_dicts(my_dicts, sep='-', amount=20):
    for my_dict in my_dicts:
        print_dict(my_dict)
        print(sep * amount)


if __name__ == '__main__':
    print(get_project_root())