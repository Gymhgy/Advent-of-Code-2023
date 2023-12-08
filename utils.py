import re
import subprocess

def ints(st):
    return [int(i) for i in re.findall('\d+', st)]

def ans(obj):
    cmd='echo '+str(obj).strip()+'|clip'
    subprocess.check_call(cmd, shell=True)
    return obj