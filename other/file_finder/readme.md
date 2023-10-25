Idea based on [this tutorial](https://www.pythonforbeginners.com/systems-programming/os-walk-and-fnmatch-in-python/)

### What does this script do:
Search all files with given pattern (in file name) from given path

### How to use it:
1. Make sure, you have all dependencies requirements by this script - you can use requirements.txt file,
but that assume you to use conda. 

2. Run a script - program will ask you to specify start_path (path from where you want to start search) and
pattern (which one you want to search for) - please look for table right up on [fnmatch docs](https://docs.python.org/3/library/fnmatch.html)
to check valid symbols in pattern.

    ```
    python file_finder.py
   ```