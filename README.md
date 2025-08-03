# 4_hw_mipt_cli
## 4 homework for mipt python development: CLI
### 4.1 copy: copies one file to any folder
format:
copy -o <path/filename>	copies the file <filename> to the same folder with new file name <filename.copy>
copy -o <filename1> -t <filename2> copies the file <filename> to the same folder with new file name <filename2>
copy -o <filename1> -t <path> copies the file <filename> to custom folder <path> with new file name <filename.copy>
copy -o <filename1> -t <path/filename2> copies the file <filename> to custom folder <path> with new file name <filename2>