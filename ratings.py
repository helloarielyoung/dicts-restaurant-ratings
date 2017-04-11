"""Restaurant rating lister."""


# put your code here
import sys

file_name = sys.argv[1]

#need to move the restaurant_info dictionary OUT of the function so
#we will be able to get it from the other functions(to add user rating)

def get_ratings_data(file_name):
    """Return dictionary with restaurant and rating data"""
    #read the text in the file
    ratings = open(file_name)

    #split the lines at : and put in dictionary
    restaurant_info = {}

    for line in ratings:
        restaurant, rating = line.split(":")
        restaurant_info[restaurant] = rating.rstrip()
    return restaurant_info

        #NOTE:  rating is a string, which is fine for this implementation
        #but if later we need to order by rating we'll have to change to int
def get_user_rating():
    """Gets user rating of a restaurant"""

    #ask user for rating
    print "Please rate a restaurant!"
    new_restaurant = raw_input("Enter a restaurant name:")
    
    #check that the rating is an integer and if not, re-prompt
    while True:
        try: 
            new_rating = int(raw_input("Enter rating for restaurant:"))
            break
        except ValueError: 
            print "Oops! Please enter a number."

    #return the restaurant and rating
    return new_restaurant, new_rating

#new function to add new_restaurant and new_rating to the dictionary

def print_ratings(restaurant_info):
    """Print statement on restaurant rating."""
#split here into two functions
    #print the result in nice sentences in alphabetical order
    #(hint use .items and sorted())

    for restaurant, rating in sorted(restaurant_info.iteritems()):
        print "%s is rated at %s." % (restaurant, rating)




restaurant_info = get_ratings_data(file_name)
get_user_rating()
# print_ratings(restaurant_info)

