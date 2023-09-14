import json

class Collection:
    def init(self):
        self.filename = "data.json"
        try:
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = []

    def add_item(self, title, artist_or_director, year, genre):
        self.data.append({
            'title': title,
            'artist_or_director': artist_or_director,
            'year': year,
            'genre': genre
        })
        self.save()

    def list_items(self):
        return self.data

    def search_by_title(self, search_term):
        for item in self.data:
            if search_term.lower() in item['title'].lower():
                yield item

    def search_by_artist(self, search_term):
        for item in self.data:
            if search_term.lower() in item['artist_or_director'].lower():
                yield item

    def search_by_year(self, search_term):
        for item in self.data:
            if str(search_term) in str(item['year']):
                yield item

    def search_by_genre(self, search_term):
        for item in self.data:
            if search_term.lower() in item['genre'].lower():
                yield item

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f)