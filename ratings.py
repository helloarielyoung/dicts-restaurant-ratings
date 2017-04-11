"""Restaurant rating lister."""


# put your code here
import sys

file_name = sys.argv[1]


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
def print_ratings(restaurant_info):
    """Print statement on restaurant rating."""
#split here into two functions
    #print the result in nice sentences in alphabetical order
    #(hint use .items and sorted())

    for restaurant, rating in sorted(restaurant_info.iteritems()):
        print "%s is rated at %s." % (restaurant, rating)


restaurant_info = get_ratings_data(file_name)
print_ratings(restaurant_info)
