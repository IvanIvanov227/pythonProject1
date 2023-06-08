class Feast:
    def __init__(self, name, count, list_person=None):
        self.name = name
        self.count = count
        if list_person is None:
            list_person = set()
        self.list_person = list_person

    def remove_guest(self, person):
        if person in self.list_person:
            self.list_person.remove(person)
            self.count += 1

    def add_guest(self, person):
        self.list_person.add(person)
        if self.count > 0:
            self.count -= 1

    def get_guests(self):
        return sorted(list(self.list_person))

    def __str__(self):
        return f'Feast of {self.name}, number of invited guests is {self.count}'

    def __eq__(self, other):
        """Сравнение =="""
        if self.count == other.count:
            return True
        elif len(self.list_person) == len(other.list_person):
            if self.name == other.name:
                return True
            return True
        return False

    def __ne__(self, other):
        """Сравнение !="""
        if self.count != other.count:
            return True
        elif len(self.list_person) != len(other.list_person):
            if self.name != other.name:
                return True
            return True
        return False

    def __lt__(self, other):
        """Сравнение <"""
        if self.count < other.count:
            return True
        elif len(self.list_person) < len(other.list_person):
            if self.name < other.name:
                return True
            return True
        return False

    def __le__(self, other):
        """Сравнение <="""
        if self.count <= other.count:
            return True
        elif len(self.list_person) <= len(other.list_person):
            if self.name <= other.name:
                return True
            return True
        return False

    def __gt__(self, other):
        """Сравнение >"""
        if self.count > other.count:
            return True
        elif len(self.list_person) > len(other.list_person):
            if self.name > other.name:
                return True
            return True
        return False

    def __ge__(self, other):
        """Сравнение >="""
        if self.count >= other.count:
            return True
        elif len(self.list_person) >= len(other.list_person):
            if self.name >= other.name:
                return True
            return True
        return False

ft = Feast('John', 7)
ft1 = Feast('Jack', 7)
print(ft >= ft1)
ft.add_guest('Lizard')
ft1.add_guest('Flamingo')
print(ft < ft1)
ft.remove_guest('Owl')
ft1.remove_guest('Flamingo')
print(ft <= ft1)