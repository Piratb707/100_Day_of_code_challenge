from collections import namedtuple

def can_take_order(driver, num_packages):
    return driver.car_capacity >= num_packages

def main():
    Driver = namedtuple('driver', ['name', 'car_type', 'car_capacity'])
    iris = Driver('Iris', 'Prius', 7)
    mickie = Driver('Mickie', 'Tucson', 15)
    witty = Driver('Witty', 'Hummer', 26)
    print(can_take_order(iris,20))
    return


if __name__ == '__main__':
    main()