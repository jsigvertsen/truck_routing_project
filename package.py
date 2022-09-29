class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, status="At the hub"):
        self.package_id = package_id  # unique ID for each package
        self.address = address  # delivery address
        self.city = city  # delivery city
        self.state = state  # delivery state
        self.zip_code = zip_code  # delivery zip code
        self.deadline = deadline  # when package must be delivered by
        self.weight = weight  # package weight in KGs
        self.status = status  # current status of package
        self.time_delivered = None  # time package was delivered
        self.time_departed = None  # time package left the hub

    def __str__(self):
        return str([self.package_id,
                    self.address,
                    self.city,
                    self.state,
                    self.zip_code,
                    self.deadline,
                    self.weight,
                    self.status])

    def get_status(self, time):

        # for each package, set status based on interface input time
        if self.time_delivered and time > self.time_delivered:  # input time is past delivery time
            self.status = "DELIVERED - " + str(self.time_delivered)
        elif self.time_departed and time > self.time_departed:  # input time is past departed time but not delivered
            self.status = "EN ROUTE"
        else:  # if not delivered or en route, package is at the hub
            self.status = "AT THE HUB"

        # interface format
        return ("Time " + str(time) + ": " +
                str(self.package_id) + "  |  " +
                str(self.address) + "  |  " +
                str(self.deadline) + "  |  " +
                str(self.city) + "  |  " +
                str(self.state) + "  |  " +
                str(self.zip_code) + "  |  " +
                str(self.weight) + "  |  " +
                str(self.status))

    def get_package_address(self):  # return package address for any package object
        return self.address
