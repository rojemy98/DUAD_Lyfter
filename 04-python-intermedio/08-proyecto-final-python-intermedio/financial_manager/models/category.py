class Category:

    # Initialize a category with name and color
    def __init__(self, name, color):

        # Category name
        self.name = name

        # Category color in HEX format (#FFA500)
        self.color = color


    # Convert category object into a list
    def to_list(self):

        return [
            self.name,   # Category name
            self.color   # Category color
        ]