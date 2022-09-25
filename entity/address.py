class Address:
    def __init__(self, country, city, street, building, zip_code, apartment=None, state=None):
        self.country = country
        self.city = city
        self.street = street
        self.building = building
        self.zip_code = zip_code
        self.apartment = apartment
        self.state = state

    @property
    def full_address(self):
        full_address = f"{ f'{self.apartment}, ' if self.apartment is not None else ''}" \
                       f"{self.building}, {self.zip_code}, {self.city}, "\
                       f"{f'{self.state}, ' if self.state is not None else ''}{self.country}"

        return full_address
