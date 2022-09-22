import sys
import re
from subprocess import check_output

def banner():
    print(""".oPYo.        8
8    8        8
8      .oPYo. 8 .oPYo.
8      .oooo8 8 8    '
8    8 8    8 8 8    .
`YooP' `YooP8 8 `YooP'

""")

def filter(exp):
    r = re.compile(r"[A-Za-z\s|;#]") # secure enough right?
    if r.search(exp) is not None:
        return False
    else:
        return True

def calc(exp):
    if filter(exp):
        cmd = "echo " + exp + " | bc"
        res = check_output(cmd, shell=True, executable='/bin/bash')
        return res.decode().strip()
    else:
        return "No hacker allowed."

def main():
    exp = input("Math Expression: ")
    res = calc(exp)
    cmd = "bash -c 'echo -n $((" + exp + "))'"
    # print(cmd)
    print(res)
    sys.exit()

if __name__ == "__main__":
    banner()
    main()
