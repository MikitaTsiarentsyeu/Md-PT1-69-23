potential_float = "-1.23"

# print(potential_float.isdigit())

# print(potential_float.count('.'))

# potential_float = potential_float.replace('.', '')
# print(potential_float)

minus = False
if potential_float.count('.')==1 and potential_float[0] == '-':
    potential_float = potential_float.replace('-', '')
    minus = True

if potential_float.isdigit() or (potential_float.count('.')==1 and potential_float.replace('.', '').isdigit()):
    f = float(potential_float)
    if minus:
        f = -f
    print(type(f))

potential_float = "1.23"

isValid = False

if not potential_float.isdigit():
    parts = potential_float.split('.')
    print(parts)
    if len(parts) == 2:
        if parts[0].isdigit() and parts[1].isdigit():
            isValid = True
else:
    isValid = True
    
if isValid:
    potential_float = float(potential_float)
else:
    print("wrong format")