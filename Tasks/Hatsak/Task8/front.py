import back


print('Hello, this program will help you to manage movies you watched!')
while True:
    print("""To add a movie to your collection press 1;
    To look throw your movie collection press 2;
    To search a movie from your collection press 3;
    To quit the program press 'q';""")

    ans = input('Chose: ')

    if ans.lower() == 'q':
        exit()
    elif ans == '1':
        back.add_movie()
        continue
    elif ans == '2':
        back.list_movies()
        continue
    elif ans == '3':
        back.search()



