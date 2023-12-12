import re
import subprocess

def ints(st):
    return [int(i) for i in re.findall('-?\d+', st)]

def ans(obj):
    cmd='echo '+str(obj).strip()+'|clip'
    subprocess.check_call(cmd, shell=True)
    return obj

def neighbors4(x, y):
    return (x+1, y), (x, y+1), (x-1, y), (x, y-1)

def neighbors8(x, y):
    return (x+1, y), (x, y+1), (x-1, y), (x, y-1), (x+1, y+1), (x-1, y+1), (x-1, y-1), (x+1, y-1)