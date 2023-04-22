class Location():
    location_adress: str
    location_place: tuple(int,int)

    def __init__(self, picture: str, coordinate: tuple(int,int)):
        self.location_place = coordinate
        self.location_adress = picture

bell_tower: Location(jpg,(x,y))
places: list[Location] = [bell_tower, old_well]