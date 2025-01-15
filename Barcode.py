from subprocess import Popen, PIPE
import subprocess
import sys,os
def bar_code_recog_fn(inp_img):
    command = ["ZBar/bin/zbarimg.exe","-q",inp_img]
    DETACHED_PROCESS = 0x00000008
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess._subprocess.STARTF_USESHOWWINDOW
    proc=subprocess.Popen(command,stderr=subprocess.PIPE, stdout=subprocess.PIPE,creationflags=DETACHED_PROCESS)
    output=proc.communicate(input=None)
    return output[0]
