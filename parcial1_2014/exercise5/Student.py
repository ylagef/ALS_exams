class Student:
    def __init__(self, dni, name, email):
        self.dni = dni
        self.name = name
        self.email = email

    def __str__(self):
        return "DNI: " + self.dni + ", Name: " + self.name + ", Email: " + self.email
