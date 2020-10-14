#   Functions Overriding
#   Function with same name present in parent class is also present in child class
#   But with different implementation

class parent:
    fatherName = ""
    motherName = ""

    def motorcycle(self):
        print("This is " + str(self.fatherName) + " motorcycle")
        print("This is Fathers motorcycle with ti ti horn and simple silencer")


class child(parent):
    childName = ""
    childAge = ""
    def motorcycle(self):
        print("This is " + self.childName + " motorcycle")
        print("This is child own motorcycle with pan pan horn and heavy silencer.")

c1 = child()
c1.childName = "Ali"
c1.childAge = 20
c1.fatherName = "Ahmad"
c1.motherName = "Amna"
c1.motorcycle()