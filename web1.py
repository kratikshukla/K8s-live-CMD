#!/usr/bin/python3

import cgi 
import subprocess

print("content-type: text/html")
print()

#print("Hii Kratik ")

f = cgi.FieldStorage()
cmd = f.getvalue("x")

o = subprocess.getoutput("sudo kubectl " + cmd + " --kubeconfig admin.conf")
print(o)
