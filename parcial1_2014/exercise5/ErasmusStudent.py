from parcial1_2014.exercise5.Student import Student


class ErasmusStudent(Student):
    def __init__(self, dni, name, email, country):
        Student.__init__(self, dni, name, email)
        self.country = country

    def __str__(self):
        return "Erasmus - " + super().__str__() + ", Country: " + self.country
