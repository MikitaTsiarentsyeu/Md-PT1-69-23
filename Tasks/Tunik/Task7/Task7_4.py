import time
def main(func): 
    def wrapper(*args):
        with open('TextFileFor4.txt','w') as file:
            start = time.time()
            end = time.time()
            values = func(*args)
            global total_time
            total_time = end - start
            file.write(f"Execution time - {total_time}\nAll values - {args}\nResult - {values}")
            return values
    return wrapper

@main
def sum(x,y):
    return x+y
result = sum(8,10)


  
