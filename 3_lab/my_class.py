class MySuperClass:
    """Тестовий клас, зараз реалізуємо опис студента
    
    ---

    surname : str
        Прізвище студента
    
    """
    var_lover_case = "Це проста класова змінна"
    COLLEGE_NAME = "Це подібне до константи в клосі, але ми можемо її перезаписати"
    _protected_var = 1
    __private_var = 2

    total_students = 0
    total_marks = 0

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

        self.var_lover_case = "Перазаписали класові змінну"
        MySuperClass.total_students += 1
        MySuperClass.total_marks += mark


    def __del__(self):
        print("Відрахували студента")
        MySuperClass.total_students -= 1

    @property
    def college_raiting(self):
        return MySuperClass.total_marks / MySuperClass.total_students

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
            self._scholarship = "1800 грн"
            return "Присвоєно підвищену стипундію"
        if raiting == 4:
            self._scholarship = "1400 грн"
            return "Присвоєно звичайну стипундію"
        self._scholarship = 0
        return "Рейтинг занизький для стипендії"
    
    def panishment(self):
        return "Ми прийшли додому і мама нас насварила за погані оцінки"
    
    @staticmethod
    def hobbi(h=None):
        """в таких методах нема вказівника на обєкт
        """
        if h:
            print(f"В мене зявилось хоббі {h}")
        else:
            print("На жаль в мене немає Хаббі")
    
    @classmethod
    def create_from_surname_name(cls, full_name:str):
        """ альтернативний конструктор, створюємо обєкт з повного імені
        розчеплюємо повне імя на частинки Прізкище та Імя
        """
        surname, name = full_name.split(" ")
        return cls(surname, name, 0)
    
    @classmethod
    def create_from_name_surname(cls, full_name:str):
        """ альтернативний конструктор, створюємо обєкт з повного імені
        розчеплюємо повне імя на частинки Прізкище та Імя
        """
        name, surname = full_name.split(" ")
        return cls(surname, name, 0)


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


class LibrarySystem:
    """Клас для управління бібліотечними книгами в бібліотечній системі."""
    
    # Класові змінні (для відстеження стану бібліотечної системи)
    total_books = 0  # Загальна кількість книг у бібліотеці
    available_books = 0  # Кількість доступних для позики книг
    total_loans = 0  # Загальна кількість позик
    
    def __init__(self, title, author):
        """Ініціалізуємо нову книгу з її назвою та автором."""
        self.title = title
        self.author = author
        self.is_borrowed = False  # Книга на початку не позичена
        
        # Збільшуємо загальну кількість книг та доступних книг
        LibrarySystem.total_books += 1
        LibrarySystem.available_books += 1

    def borrow(self):
        """Позика книги, якщо вона доступна."""
        if self.is_borrowed:
            return f"Книга '{self.title}' вже позичена."
        if LibrarySystem.available_books == 0:
            return "У бібліотеці немає доступних книг для позики."
        
        self.is_borrowed = True
        LibrarySystem.available_books -= 1
        LibrarySystem.total_loans += 1
        return f"Ви позичили книгу '{self.title}'."

    def return_book(self):
        """Повернення книги в бібліотеку."""
        if not self.is_borrowed:
            return f"Книга '{self.title}' не була позичена."
        
        self.is_borrowed = False
        LibrarySystem.available_books += 1
        return f"Ви повернули книгу '{self.title}'."

    @classmethod
    def library_status(cls):
        """Статус бібліотеки: кількість книг, доступних для позики, та позик."""
        return (f"У бібліотеці {cls.total_books} книг, з них доступних для позики {cls.available_books}."
                f" Загальна кількість позик: {cls.total_loans}.")

    @classmethod
    def add_book(cls, title, author):
        """Додати нову книгу до бібліотеки."""
        new_book = LibrarySystem(title, author)
        return new_book


# my_class/my_class.py

