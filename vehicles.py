class Vehicle:
    def __init__(
        self, Make, Model, Year, Weight, NeedsMaintenance=False, TripsSinceMaintenance=0
    ):
        self.Make = Make
        self.Model = Model
        self.Year = Year
        self.Weight = Weight

    def setMake(self, Make):
        self.Make = Make

    def setModel(self, Model):
        self.Model = Model

    def setYear(self, Year):
        self.Year = Year

    def setWeight(self, Weight):
        self.Weight = Weight


class Cars(Vehicle):
    def __init__(
        self,
        Make,
        Model,
        Year,
        Weight,
        NeedsMaintenance=False,
        TripsSinceMaintenance=0,
        isDriving=False,
    ):
        Vehicle.__init__(self, Make, Model, Year, Weight)
        self.NeedsMaintenance = NeedsMaintenance
        self.TripsSinceMaintenance = TripsSinceMaintenance
        self.isDriving = isDriving

    def Drive(self):

        self.isDriving = True
        self.TripsSinceMaintenance += 1

    def Stop(self):
        self.isDriving = False
        self.TripsSinceMaintenance += 1

    def Verify(self):
        if self.TripsSinceMaintenance >= 100:
            self.NeedsMaintenance = True

    def Repair(self):
        self.NeedsMaintenance = False
        self.TripsSinceMaintenance = 0


class Plane(Vehicle):
    def __init__(
        self,
        Make,
        Model,
        Year,
        Weight,
        TripsSinceMaintenance=0,
        NeedsMaintenance=False,
        isFlying=False,
    ):
        Vehicle.__init__(self, Make, Model, Year, Weight)
        self.NeedsMaintenance = NeedsMaintenance
        self.TripsSinceMaintenance = TripsSinceMaintenance
        self.isFlying = isFlying

    def Flying(self):
        self.isFlying = True
        self.TripsSinceMaintenance += 1
        if self.TripsSinceMaintenance == 100:
            isFlying = False

    def Landing(self):
        self.isFlying = False
        self.TripsSinceMaintenance += 1

    def Verify(self):
        if self.TripsSinceMaintenance >= 100:
            self.NeedsMaintenance = True
            print("The plane cannot fly!!!")

    def Repair(self):
        self.TripsSinceMaintenance = 0
        self.NeedsMaintenance = False


newCar1 = Cars("Dacia", "Logan", 2009, 1000)
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Drive()
newCar1.Stop()
newCar1.Verify()
print("Make: ", newCar1.Make)
print("Model: ", newCar1.Model)
print("Year: ", newCar1.Year)
print("Weight: ", newCar1.Weight)
print("Before maintenance: ", newCar1.TripsSinceMaintenance)
print("Needs maintenance: ", newCar1.NeedsMaintenance)
print()
newCar1.Repair()
print("After maintenance: ", newCar1.TripsSinceMaintenance)
print("Needs maintenance: ", newCar1.NeedsMaintenance)
print()
print()


newCar2 = Cars("Opel", "Astra H", 2004, 1500)
newCar3 = Cars("BMW", "X1", 2010, 1000)
print("Make: ", newCar2.Make)
print("Model: ", newCar2.Model)
print("Year: ", newCar2.Year)
print("Weight: ", newCar2.Weight)
newCar2.Drive()
newCar2.Stop()
newCar2.Drive()
newCar2.Stop()
newCar2.Drive()
newCar2.Stop()
print("Before maintenance: ", newCar2.TripsSinceMaintenance)
print("Needs maintenance: ", newCar2.NeedsMaintenance)
print()
print()


print("Make: ", newCar3.Make)
print("Model: ", newCar3.Model)
print("Year: ", newCar3.Year)
print("Weight: ", newCar3.Weight)
newCar3.Drive()
newCar3.Stop()
newCar3.Drive()
newCar3.Stop()
newCar3.Drive()
newCar3.Stop()
newCar3.Drive()
newCar3.Stop()
newCar3.Drive()
newCar3.Stop()
newCar3.Drive()
newCar3.Stop()
print("Before maintenance: ", newCar3.TripsSinceMaintenance)
print("Needs maintenance: ", newCar3.NeedsMaintenance)
print()
print()


newPlane1 = Plane("Tarom", "dasdjh", 2010, 10000)
print("Make: ", newPlane1.Make)
print("Model: ", newPlane1.Model)
print("Year: ", newPlane1.Year)
print("Weight: ", newPlane1.Weight)
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Flying()
newPlane1.Landing()
newPlane1.Verify()
print("Before maintenance: ", newPlane1.TripsSinceMaintenance)
print("Needs maintenance: ", newPlane1.NeedsMaintenance)
newPlane1.Flying()
newPlane1.Flying()
newPlane1.Flying()
newPlane1.Flying()
newPlane1.Flying()
