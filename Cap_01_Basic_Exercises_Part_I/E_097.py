
# The code lists the special variables used in the language.

varNames = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ name i'.split()))
print()
print('\n'.join(' '.join(varNames[i: i + 8]) for i in range(0, len(varNames), 8)))