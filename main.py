import csv
import math

from datetime import timedelta
from truck import Truck
from package import Package
from hash_table import Hash


def load_package_data(filename):
    with open(filename, encoding="utf-8-sig") as packages:
        package_data = csv.reader(packages, delimiter=",")
        next(package_data)
        # assign each item in package_data to an attribute
        for i in package_data:
            p_id = int(i[0])
            p_address = i[1]
            p_city = i[2]
            p_state = i[3]
            p_zip = i[4]
            p_deadline = i[5]
            p_weight = i[6]

            # create package object and add object to the hash table
            my_package = Package(p_id, p_address, p_city, p_state, p_zip, p_deadline, p_weight)
            hash_table.insert(p_id, my_package)


def find_distance(x, y):
    distance = d[x][y]  # lookup x and y in the distance matrix table d

    return float(distance)  # return the distance between x and y


def find_address_id(package_id):
    # search the hash table for package address
    package_address = hash_table.search(package_id).get_package_address()

    # search the address csv file and return the address ID
    for i in range(len(a)):
        if package_address == a[i][1]:
            return int(a[i][0])


def truck_scheduler(truck_packages, departure_time=timedelta(hours=8), speed=18):
    route = []
    dist_traveled = 0
    start_address = 0
    min_package = None
    curr_time = departure_time
    truckload = truck_packages

    # set departure time for each package
    for package in range(len(truck_packages)):
        hash_table.search(truck_packages[package]).time_departed = curr_time

    # find the optimal next address as long as there are packages on the truck
    while len(truck_packages) > 0:
        # initial assignment for minimum distance
        m_distance = float(math.inf)

        # find the package with the shortest path of remaining packages in truck from starting point
        for package in range(len(truck_packages)):
            if find_distance(start_address, find_address_id(truckload[package])) < m_distance:
                m_distance = find_distance(start_address, find_address_id(truckload[package]))
                min_package = truckload[package]  # the package closest to starting address

        curr_time += timedelta(hours=(m_distance / speed))  # add time spent traveling to departure time
        hash_table.search(min_package).time_delivered = curr_time  # assign delivery time to package object
        route.append(min_package)  # add package to route
        dist_traveled += m_distance  # add distance to address to total distance traveled
        truckload.remove(min_package)  # remove package from truck
        start_address = find_address_id(min_package)  # assign start address to shortest distance package

    return dist_traveled  # return the total distance traveled for the truck


def interface(time):
    print("Total miles:", format(total_miles, '.2f'))  # print total miles of all trucks in interface

    for i in range(40):
        print(hash_table.search(i + 1).get_status(time))  # print all attributes of each package


# address file containing address and address ID
with open('Address File.csv', encoding="utf-8-sig") as addresses:
    address_data = csv.reader(addresses, delimiter=",")
    a = list(address_data)

# distance table containing address ID and distances in miles
with open('WGUPS Distance Table.csv', encoding="utf-8-sig") as distances:
    distance_data = csv.reader(distances, delimiter=",")
    d = list(distance_data)

# create hash table instance and load packages into the hash table
hash_table = Hash()
load_package_data('WGUPS Package File.csv')

# create an instance for each truck with truck_id and packages
truck1 = Truck(1, [15, 16, 1, 13, 14, 19, 20, 29, 33, 30, 31, 37])
truck2 = Truck(2, [6, 18, 25, 28, 32, 36, 38, 40, 34, 3, 35, 39])
truck3 = Truck(3, [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24, 26, 27])

# add the total miles traveled for each truck and assign to truck object
truck1.miles += truck_scheduler(truck1.get_packages(), timedelta(hours=8))
truck2.miles += truck_scheduler(truck2.get_packages(), timedelta(hours=9, minutes=5))
hash_table.search(9).address = '410 S State St'  # update address for package 9
truck3.miles += truck_scheduler(truck3.get_packages(), timedelta(hours=10, minutes=20))

# add total miles for each truck
total_miles = truck1.miles + truck2.miles + truck3.miles

# show status of packages at a specified time
interface(timedelta(hours=13))
