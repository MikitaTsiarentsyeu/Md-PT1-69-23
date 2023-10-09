s = input()
symbol = input()
count = 0

while len(symbol)>1:
    symbol = input()

def count_symbols(string, symbol, count):
    if symbol in string:
        count = count + 1
        string = string.replace(symbol, '', 1)
        return count_symbols(string, symbol, count)
    
    return count

print(count_symbols(s, symbol, count))
