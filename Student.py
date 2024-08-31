class Student:
    def __init__(self, id, homeLocation, alumni = "", volunteer = ""):
        self.id = id
        self.homeLocation = homeLocation
        self.alumni = alumni 
        self.volunteer = volunteer 

    def __repr__(self):
        is_alumni = ("Is alumni of " if self.alumni else "Is not alumni of ") + self.alumni
        is_volunteer = ("Is volunteer of " if self.volunteer else "Is not volunteer of ") + self.volunteer
        return f"Student {self.id}, at home location {self.homeLocation}. {is_alumni}. {is_volunteer}" 
    
    