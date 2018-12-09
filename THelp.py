import json

class Node:
    def __init__(self):
        self.next = None

class Hotel(Node):
    def __init__(self, name, location, rating):
        Node.__init__(self)
        self.name = name
        self.location = location
        self.rating = rating


class Reservation(Node):
    def __init__(self, from_date, to_date, price):
        Node.__init__(self)
        self.price = price
        self.from_date = from_date
        self.to_date = to_date


class Tourist(Node):
    def __init__(self, start_date, end_date,rating_low, rating_high, cost_low, cost_high, location):
        Node.__init__(self)
        self.start_date = start_date
        self.end_date = end_date
        self.rating_low = rating_low
        self.rating_high = rating_high
        self.cost_low = cost_low
        self.cost_high = cost_high
        self.location = location

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,new_data):
        if self.head is not None:
            new_data.next = self.head
            self.head = new_data
        else:
            self.head = new_data

    def findRating(self, tourist):
        temp = self.head
        while temp is not None:
            if temp.rating >= tourist.rating_low and temp.rating <= tourist.rating_high:
                print "You can reserve " + temp.name
            temp = temp.next
        print "Found all hotels. "




def loadhoteldata():
    with open('hote.json') as data_file:
        hotel_info = json.load(data_file)
    list_ = LinkedList()
    rest_house = Hotel("Multi Rest House", hotel_info["Multi Rest House"]["location"], hotel_info["Multi Rest House"]["rating"])
    list_.append(rest_house)
    dilijan_resort = Hotel("Dilijan Resort", hotel_info["Dilijan Resort"]["location"], hotel_info["Dilijan Resort"] ["rating"])
    list_.append(dilijan_resort)
    mariot = Hotel("Mariot", hotel_info["Mariot"]["location"], hotel_info["Mariot"] ["rating"])
    list_.append(mariot)
    opera = Hotel("Opera", hotel_info["Opera"]["location"], hotel_info["Opera"] ["rating"])
    list_.append(opera)


    return list_

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




def main():
    #call function loading hotel data
    #call function(s) asking user for inputs & storing inputs in json file
    hotels = loadhoteldata()
    tourist = touristInput()
    hotels.findRating(tourist)
    print ""



main()
