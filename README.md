# **4_hw_mipt_cli**
## 4 homework for mipt python development: CLI

### 4.1 file manager
### 4.1.1 copy: copies the selected file to any folder
format:
manager.py copy -o <filename>	copies the file <filename> to the same folder with new file name <filename.copy>  
manager.py copy -o <filename1> -t <filename2> copies the file <filename> to the same folder with new file name <filename2>  
manager.py copy -o <filename1> -t <path> copies the file <filename> to custom folder <path> with new file name <filename.copy>  
manager.py copy -o <filename1> -t <path\filename2> copies the file <filename> to custom folder <path> with new file name <filename2>  
### 4.1.2 rmfile: deletes the selected file 
format:
manager.py rmfile -o <path\filename> deletes the file <filename> from custom folder
manager.py rmfile -o <filename> deletes the file <filename> from current folder
### 4.1.3 rmfolder: deletes the selected folder  
format:
manager.py rmfile -o <path> deletes the folder <path>; can be used relative or absolute path to the directory

### 4.2 test environment (for running tests only)  
### 4.2.1 create_environment(): 
creates folders and files in the current directory for running tests
### 4.2.2 remove_environment(): 
removes test environment