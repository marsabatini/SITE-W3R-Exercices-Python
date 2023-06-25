
# This program gets the effective group id, user id, real group id
# and a list of supplemental group ids associated with the current process.

import os

print("Group id:\t", os.getegid())
print("User id:\t", os.geteuid())
print("Real group id:", os.getgid())
print("List of supplemental group id:", os.getgroups())