from tkinter.ttk import Label

from lesson12.Person import Person

class Adult(Person):
    def calculete_bmi(self):
        return self.weight / (self.height ** 2)

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "underweight"
        elif 18.5 <= bmi < 25:
            return "normal weight"
        elif 25 <= bmi < 30:
            return "overweight"
        else:
            return "obese"
