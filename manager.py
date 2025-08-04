#ma
import argparse
import os

#print(globals().get('origin', 'Не найдено'))  # Поиск в глобальных переменных
#print(locals().get('origin', 'Не найдено'))  # Поиск в локальных переменных

#(легкое) команда которая позволяет копировать файл 
#(пример использования: manager copy test.txt)
def copy_file(args):
    """
       Copies a file 
    """      
    if args.origin:
        if os.path.isfile(args.origin):
            if not os.path.basename(args.target):
                target_filename = os.path.basename(args.origin)
            else:
                target_filename = os.path.basename(args.target)
            target_directory = os.path.dirname(args.target)
            if os.path.isdir(target_directory):                
                args.target = os.path.join(target_directory, target_filename)
                copy_number = 1
                while os.path.isfile(args.target):
                    args.target = os.path.join(target_directory, f'{target_filename}.copy({copy_number})')
                    copy_number += 1                
                os.system(f"copy {args.origin} {args.target}")
            else:
                print(f'error: folder {target_directory} does not exist')
                return -1
        else:
            print(f'error: file {args.origin} does not exist')
            return -1
    else:
        print('error: <file name> missing')
        return -1
    return 0   

#(легкое) команда которая удаляет папку 
#(пример использования: manager delete folder_name)
def remove_folder(args):
    if os.path.isdir(origin_directory):
        folder = os.path.dirname(args.target)
        for item in os.listdir(folder):
            pass
            #if 
        print('remove_folder')
        return 0
    else:
        print(f'error: folder {target_directory} does not exist')
        return -1
    

#(легкое) команда которая удаляет файл 
#(пример использования: manager delete file_name)
def remove_file(args):
    """
        Deletes a file
    """
    print(f'args = {args}')
    if args.origin:
        if os.path.isfile(args.origin):
            os.remove(args.origin)
            return 0
        else:
            print(f'error: file <{args.origin}> does not exist')
            return -1
    else:
        print('error: <file name> missing')
        return -1 

def analyze(args):
    print('analyze')

#dictionary of valid actions
actions = {
    "copy": copy_file,
    "rmfold": remove_folder,
    "rmfile": remove_file,
    "analyze": analyze
}

#parser object to get args from the cli
parser = argparse.ArgumentParser(
                 prog = 'file manager',
                 description = 'allows you to perform some actions with a file',
                 epilog = 'examples:\n manager copy <file_name>'
)

#manager arguments declaring
parser.add_argument('action', type = str, help = 'allowed action')
parser.add_argument('--origin', '-o', type = str, default = '', help = 'original file name or path')
parser.add_argument('--target', '-t', type = str, default = '', help = 'target file name or path')

args = parser.parse_args()

#valid function call
if args.action in actions:   
    actions[args.action](args)  
else:
    print('error: unknown argument <action>')

#parser.add_argument("--output", "-o", default="out.txt", help="Выходной файл")
#parser.add_argument("--mode", choices=["fast", "slow"], default="fast")

#if not all([args.action, args.file_name]):
#    parser.print_help()
#    sys.exit(1)

#current_dir = os.getcwd()