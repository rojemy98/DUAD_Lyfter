class Category:

    def __init__(self, name, color):

        self.name = name
        self.color = color


    def to_list(self):

        return [
            self.name,
            self.color
        ]