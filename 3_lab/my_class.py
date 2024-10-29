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
    
    @property
    def name(self):
        """Ця властивість є затритою, її можна читати але не можна змінювати
        """
        return self.__name
    
    @property
    def surname(self):
        return self.__surname
    
    def __repr__(self):
        return "Представлення обєкту Студент, його задають: MySuperClass(surname, name, mark)"
    
    def __len__(self):
        return len(self.surname)

def function_in_module():
    pass



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
