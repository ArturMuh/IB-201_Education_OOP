class Weapon:
    def __init__(self, name: str, damage: int | float, range: int | float) -> None:
        self.name = name
        self.damage = damage
        self.range = range

    def hit(self, actor, target) -> None:
        if not target.is_alive():
            print("Враг уже повержен")
            return

        # Вычисляем расстояние между персонажами без math
        x1, y1 = actor.get_coords()
        x2, y2 = target.get_coords()
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5  # квадратный корень через **0.5

        if distance > self.range:
            print(f"Враг слишком далеко для оружия {self.name}")
        else:
            print(f"Врагу нанесен урон оружием {self.name} в размере {self.damage}")
            target.get_damage(self.damage)

    def __str__(self) -> str:
        return self.name


class BaseCharacter:
    def __init__(self, pos_x: int | float, pos_y: int | float, hp: int | float) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = hp

    def move(self, delta_x: int | float, delta_y: int | float) -> None:
        self.pos_x += delta_x
        self.pos_y += delta_y

    def is_alive(self) -> bool:
        return self.hp > 0

    def get_damage(self, amount: int | float) -> None:
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def get_coords(self) -> tuple:
        return (self.pos_x, self.pos_y)

class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x: int | float, pos_y: int | float, weapon: Weapon, hp: int | float) -> None:
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon

    def hit(self, target) -> None:
        if isinstance(target, MainHero):
            self.weapon.hit(self, target)
        else:
            print("Могу ударить только Главного героя")

    def __str__(self) -> str:
        return f"Враг на позиции ({self.pos_x}, {self.pos_y}) с оружием {self.weapon}"


class MainHero(BaseCharacter):
    def __init__(self, pos_x: int | float, pos_y: int | float, name: str, hp: int | float) -> None:
        super().__init__(pos_x, pos_y, hp)
        self.name = name
        self.weapons = []
        self.current_weapon_index = -1
        self.max_hp = 200

    def hit(self, target) -> None:
        if self.current_weapon_index == -1 or not self.weapons:
            print("Я безоружен")
            return

        if isinstance(target, BaseEnemy):
            current_weapon = self.weapons[self.current_weapon_index]
            current_weapon.hit(self, target)
        else:
            print("Могу ударить только Врага")

    def add_weapon(self, weapon) -> None:
        if not isinstance(weapon, Weapon):
            print("Это не оружие")
            return

        self.weapons.append(weapon)
        print(f"Подобрал {weapon}")

        # Если это первое оружие, экипируем его сразу
        if len(self.weapons) == 1:
            self.current_weapon_index = 0

    def next_weapon(self) -> None:
        if not self.weapons:
            print("Я безоружен")
            return

        if len(self.weapons) == 1:
            print("У меня только одно оружие")
            return

        self.current_weapon_index = (self.current_weapon_index + 1) % len(self.weapons)
        print(f"Сменил оружие на {self.weapons[self.current_weapon_index]}")

    def heal(self, amount: int | float) -> None:
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"Полечился, теперь здоровья {self.hp}")

weapon1 = Weapon("Короткий меч", 5, 1)
weapon2 = Weapon("Длинный меч", 7, 2)
weapon3 = Weapon("Лук", 3, 10)
weapon4 = Weapon("Лазерная орбитальная пушка", 1000, 1000)
princess = BaseCharacter(100, 100, 100)
archer = BaseEnemy(50, 50, weapon3, 100)
armored_swordsman = BaseEnemy(10, 10, weapon2, 500)
archer.hit(armored_swordsman)
armored_swordsman.move(10, 10)
print(armored_swordsman.get_coords())
main_hero = MainHero(0, 0, "Король Артур", 200)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.add_weapon(weapon1)
main_hero.hit(armored_swordsman)
main_hero.add_weapon(weapon4)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.hit(princess)
main_hero.hit(armored_swordsman)
main_hero.hit(armored_swordsman)