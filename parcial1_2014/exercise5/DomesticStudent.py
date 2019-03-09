from parcial1_2014.exercise5.Student import Student


class DomesticStudent(Student):
    def __init__(self, dni, name, email, province):
        Student.__init__(self, dni, name, email)
        self.province = province

    def __str__(self):
        return "Domestic - " + super().__str__() + ", Province: " + self.province
