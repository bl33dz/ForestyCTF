import sys
import re
from subprocess import check_output, DEVNULL

def banner():
    print(""".oPYo.        8
8    8        8
8      .oPYo. 8 .oPYo.
8      .oooo8 8 8    '
8    8 8    8 8 8    .
`YooP' `YooP8 8 `YooP' - version 2.0

""")

def filter(exp):
    r = re.compile(r"[A-Za-z\s|;#=]") # secure enough right?
    if r.search(exp) is not None:
        return False
    else:
        return True

def calc(exp):
    if filter(exp):
        cmd = ["echo -ne 'scale=2; " + exp + "\n' | bc -l"]
        res = check_output('\n'.join(cmd), shell=True, executable='/bin/bash', stderr=DEVNULL)
        return res.decode().split('\n')[0] # no directory listing for you
    else:
        return "No hacker allowed."

def main():
    exp = input("Math Expression: ")
    res = calc(exp)
    print(res)
    sys.exit()

if __name__ == "__main__":
    banner()
    main()
