class MySuperClass:
    """Тестовий клас, зараз реалізуємо опис студента
    
    ---

    surname : str
        Прізвище студента
    
    """
    def __init__(self, surname:str, name, mark:int, group=None):
        """
        Ініціалізуємо обєкт
        - в середині конструктора створюються атрибути
        """
        print("Викликаємо __init__")
        self.__surname = surname #  private Це приватні атрибути, вони не висвічуються назовні
        self.__name = name
        self.mark = mark # public публічний атрибук
        self.group = group
        self._age = None # (protected) захищений атрибут
        self._scholarship = 0
    
    @property
    def name(self):
        """Ця властивість є закритою, її можна читати але не можна змінювати
        """
        return self.__name
    
    @property
    def surname(self):
        return self.__surname
    
    @property
    def say_hello(self):
        a = 1 + 2
        return f"Привіт {a}"
    
    def __repr__(self):
        return "Представлення обєкту Студент, його задають: MySuperClass(surname, name, mark)"
    
    def __len__(self):
        return len(self.surname)
    
    def fucntion_in_class(self):
        """Це вже метод згідно термінології, і він публічний
        """
        return "Ми викликали публічний метод"

    def _protected_method_in_class(self):
        """Це захищений метод
        """
        self.__this_is_private()
        return "Ми доступаємось до захищеного методу"
    
    def __this_is_private(self):
        print("Це приватний метод!")

    def calculate_scholarship_after_session(self, raiting: int):
        if raiting == 5:
            self._scholarship = "2200 грн"
            return "Вітаю! Отримано підвищену стипундію"
        if raiting == 4:
            self._scholarship = "1510 грн"
            return "вітаю! Отримано звичайну стипундію"
        self._scholarship = 0
        return "На жаль рейтинг занизький для стипендії"
    
    def panishment(self):
        return "Ми прийшли додому і мама нас насварила за погані оцінки"

def function_in_module():
    """Це просто функція (згідно загальної термінології)
    """
    pass



class Car:
    """Клас, що представляє автомобіль
    """

    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def __repr__(self):
        return f"{self.make} {self.model} ({self.year})"
    
    def age(self):
        """Обчислює вік автомобіля"""
        from datetime import datetime
        current_year = datetime.now().year
        return current_year - self.year




class Animal:
    """
    Клас Animal для зберігання інформації про тварин.

    Attributes:
        name (str): Ім'я тварини.
        species (str): Вид тварини.
        age (int): Вік тварини.
    """

    def __init__(self, name: str, species: str, age: int):
        """
        Ініціалізує новий екземпляр класу Animal.

        Args:
            name (str): Ім'я тварини.
            species (str): Вид тварини.
            age (int): Вік тварини.
        """
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self, sound: str):
        """Метод, що дозволяє тварині видавати звук."""
        print(f"{self.name} говорить: {sound}")

    def __repr__(self):
        return f"Animal(name='{self.name}', species='{self.species}', age={self.age})"


# my_class.py

class Book:
    """Клас, що представляє книгу"""
    
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return f"{self.title} успішно позичено."
        else:
            return f"{self.title} наразі недоступна."

    def return_book(self):
        self.is_available = True
        return f"{self.title} успішно повернено."


class User:
    """Клас, що представляє користувача бібліотеки"""
    
    def __init__(self, name: str):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book: Book):
        result = book.borrow()
        if not book.is_available:
            self.borrowed_books.append(book)
        return result

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return f"{book.title} повернуто користувачем {self.name}."
        else:
            return f"{self.name} не позичав цю книгу."


class Library:
    """Клас, що представляє бібліотеку"""
    
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def list_books(self):
        available_books = [book.title for book in self.books if book.is_available]
        return available_books

