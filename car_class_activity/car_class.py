class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5
        if self.__speed < 0:
            self.__speed = 0

    def get_speed(self):
        return self.__speed

def main():
    my_car = Car("2024", "Ford")

    print(f"Testing the Car Class...")
    print("-" * 30)

    print("Accelerating:")
    for i in range(5):
        my_car.accelerate()
        print(f"Call {i + 1}: Current speed is {my_car.get_speed()}")

    print("-" * 30)

    print("Braking:")
    for i in range(5):
        my_car.brake()
        print(f"Call {i + 1}: Current speed is {my_car.get_speed()}")

if __name__ == "__main__":
    main()