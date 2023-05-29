FILEPATH = 'todos.txt'


def get_todos(file_path=FILEPATH):
    """ Read a text file and return the list of
    to-do items
    """
    with open(file_path, 'r') as local_file:
        return local_file.readlines()


def write_todos(todos_arg, file_path=FILEPATH):
    """ Write the to-do items list in the text file"""
    with open(file_path, 'w') as local_file:
        local_file.writelines(todos_arg)


if __name__ == '__main__':
    print(get_todos(r'..\todos.txt'))
