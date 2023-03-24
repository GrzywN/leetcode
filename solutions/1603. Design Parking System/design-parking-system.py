class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking = {
            1: [big, 0],
            2: [medium, 0],
            3: [small, 0],
        }

    def addCar(self, carType: int) -> bool:
        max_parked_cars, curr_parked_cars = self.parking[carType]

        if curr_parked_cars + 1 > max_parked_cars:
            return False

        self.parking[carType][1] = curr_parked_cars + 1
        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
