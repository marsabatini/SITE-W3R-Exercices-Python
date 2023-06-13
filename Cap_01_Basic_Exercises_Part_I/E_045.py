
    # This program calls an external command


from subprocess import call
import os
import psutil

#Method 01
print("Method 01")
call(['ls', '-l'])


#Method 02
print("\nMethod 02")
print(os.system('ls -l'))


#Method 03
print("\nMethod 03")
print(psutil.cpu_count())