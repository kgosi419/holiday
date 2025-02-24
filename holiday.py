''' Objective off the program is to calculate the total cost of the holiday
based on the user's choices'''

# Functions to calculate the totals

# Function for the hotel cost


def hotel_cost(days_nights):
    return (days_nights * 500)

# Function for plane cost


def plane_cost(city):
    if city.lower() == 'a':
        return 800
    elif city.lower() == 'b':
        return 1350
    elif city.lower() == 'c':
        return 1000
    else:
        print("invalid city")

# Function for the car rental


def car_rental(rental_days):
    return (rental_days * 250)

# Function for the total cost of the holiday


def total_holiday_cost(days_nights, city, rental_days):
    return hotel_cost(days_nights) + plane_cost(city) + car_rental(rental_days)


# Get input from user and give out the total cost
city = input("Select which city you are traveling to: (options: a. b. c.): ").lower()
cost = plane_cost(city)
while city.lower() not in ["a", "b", "c"]:
    print("option invalid")
    city = input("Select which city you are traveling to: (options: a. b. c.):").lower()

print(f"Plane cost for the selected city: R{cost}")

nights = int(input("How many nights: "))
print(f"Total cost for {nights} nights: R{hotel_cost(nights)}")
car = int(input("car rental cost per day: "))
print(f"Cost of car rental: R{car_rental(car)}")

print(f"The holiday will cost you: R{total_holiday_cost(nights, city, car)}")
