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


def activity_cost(activity, days_nights):
    activity_costs = {
        'dive': 1000,
        'hike': 500,
        'city_tour': 300
    }

    if activity.lower() in activity_costs:
        return activity_costs[activity.lower()] * days_nights
    else:
        print("Invalid activity selected")
        return 0

# Function for the total cost of the holiday

def total_holiday_cost(days_nights, city, rental_days, activity):
    return (hotel_cost(days_nights) +
            plane_cost(city) +
            car_rental(rental_days) +
            activity_cost(activity, days_nights))


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

activity = input("What activity would you like to do? (dive, hike, city_tour): ")
print(f"Cost of activity: R{activity_cost(activity, nights)}")

total_cost = total_holiday_cost(nights, city, car, activity)
print(f"The holiday will cost you: R{total_cost}")
