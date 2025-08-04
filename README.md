# 4_hw_mipt_cli
## 4 homework for mipt python development: CLI

### 4.1 copy: copies the selected file to any folder
format:
manager.py copy -o <path/filename>	copies the file <filename> to the same folder with new file name <filename.copy>
manager.py copy -o <filename1> -t <filename2> copies the file <filename> to the same folder with new file name <filename2>
manager.py copy -o <filename1> -t <path> copies the file <filename> to custom folder <path> with new file name <filename.copy>
manager.py copy -o <filename1> -t <path/filename2> copies the file <filename> to custom folder <path> with new file name <filename2>

### 4.2 rmfile: deletes the selected file
format:
manager.py rmfile -o <path/filename>