"""Restaurant rating lister."""


# put your code here
import sys

file_name = sys.argv[1]


def get_ratings(file_name):
    #read the text in the file
    ratings = open(file_name)

    #split the lines at : and put in dictionary
    restaurant_info = {}

    for rating in ratings:
        restaurant = ratings.split(":")

    #put the results in a dictionary
    #print the result in nice sentences in alphabetical order (hint use .items and sorted())   
