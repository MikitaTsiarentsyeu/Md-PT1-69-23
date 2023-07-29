import time

chunk_size = 10000

start = time.time()
with open("test.JPG", 'rb') as donor:
    with open("test_copy.JPG", 'wb') as recepient:
        while True:
            content = donor.read(chunk_size)
            if content:
                recepient.write(content)
            else:
                break
finish = time.time()

print(finish-start)

