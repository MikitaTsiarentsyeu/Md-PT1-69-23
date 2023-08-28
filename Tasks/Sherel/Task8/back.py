import json
import tabulate

class DataBase:
    def get_collection(self):
        with open('data.json', 'r') as file:
            data = json.load(file)
        return print(f'\n{tabulate.tabulate(data, headers="firstrow")}')

    def post_collection(self):
        with open('data.json', 'r') as file:
            data = json.load(file)
        message_for_user = ["Name picture: ", "Author picture: ", "Year picture: ", "Genre picture: "]
        headers = ["title", "author", "year", "genre"]
        user_inputs = []
        for x in message_for_user:
            while True:
                input_value = input(x)
                if not input_value:
                    print("The field cannot be empty, please enter a value.")
                else:
                    user_inputs.append(input_value)
                    break
        data.append(dict(zip(headers, user_inputs)))
        with open('data.json', 'w') as file:
            json.dump(data, file, sort_keys=True, indent=4)
        return print('\nThe picture has been added to the database.')

    def gen_search_in_collection(self, by):
        with open('data.json', 'r') as file:
            data = json.load(file)
        for i in data:
            if self in i[by]:
                yield i
