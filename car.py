class Car:
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year
        self.__cupholders = 5

    def __str__(self):
        return (f"Color : {self.color} | Model: {self.model} | Year: {self.year}")
