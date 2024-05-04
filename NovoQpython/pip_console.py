# qpy:console
import os
import sys

# A função input é uma função embutida do Python, não precisa ser importada de outro lugar


def modcmd(arg):
    os.system(sys.executable + " " + sys.prefix + "/bin/" + arg)


if not os.path.exists(sys.prefix + "/bin/pip"):
    print("You need to install pip first.")
print("Input pip commands, ie: pip install {module}")
while True:
    cmd = input("-->")
    if cmd == "":
        break
    modcmd(cmd)
