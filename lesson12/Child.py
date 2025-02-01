from tkinter.ttk import Label

from lesson12.Person import Person

class Child(Person):
    def calculete_bmi(self):
        return self.weight / (self.height ** 2)  * 1.3

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 14:
            return "underweight"
        elif 14 <= bmi < 18:
            return "normal weight"
        elif 18 <= bmi < 24:
            return "overweight"
        else:
            return "obese"
