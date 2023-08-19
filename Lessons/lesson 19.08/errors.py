def test_func():
    try:
        return test[0]
    except:
        print("function level")
        raise ValueError("something went wrong")
    
test = 5

try:
    while True:
        try:
            if test == 5:
                try:
                    res = test_func()
                except ValueError:
                    print("ooops print")
                    break
        except NameError:
            print("ooops if")
            break
except:
    print("ooops while")



# try:
#     print(var)
# except NameError:
#     raise ValueError("BOOM!")

try:
    if True:
        raise NameError("the name is not defined")
except NameError as e:
    print(e)
except ValueError as e:
    print(e)
except:
    print("something went wrong")
else:
    print("everything went smoothly")
finally:
    print("finally!")


f = open("test.txt", 'w')
try:
    f.write("test")
finally:
    f.close()

with open("test.txt", 'w') as f:
    f.write("test")