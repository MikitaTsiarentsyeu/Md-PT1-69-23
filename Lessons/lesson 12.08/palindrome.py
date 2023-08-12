def is_palindr(token):
    if len(token) < 1:
        return True
    if token[0] == token[-1]:
        return is_palindr(token[1:-1])
    else:
        return False
    
def is_palindr(token, start, end):
    if start >= end:
        return True
    if token[start] != token[end]:
        return False

    return is_palindr(token, start+1, end-1)

t = "tenet1"
print(is_palindr(t, 0, len(t)-1))