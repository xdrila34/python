from lesson12.Adult import Adult
from lesson12.Child import Child


BMIApp:
    def __init__(self):
        self.people = []
    def add_person(self, person):
        self.people.append(person)

    def collect_user_data(self):
        name = input("enter name")
        age = int(input("enter age"))
        weight = float(input("enter weight"))
        height = float(imput("enter height"))

        if age >= 18:
            person = Adult()
        else:
            person = child()

        self.add_person(person)

        def print_result(self):
            for person in self.people:
                person.print_info()

        def run(self):
            while true:
                self.collect_user_data()
                cconst = imput("do you want to add another person? (yes/no):").strip.lower()
                if const != 'yes':
                    break
                slef.print_reslt