#Implement a text output of the time entered from the console (the user should input data in the format hh:mm).

#Show the responses to the user in Russian according to the rules listed below:
#min == 0: такое-то значение часа ровно (15:00 - три часа ровно)
#min < 30: столько-то минут следующего часа (19:12 - двенадцать минут восьмого)
#min == 30: половина такого-то (15:30 - половина четвёртого)
#min > 30 and min < 45 столько-то минут следующего часа (12:38 - тридцать восемь минут первого)
#min >= 45 без min такого-то (08:54 - без шести минут девять)



# проверка данных на валидность
while True:
    your_time = input("Please, input data in the format hh:mm\n")
    if your_time.count(":") != 1:
        print("You entered the wrong data format!\n")
        continue
    hh=your_time.split(":")[0]
    mm=your_time.split(":")[1]
    if not (hh.isdigit() and mm.isdigit()):
        print("You entered the wrong data format!\n")
        continue
    hh,mm=int(hh),int(mm)
    if hh>24:
        print("Incorrect input, the hour value sould be less then 24!\n")
        continue
    if mm>59:
        print("Incorrect input, the minutes value sould be less then 60!\n")
        continue

    break

        
# вывод буквенной части:
my_dict={0:['полночь','первого','ровно',''],
         1:['час','второго','одна','без одной'],
         2:['два','третьего','две','без двух'],
         3:['три','четвертого','три','без трех'],
         4:['четыре','пятого','четыре','без четырех'],
         5:['пять','шестого','пять','без пяти'],
         6:['шесть','седьмого','шесть','без шести'],
         7:['семь','восьмого','семь','без семи'],
         8:['восемь','девятого','восемь','без восьми'],
         9:['девять','десятого','девять','без девяти'],
         10:['десять','одиннадцатого','десять','без'],
         11:['одиннадцать','двенадцатого','одиннадцать','без одиннадцати'],
         12:['полдень','первого','двенадцать','без двенадцати'],
         13:['','','тринадцать','без тринадцати'],
         14:['','','четырнадцать','без четырнадцати'],
         15:['четверть','','','без четверти'],
         16:['','','шестнадцать',''],
         17:['','','семнадцать',''],
         18:['','','восемнадцать',''],
         19:['','','девятнадцать',''],
         20:['','','двадцать',''],
         30:['половина','','тридцать',''],
         40:['','','сорок','']}
hh_words=('часов','часа')
mm_words=('минута','минуты','минут')
x="(время до полудня)"
m1=(mm//10)*10
m2=mm-m1

if 12<hh<24:
    hh-=12
    x="(время после полудня)"
if mm==0:
    if hh==0 or hh==12:
        print(your_time,' - ',my_dict[hh][0])
    elif hh==1:
        print(your_time,' - ',my_dict[hh][0],my_dict[mm][2],x)
    elif 1<hh<5:
        print(your_time,' - ',my_dict[hh][0],hh_words[1],my_dict[mm][2],x)
    elif 4<hh<12:
        print(your_time,' - ',my_dict[hh][0],hh_words[0],my_dict[mm][2],x)
elif mm==15 or mm==30:
    print(your_time,' - ',my_dict[mm][0],my_dict[hh][1],x)
elif mm==1 or mm==21 or mm==31 or mm==41:
    print(your_time,' - ',my_dict[m1][2],my_dict[m2][2],mm_words[0],my_dict[hh][1],x)
elif 1<mm<5 or 21<mm<25 or 31<mm<35 or 41<mm<45:
    print(your_time,' - ',my_dict[m1][2],my_dict[m2][2],mm_words[1],my_dict[hh][1],x)
elif 4<mm<15 or 15<mm<21 or 24<mm<30 or 34<mm<41:
    print(your_time,' - ',my_dict[m1][2],my_dict[m2][2],mm_words[2],my_dict[hh][1],x)
elif mm==45:
    if hh==11 and x=="(время после полудня)":
        print(your_time,' - ',my_dict[60-mm][3],my_dict[0][0],x)
    else:
        print(your_time,' - ',my_dict[60-mm][3],my_dict[hh][1],x)
elif 45<mm<59:
    if hh==11 and x=="(время после полудня)":
        print(your_time,' - ',my_dict[60-mm][3],mm_words[2],my_dict[0][0],x)
    else:
        print(your_time,' - ',my_dict[60-mm][3],mm_words[2],my_dict[hh+1][0],x)
elif mm==59:
    if hh==11 and x=="(время после полудня)":
        print(your_time,' - ',my_dict[60-mm][3],mm_words[1],my_dict[0][0],x)
    else:
        print(your_time,' - ',my_dict[60-mm][3],mm_words[1],my_dict[hh+1][0],x)
else:
    print("Что-то пошло не так :( ")