import os

current_path = os.getcwd() ###current_path?
test_path = os.path.join(current_path, 'test1')
if os.path.exists(test_path):
	print(f'error: before running tests, you should delete the directory {test_path}')
else:
	os.makedirs(os.path.join(test_path, 'test2', 'test3'))  

filename = os.path.join(test_path, 'test.txt')
if not os.path.isfile(filename):
    with open(filename, 'w') as f:
        f.write('')
else:
    print(f'error: file <{filename}> already exists!')

### Доделать создание тестового окружения - создать еще один файл (ненулевой)
### сделать очистку тестового окружения
### обернуть в функции