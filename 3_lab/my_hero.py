# my_hero.py

class Hero:
    """Клас, що представляє героя з Dota 2
    
    Атрибути:
    ----------
    name : str
        Ім'я героя
    role : str
        Роль героя (наприклад, "Carry", "Support", "Tank")
    health : int
        Поточне здоров'я героя
    skills : list
        Список навичок героя
    """

    def __init__(self, name: str, role: str, health: int, skills: list):
        self.name = name
        self.role = role
        self.health = health
        self.skills = skills

    def attack(self, target):
        """Атакує ворога"""
        return f"{self.name} атакує {target.name}!"

    def use_skill(self, skill_index: int):
        """Використовує навичку"""
        if skill_index < len(self.skills):
            return f"{self.name} використовує навичку: {self.skills[skill_index]}"
        else:
            return "Навичка не знайдена."

    def __repr__(self):
        return f"{self.name} ({self.role}) - Здоров'я: {self.health}"
