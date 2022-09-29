class Truck:
    def __init__(self, truck_id, packages=None):
        self.truck_id = truck_id  # example: truck1
        self.packages = packages
        self.miles = 0  # miles are initially set to 0

    def __str__(self):
        return str(self.packages)

    def get_packages(self):
        return self.packages  # return all packages on the truck
