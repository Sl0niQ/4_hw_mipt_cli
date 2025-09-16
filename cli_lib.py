import os

#(легкое) команда которая позволяет копировать файл 
def cross_platform_copy(copy_from, copy_to):
    """
        low level copy for different os
    """
    if os.name == "nt":
        print(f'cp "{copy_from}" "{copy_to}"')
        os.system(f'copy "{copy_from}" "{copy_to}"')
    else:
        print(f'cp "{copy_from}" "{copy_to}"')
        os.system(f'cp "{copy_from}" "{copy_to}"')

def copy_file(args):
    """
       copies a file
       python manager.py copy -o <filename> [-t <filename>] 
    """      
    if args.origin:
        if os.path.isfile(args.origin):
            if not os.path.basename(args.target):
                target_filename = os.path.basename(args.origin)                
                args.target = target_filename               
            else:
                target_filename = os.path.basename(args.target)
            target_directory = os.path.dirname(os.path.abspath(args.target))           
            if os.path.isdir(target_directory):                
                args.target = os.path.join(target_directory, target_filename)
                copy_number = 1
                while os.path.isfile(args.target):
                    args.target = os.path.join(target_directory, f"{target_filename}.copy({copy_number})")
                    copy_number += 1                
                #os.system(f"copy {args.origin} {args.target}")
                cross_platform_copy(args.origin, args.target)
            else:
                print(f"error: folder {target_directory} does not exist")
                return -1
        else:
            print(f"error: file {args.origin} does not exist")
            return -1
    else:
        print("error: <file name> missing")
        return -1
    return 0   

#(легкое) команда которая удаляет папку 
def remove_folder(args):
    """
        deletes a folder
        python manager.py rmfold -o <path>
    """   
    if args.origin:
        try:
            folder = os.path.abspath(args.origin)
            if os.path.isdir(folder):                        
                for item in os.listdir(folder):
                    local_path = os.path.join(folder, item)
                    if os.path.isdir(local_path):
                        args.origin = local_path
                        remove_folder(args)
                    else:
                        os.remove(local_path)
                os.rmdir(folder)            
                return 0
            else:
                print(f"error: folder <{args.origin}> does not exist")
                return -1

        except PermissionError:
            print(f"error: permission denied for folder <{args.origin}>")
            return -1
        
        except OSError as e:
            print(f"error: cannot delete folder <{args.origin}> - {e}")
            return -1
            
        except Exception as e:
            print(f"unexpected error: {e}")
            return -1

    else:
        print("error: <folder name> missing")
        return -1

#(легкое) команда которая удаляет файл 
def remove_file(args):
    """
        deletes a file
        python manager.py rmfile -o <filename>
    """    
    try:
            if os.path.isfile(args.origin):
                os.remove(args.origin)
                print(f"file {args.origin} has been deleted")
                return 0
            else:
                print(f"error: file <{args.origin}> does not exist")
                return -1
                
    except PermissionError:
        print(f"error: permission denied to delete file <{args.origin}>")
        return -1
            
    except OSError as e:
        print(f"error: cannot delete file <{args.origin}> - {e}")
        return -1
            
    except Exception as e:
        print(f"unexpected error: {e}")
        return -1

    else:
        print("error: <file name> missing")
        return -1 

def folder_size(fpath):
    """
        calculates folder size
    """
    total_size = 0
    for item in os.listdir(fpath):
        item_path = os.path.join(fpath, item)
        if os.path.isdir(item_path):                
            total_size += folder_size(item_path)
        else:
            total_size += os.path.getsize(item_path)
    return total_size  

#(сложное) команда запускающая анализ всех вложенных папок и файлов, и выводящая информацию о том насколько 
#большие файлы находятся на уровне вызова. Способ вывода любой (но только через консоль), например: manager analyse
def analyze(args):
    """
        analyzes the folder structure
        python manager.py analyze -o <path>
    """
    if args.origin:
        if os.path.exists(args.origin):
            full_path = os.path.abspath(args.origin)
            if os.path.isdir(full_path):
                print(f"{os.path.basename(full_path)}")
                total_size = 0
                for item in os.listdir(full_path):
                    local_path = os.path.join(full_path, item)

                    try:
                        if os.path.isdir(local_path):
                            fold_size = folder_size(local_path)
                            object_name = os.path.basename(local_path)
                            object_name = f"{object_name[:18]}.." if len(object_name) > 20 else object_name
                            print(f"  {object_name:<20} {'<dir>':<5} {fold_size:>16} bytes")
                            total_size += fold_size
                        else:
                            file_size = os.path.getsize(local_path)
                            object_name = os.path.basename(local_path)
                            object_name = f"{object_name[:18]}.." if len(object_name) > 20 else object_name
                            print(f"  {object_name:<26} {file_size:>16} bytes")
                            total_size += file_size
                    except (PermissionError, OSError) as e:
                        print(f"  {item[:20]:<20} {'<error>':<5} {'N/A':>16}")
                        continue

                print(f"{'-' * 51}\ntotal {' ' * 22} {total_size:>16} bytes")
            else:
                print(f"{os.path.basename(full_path):<27} {os.path.getsize(full_path):>16} bytes")          
            return 0
        else:
            print(f"error: file or folder <{args.origin}> does not exist")
            return -1
    else:
        print("error: <file or folder name> missing")
        return -1

#dictionary of valid actions
actions = {
    "copy": copy_file,
    "rmfold": remove_folder,
    "rmfile": remove_file,
    "analyze": analyze
}