class Bodybuilder:
    """Клас, що представляє бодібілдера."""

    # Статична змінна для відстежування загальної кількості бодібілдерів
    total_bodybuilders = 0

    def __init__(self, name: str, age: int, weight: float, height: float):
        """Ініціалізація бодібілдера з атрибутами: ім'я, вік, вага, зріст."""
        self.name = name
        self.age = age
        self.weight = weight  # Вага в кг
        self.height = height  # Зріст в см
        self.progress = 0  # Прогрес в % від стартової форми
        self.training_plan = []  # План тренувань
        self.diet_plan = []  # План харчування

        # Збільшуємо кількість бодібілдерів
        Bodybuilder.total_bodybuilders += 1

    def __del__(self):
        """Метод для зменшення кількості бодібілдерів при видаленні об'єкта."""
        Bodybuilder.total_bodybuilders -= 1

    def calculate_bmi(self):
        """Вираховує ІМТ (Індекс маси тіла)."""
        height_in_meters = self.height / 100  # Перетворюємо зріст на метри
        return self.weight / (height_in_meters ** 2)

    def update_training_plan(self, new_plan: list):
        """Оновлює план тренувань."""
        self.training_plan = new_plan

    def update_diet_plan(self, new_diet: list):
        """Оновлює план харчування."""
        self.diet_plan = new_diet

    def track_progress(self):
        """Обчислює прогрес на основі змін у вазі та тренуваннях."""
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            self.progress = 10  # Прогрес на стадії набору маси
        elif 18.5 <= bmi < 25:
            self.progress = 50  # Оптимальна форма
        else:
            self.progress = 30  # Прогрес на стадії спалювання жиру
        return self.progress

    @staticmethod
    def get_total_bodybuilders():
        """Статичний метод для отримання загальної кількості бодібілдерів."""
        return Bodybuilder.total_bodybuilders

    @classmethod
    def create_bodybuilder_from_data(cls, data: dict):
        """Класовий метод для створення бодібілдера з даних у вигляді словника."""
        return cls(data['name'], data['age'], data['weight'], data['height'])




class Food:
    """Опис класу їжі в ресторані або кафе"""

    total_items = 0
    total_calories = 0

    def __init__(self, name: str, category: str, price: float, calories: int):
        """
        Ініціалізація страви з її атрибутами.
        - Назва страви, категорія (наприклад, закуска, основна страва), ціна, калорії.
        """
        print(f"Створюється страва: {name}")
        self.name = name          # Назва страви
        self.category = category  # Категорія страви (закуска, основна страва, десерт)
        self.price = price        # Ціна страви
        self.calories = calories  # Калорії

        # Збільшуємо загальну кількість страв та загальні калорії
        Food.total_items += 1
        Food.total_calories += calories

    def __del__(self):
        """Очищення після видалення страви"""
        print(f"Страва {self.name} була видалена")
        Food.total_items -= 1
        Food.total_calories -= self.calories

    @property
    def average_calories(self):
        """Властивість для отримання середньої кількості калорій усіх страв"""
        return Food.total_calories / Food.total_items if Food.total_items > 0 else 0

    @property
    def food_info(self):
        """Отримання загальної інформації про страву"""
        return f"{self.name} ({self.category}), ціна: {self.price} грн, калорії: {self.calories}"

    @classmethod
    def create_from_name_category(cls, name_category: str, price: float, calories: int):
        """Альтернативний конструктор для створення страви за назвою та категорією"""
        name, category = name_category.split(" - ")
        return cls(name, category, price, calories)

    @classmethod
    def create_from_category_name(cls, category_name: str, price: float, calories: int):
        """Альтернативний конструктор для створення страви за категорією та назвою"""
        category, name = category_name.split(" - ")
        return cls(name, category, price, calories)

    def __repr__(self):
        """Представлення об'єкта їжі"""
        return f"Food('{self.name}', '{self.category}', {self.price}, {self.calories})"

    def update_price(self, new_price: float):
        """Оновлення ціни страви"""
        self.price = new_price

    def update_calories(self, new_calories: int):
        """Оновлення калорій страви"""
        Food.total_calories -= self.calories
        self.calories = new_calories
        Food.total_calories += new_calories

    @staticmethod
    def food_category(category: str):
        """Статичний метод для виведення категорії страви"""
        print(f"Ця страва належить до категорії: {category}")

