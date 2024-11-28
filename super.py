

class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id


class Programmer(Employee):
    def __init__(self,name,id,language):
        super().__init__(name,id)
        self.language = language


Bijaya = Employee ("Bijaya Adhikari", 505)
Saugat = Programmer("Saugat Subedi", 506,"Python")

print(Saugat.__dict__)
print(Bijaya.id)