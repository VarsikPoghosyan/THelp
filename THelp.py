import json

class Hotel:
    def __init__(self, name, location, rating):
        self.name = name
        self.location = location
        self.rating = rating

class Reservation:
    def __init__(self, from_date, to_date, price):
        self.price = price
        self.from_date = from_date
        self.to_date = to_date


class Tourist:
    def __init__(self, start_date, end_date,rating_low, rating_high, cost_low, cost_high, location):
        self.strat_date = start_date
        self.end_date = end_date
        self.rating_low = rating_low
        self.rating_high = rating_high
        self.cost_low = cost_low
        self.cost_high = cost_high
        self.location = location

def loadhoteldata():
    with open('hote.json') as data_file:
        hotel_info = json.load(data_file)
    list_ = list()
    rest_house = Hotel("Multi Rest House", hotel_info["Multi Rest House"]["location"], hotel_info["Multi Rest House"]["rating"])
    list_.append(rest_house)
    dilijan_resort = Hotel("Dilijan Resort", hotel_info["Dilijan Resort"]["location"], hotel_info["Dilijan Resort"] ["rating"])
    list_.append(dilijan_resort)
    mariot = Hotel("Mariot", hotel_info["Mariot"]["location"], hotel_info["Mariot"] ["rating"])
    list_.append(mariot)
    opera = Hotel("Opera", hotel_info["Opera"]["location"], hotel_info["Opera"] ["rating"])
    list_.append(opera)


    return hotel_info

def loadtouristdata():
    with open('tourist1.json') as data_file:
        tourist_info = json.load(data_file)
    return tourist_info

def touristInput():
    start_date = raw_input("Please insert your starting date: ")
    end_date = raw_input("Please insert your ending date: ")
    rating_low = input("Please insert the lowest rating of the hotel: ")
    rating_high = input("Please insert the highest rating of the hotel: ")
    cost_high = input("Please insert the maximum amount you can pay: ")
    cost_low = input("Please insert the minimum amount you can pay: ")
    location = raw_input("Please insert your desired location: ")
    return Tourist(start_date, end_date,rating_low, rating_high, cost_low, cost_high, location)

def reserve(tourist,hotels):
   for i in range(len(hotels)):
       if tourist.location == hotels.location:
           print "You reservation accepted."
       else:

           print "Sorry,"


def main():
    #call function loading hotel data
    #call function(s) asking user for inputs & storing inputs in json file
    hotels = loadhoteldata()
    tourist = touristInput()
    reserve(tourist, hotels)



main()
