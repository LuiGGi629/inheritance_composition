class Address:
    def __init__(self, street, city, state, zipcode, street2="") -> None:
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.street2 = street2

    def __str__(self) -> str:
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f"{self.city}, {self.state}, {self.zipcode}")
        return "\n".join(lines)


address = Address("55 Main St.", "Concord", "NH", "03301")
print(address)
