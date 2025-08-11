# **4_hw_mipt_cli**
## 4 homework for mipt python development: CLI

### 4.1 file manager for console
### 4.1.1 copy: copies the selected file to any folder
format (run from console):  
    python manager.py copy -o <filename>	copies the file <filename> to the same folder with new file name <filename.copy>  
    python manager.py copy -o <filename1> -t <filename2> copies the file <filename> to the same folder with new file name <filename2>  
    python manager.py copy -o <filename1> -t <path> copies the file <filename> to custom folder <path> with new file name <filename.copy>  
    python manager.py copy -o <filename1> -t <path\filename2> copies the file <filename> to custom folder <path> with new file name <filename2>  
### 4.1.2 rmfile: deletes the selected file 
format (run from console):
    python manager.py rmfile -o <path\filename> deletes the file <filename> from custom folder
    python manager.py rmfile -o <filename> deletes the file <filename> from current folder
### 4.1.3 rmfolder: deletes the selected folder  
format (run from console):  
    python manager.py rmfile -o <path> deletes the folder <path>; can be used relative or absolute path to the directory

### 4.1.4 analyze: displays the selected folder structure and size, or file size 
format (run from console):
    python manager.py analize -o <path>; can be used relative or absolute path to the file or directory

### 4.2 test environment (for tests only)  
### 4.2.1 create_environment():
creates folders and files in the current directory for running tests
### 4.2.2 remove_environment():
removes test environment

### 4.3 tests for manager features using test environment 
	- copy file feature tests
	- delete file feature tests
	- delete folder feature tests
	- analyze folder feature tests
format (run from console):
python tests.py
