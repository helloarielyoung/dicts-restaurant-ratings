"""Restaurant rating lister."""


# put your code here
import sys

file_name = sys.argv[1]


def get_ratings(file_name):
    #read the text in the file
    ratings = open(file_name)

    #split the lines at : and put in dictionary
    restaurant_info = {}

    for line in ratings:
        restaurant, rating = line.split(":")
        restaurant_info[restaurant] = rating.rstrip()

        #NOTE:  rating is a string, which is fine for this implementation
        #but if later we need to order by rating we'll have to change to int

    #for testing
    print restaurant_info

    #put the results in a dictionary
    #print the result in nice sentences in alphabetical order (hint use .items and sorted())   
get_ratings(file_name)
