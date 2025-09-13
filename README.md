# **4_hw_mipt_cli**
## 4 homework for mipt python development: CLI

### 4.1 file manager for console  
#### 4.1.1 copy: copies selected file to any folder  
**format** (run from console)  
copies file "filename" to the same folder with new file name "filename.copy":  
_  python manager.py copy -o {filename}_  
copies file "filename1" to the same folder with new file name "filename2":  
_- python manager.py copy -o {filename1} -t {filename2}_  
copies file "filename" to custom folder "path" with file name "filename":  
    _python manager.py copy -o {filename} -t {path}_  
copies file "filename1" to custom folder "path" with new file name "filename2":
```python manager.py copy -o {filename1} -t {path\filename2}
``` 
#### 4.1.2 rmfile: deletes selected file  
format (run from console)  
    deletes file "filename" from custom folder:  
    _python manager.py rmfile -o {path\filename}_  
    deletes file "filename" from current folder:  
    _python manager.py rmfile -o {filename}_  
#### 4.1.3 rmfolder: deletes selected folder  
format (run from console)  
    deletes folder "path" (relative or absolute path to the directory can be used):  
    _python manager.py rmfile -o {path}_  
#### 4.1.4 analyze: displays the selected folder structure and size, or file size  
format (run from console)  
    relative or absolute path to the file or directory can be used:  
    _python manager.py analyze -o {path}_  
### 4.2 test environment (for tests only)  
#### 4.2.1 create_environment():  
creates folders and files in the current directory for running tests  
#### 4.2.2 remove_environment():  
removes test environment  
### 4.3 tests for manager features using test environment  
	- copy file feature tests  
	- delete file feature tests  
	- delete folder feature tests  
	- analyze folder feature tests  
format (run from console):  
    _python tests.py_  