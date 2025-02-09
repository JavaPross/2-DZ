import random


class Job:
    def __init__ (self, name: str = "example_job", salary: float = 1):
        self.name = name
        self.salary = salary

    # Setters
    def set_name(self, name: str):
        self.name = name

    def set_salary(self, salary: float):
        self.salary = salary


class Human:
    def __init__(self, name: str, job: Job = None, home=None, car=None, money: float = 0, psyhik: float = 100):
        self.name = name
        self.job = job
        self.home = home
        self.happiness = 100
        self.satiety = 100
        self.car = car
        self.money = money
        self.psyhik = psyhik

    # Setters
    def set_name(self, name): 
        self.name = name

    def set_home(self, home): 
        self.home = home

    def set_car(self, car): 
        self.car = car

    def set_job(self, job): 
        self.job = job

    def set_psyhik(self, psyhik: float): 
        self.psyhik = psyhik

    # Functions
    def eat(self):
        self.satiety += 10

    def decrease_psyhik(self):
        self.psyhik -= 1

    def work(self):
        if self.job:
            self.money += self.job.salary
        else:
            print(f"{self.name} не имеет работы!")



programmer = Job("Programmer", 1500)
snipervigrevkalmara = Job("killerpromax", 500000000)
it_specialist = Job("It specialist", 1000)
deputat = Job("Dovlet qulluqcusu", 6000)
Javad = Human("Javad", snipervigrevkalmara, None, None, 1000000)

print(f"Job:\n\tName: {snipervigrevkalmara.name}\n\tSalary: {snipervigrevkalmara.salary}")

print(f"Human:\n\tName: {Javad.name}\n\tJob: {Javad.job.name} with salary {Javad.job.salary}\n\tHome: {Javad.home}\n\tCar: {Javad.car}\n\tMoney: {Javad.money}")


simple_job = Job()
print(f"Job:\n\tName: {simple_job.name}\n\tSalary: {simple_job.salary}")

new_name = input("Input new job name: ")
new_salary = float(input("Input new job salary: "))

simple_job.set_salary(new_salary)
simple_job.set_name(new_name)

if new_name == snipervigrevkalmara.name:
    Javad.psyhik -= 50

if Javad.psyhik < 50:
    print("soshelsuma!")

print(f"Javad's psyhik: {Javad.psyhik}")
