import os

def create_environment() -> int:
    """
        creates folders and files to test the app 'manager'
        <current folder>\\test\\test.txt
        <current folder>\\test\\test1\\test.txt
        <current folder>\\test\\test1\\test2\\test.txt
    """    
    test_path = os.path.join(os.getcwd(), 'test')
    if os.path.exists(test_path):
        print(f'error: before running tests, you should clear the test environment by running the remove_environment() function')
        return -1
    else:
    	os.makedirs(os.path.join(test_path, 'test1', 'test2'))  

    filename = os.path.join(test_path, 'test.txt')
    if not os.path.isfile(filename):
        with open(filename, 'w') as f:
            f.write('Q' * 100)
    else:
        print(f'error: file <{filename}> already exists!')

    filename = os.path.join(test_path, 'test1', 'test.txt')
    if not os.path.isfile(filename):
        with open(filename, 'w') as f:
            f.write('Q' * 10000)
    else:
        print(f'error: file <{filename}> already exists!')

    filename = os.path.join(test_path, 'test1', 'test2',  'test.txt')
    if not os.path.isfile(filename):
        with open(filename, 'w') as f:
            f.write('Q' * 1000000)
    else:
        print(f'error: file <{filename}> already exists!')        
    return 0

def remove_environment(test_path = '') -> int:
    """
        removes test environment from current folder
    """    
    test_path = test_path if test_path else os.path.join(os.getcwd(), 'test')
    if os.path.exists(test_path):
        for item in os.listdir(test_path):
            local_path = os.path.join(test_path, item)
            if os.path.isdir(local_path):
                remove_environment(local_path)
            else:
                os.remove(local_path)
        os.rmdir(test_path)
        return 0
    else:
        print(f'test environment has already been removed')
        return -1