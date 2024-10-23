class MySuperClass:
    def __init__(self, surname, name, mark):
        # в середині конструктора створюються атрибути
        self.surname = surname
        self.name = name
        self.mark = mark

def function_in_module():
    pass



# Прикалад ChatGPT

class Car:
    """Цей клас представляє автомобіль."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        """Відображає об'єкт у зручному форматі."""
        return f"Car(марка='{self.make}', модель='{self.model}', рік={self.year})"

    def age(self):
        """Повертає вік автомобіля."""
        from datetime import datetime
        current_year = datetime.now().year
        return current_year - self.year
