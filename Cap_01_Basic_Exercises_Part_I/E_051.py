
    # The program determines the profiling of Python programs.

    # Note
    # A profiles is a set of statics that describes how often
    # and for how long various parts of the program executed.
    # These  statistics can be formatted into reports via the
    # pstats module.


import cProfile

def sum():
    print(1 + 2)

cProfile.run('sum()')