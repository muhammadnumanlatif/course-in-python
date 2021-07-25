
class House:
    rooms = None
    bathrooms = None
    has_garage = None

    def __init__(self, num_rooms, num_bathrooms, has_garage):
        self.rooms = num_rooms
        self.bathrooms = num_bathrooms
        self.has_garage = has_garage
    
    def total_num_of_rooms(self):
        return self.rooms + self.bathrooms

seha_house = House(num_rooms=3,num_bathrooms=2,has_garage=False)
print(seha_house.rooms)
print(seha_house.bathrooms)
print(seha_house.has_garage)
print(seha_house.total_num_of_rooms)


class Hotel(House):
    pass


seha_hotel = Hotel(num_rooms=25, num_bathrooms=35, has_garage=True)
print(seha_hotel.total_num_of_rooms)

