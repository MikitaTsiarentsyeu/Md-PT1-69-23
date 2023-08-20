import time

run = False

def start():
    global start_time, run
    run = True
    start_time = time.time()

def finish():
    global run
    if run:
        end = time.time()
        run = False
        return end - start_time