"""
V1.py
Reconnaissance script:
- Scans the current directory for Python (.py) files.
- Outputs the filenames into V1.txt (one per line).
"""

import os

def find_python_files():
    py_files = []
    for filename in os.listdir('.'):
        if filename.endswith('.py') and filename != 'V1.py':  
            py_files.append(filename)
    return py_files

def main():
    py_files = find_python_files()
    
    with open("V1.txt", "w") as outfile:
        for f in py_files:
            outfile.write(f + "\n")

if __name__ == "__main__":
    main()
