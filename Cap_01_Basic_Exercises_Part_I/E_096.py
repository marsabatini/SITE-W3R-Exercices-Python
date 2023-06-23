
# This program prints th current call stack.

import traceback

def f1():
    return abc()

def abc():
    traceback.print_stack()

f1()