class Employee:
    company = 'Газпром'

    def __init__(self, name, salary, on_vacation, is_good_employee):
        self.name = name
        self.salary = salary
        self.on_vacation = on_vacation
        self.is_good_employee = is_good_employee

    def get_info(self):
        print(f'У {self.name} заплата {self.salary}. В отпуске - ? {"Да" if self.on_vacation else "Нет"}')


persons = [Employee('Александр', 15000, True, True), Employee('Дарья', 150000, False, False),
           Employee('Олег', 43020, False, True), Employee('Анастасия', 15600, True, True),
           Employee('Екатерина', 35000, False, True)]

for i in persons:
    if not i.is_good_employee:
        print(f'Сотрудник {i.name} уволен!')
        persons.pop(persons.index(i))
        print()
        print('Список оставшихся сотрудников:')
        for new_list in persons:
            print(f'- {new_list.name}')