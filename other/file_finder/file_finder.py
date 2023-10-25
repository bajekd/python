import os
import fnmatch

start_path = input("Please provide start_path, where you want to start searching: ")
pattern = input("Please provide pattern via which you want to search: ")
for path, dirs, files in os.walk(start_path):
    for filename in fnmatch.filter(files, pattern):
        print(os.path.join(path, filename))
