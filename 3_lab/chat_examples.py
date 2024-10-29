# Ось так нам допоміг ChatGPT зробити опис
class Students:
    """
    Клас Students для зберігання інформації про студентів.

    Attributes:
        surname (str): Прізвище студента.
        name (str): Ім'я студента.
        mark (int): Оцінка студента.
    """

    def __init__(self, surname: str, name: str, mark: int):
        """
        Ініціалізує новий екземпляр класу Students.

        Args:
            surname (str): Прізвище студента.
            name (str): Ім'я студента.
            mark (int): Оцінка студента, яка повинна бути цілим числом.
        """
        print("Викликаємо __init__")
        self.surname = surname
        self.name = name
        self.mark = mark



from my_class import Animal

def demonstrate_animal_class():
    animal1 = Animal("Рекс", "Собака", 5)
    print(f"Створено: {animal1}")

    animal2 = Animal("Мурка", "Кіт", 3)
    print(f"Створено: {animal2}")

    # Виклик методу для звуку
    animal1.make_sound("Гав")
    animal2.make_sound("Мяу")

    # Динамічний атрибут
    animal1.color = "Чорний"
    print(f"{animal1.name} має колір: {animal1.color}")
