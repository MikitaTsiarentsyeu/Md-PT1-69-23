import time_it

time_it.start()
for i in range(100000):
    i+1
finish = time_it.finish()

print(finish)