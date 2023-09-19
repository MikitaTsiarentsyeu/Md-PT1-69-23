import json

class DataBase:
    def __init__(self, filename):
        self.filename = filename

    def get_collection(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return None

    def post_collection(self, headers, user_inputs):
        data = DataBase.get_collection(self)
        data.append(dict(zip(headers, user_inputs)))
        with open(self.filename, 'w') as file:
            json.dump(data, file, sort_keys=True, indent=4)
        return True

    def gen_search_in_collection(self, search_input, by):
        data = DataBase.get_collection(self)
        for i in data:
            if search_input in i[by]:
                yield i