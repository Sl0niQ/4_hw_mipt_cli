# **4_hw_mipt_cli**
# 4 homework for mipt python development: CLI

## 4.1 file manager for console  
### 4.1.1 copy: 
copies file "filename" to the same folder with new file name "filename.copy":
```bash
python manager.py copy -o {filename}
```
copies file "filename1" to the same folder with new file name "filename2":  
```
python manager.py copy -o {filename1} -t {filename2}
```
copies file "filename" to custom folder "path" with file name "filename":  
```
python manager.py copy -o {filename} -t {path}
```
copies file "filename1" to custom folder "path" with new file name "filename2":
```
python manager.py copy -o {filename1} -t {path\filename2}
``` 
### 4.1.2 rmfile: 
deletes file "filename" from custom folder:
```
python manager.py rmfile -o {path\filename}
```
deletes file "filename" from current folder:
```
python manager.py rmfile -o {filename}
```
### 4.1.3 rmfolder:
deletes folder "path" (relative or absolute path to the directory can be used):
```
python manager.py rmfile -o {path}
```
### 4.1.4 analyze: 
displays structure and size of selected folder, or file size (relative or absolute path to the file or directory can be used):
```
python manager.py analyze -o {path}
```
### 4.2 test environment (for tests only)  
#### 4.2.1 create_environment():  
creates folders and files in the current directory for running the tests  
#### 4.2.2 remove_environment():  
removes test environment  
### 4.3 tests for manager features using test environment  
- copy file feature tests  
- delete file feature tests  
- delete folder feature tests  
- analyze folder feature tests  
```
python tests.py
```