class School:
    def __init__(self, name, location, maxAllocation):
        self.name = name
        self.location = location
        self.maxAllocation = maxAllocation

    def __repr__(self):
        return f"School {self.name}, at location {self.location}, with max allocation {self.maxAllocation}"
    
    