# Name: Thi Van Anh Duong
# Student ID: 90023112
# Major: Information Technology
# program.py - My Assignment 1 with netflix.csv
#

import matplotlib.pyplot as plt
import numpy as np

def findList(a):
    result = []
    for i in range(len(rawData)):
        if (rawData[i][a] not in result):
            result.append(rawData[i][a])
    return(result)


def addFilterGenre(ogenre):
    result = []
    for i in range(len(rawData)):
        if rawData[i][6] == ogenre:
            result.append(rawData[i])
    return(result)


def minvalid(minYear):
    while minYear < 1925 or minYear > 2021:
        print("Error! This year is not available.")
        print()
        minYear = int(input("Please choose a minimum year: "))
    return(minYear)


def maxvalid(minYear,maxYear):
    while maxYear > 2021 or maxYear < 1954 or maxYear < minYear:
        print("Error! This year is not available.")
        print()
        maxYear = int(input("Please choose a maximum year: "))
    return(maxYear)


def addFilterReleaseYear(minYear,maxYear):
    result = []
    for i in range(len(rawData)):
        if int(rawData[i][3]) >= minYear and int(rawData[i][3]) <= maxYear:
            result.append(rawData[i])
    return(result)


def addFilterRating(low_position,high_position):
    result = []
    for i in range(len(rawData)):
        position = -1
        for j in range(len(rating)):
            if rawData[i][4] == rating[j]:
                position = j
        if position != -1 and position <= high_position and position >= low_position:
            result.append(rawData[i])
    return(result)


def printTotal(rawData):
    total = 0 
    for i in range(len(rawData)):
        total += 1
    return(total)


def genreGraph(listGenre,count,title,xlabel,ylabel):
    plt.subplot(211)
    plt.bar(listGenre,count)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45, ha='right')
    
    plt.show()

def yearGraph(listYear,count,title,xlabel,ylabel):
    plt.subplot(211)
    plt.bar(listYear,count, color = 'red')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45, ha='right')
    
    plt.show()

def ratingGraph(listRating,count,title,xlabel,ylabel):
    plt.subplot(211)
    plt.plot(listRating,count,'r--')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45, ha='right')
    plt.grid()

    plt.show()


def countFilms(listFilter,a):
    count = np.zeros(len(listFilter))
    for i in range(len(rawData)):
        for j in range(len(listFilter)):
            if listFilter[j] == rawData[i][a]:
                        count[j] += 1
    return(count)
# Reading The File

netfile = open('netflix.csv','r')
data = netfile.readline() # This line is for read the first line and ignore it
data = netfile.readline() # Start working at this line

rawData = [] # Variable stores all movies information
minYear = 1925
maxYear = 2021

while data:
    splitline = data.strip().split(',')
    rawData.append(splitline)
    data = netfile.readline()

netfile.close()

# Display A Menu

print()
print('~~~~~~~~WELCOME TO MY NETFILX PROGRAM  ٩(^‿^)۶ ~~~~~~~~')
print()
print()
choice = input("Enter the option - (A)dd filters, (P)rint names, (G)raph data or e(X)it: ")
print() 
while choice.upper() != "X":

    if choice.upper() == "A":
        print()
        print('~~~~~~~~NOW LET\'S ADD A FILTER THAT YOU WANT ಠ_ృ  ~~~~~~~~')
        print()
        filt = input("Please choose a filter type - (G)enre, Release (Y)ear, (R)ating:  ").upper()
        print()

# Add Filter Genre

        if filt == "G":
            genre = findList(6)
            print('All genres : ', genre)
            print()
            ogenre = input("Choose genre you want: ")
            print()
            checkgenre = False
            for g in range(len(genre)):
                if ogenre == genre[g]:
                    checkgenre = True
            if checkgenre == False:
                print("Please enter a valid genre !")
                print(" ಥ_ಥ ")
                print()
                ogenre = input("Choose genre you want: ")
                print()
            else:
                rawData = addFilterGenre(ogenre)

# Add Filter Release Year

        elif filt == "Y":
            print("*~~~~~~*~~~~~*~~~~~~*~~~~~~*~~~~~~~*~~~~~~~*")
            print('Choose a year between',minYear, 'and',maxYear,': ')
            print()
            minYear = int(input("Please choose a minimun year: "))
            minYear = minvalid(minYear)

            maxYear = int(input("Please choose a maximun year: "))
            maxYear = maxvalid(minYear,maxYear)
            print()

            rawData = addFilterReleaseYear(minYear,maxYear)

# Add Filter Rating

        elif filt == "R":
            rating = ['G','PG','PG-13','M','MA','R']
            print('Rating list: ',rating)

            lowrate = input('Choose a low rating: ').upper()
            for l in range(len(rating)):
                if rating[l] == lowrate:
                    low_position = l
            while True:
                highrate = input('Choose a high rating: ').upper()
                for h in range(len(rating)):
                    if rating[h] == highrate:
                        high_position = h
                if low_position < high_position:
                    break
                print('Error ! Please enter again !')

            rawData = addFilterRating(low_position,high_position)


             


        else:
            print('')
            print("We don\'t have this filter ! (╥﹏╥) ")
            print()
            filt = input("Please choose a filter type - (G)enre, Release (Y)ear, (R)ating or e(X)it:  ").upper()

# Printing names

    elif choice.upper() == "P":
        for i in range(len(rawData)):
            print("Movies: \n" + rawData[i][0] + "  :  " + rawData[i][7])
            print()
        print('Total movies:',printTotal(rawData))
        print()

# Graphing the result
    elif choice.upper() == "G":
        gchoice = input("Choose a graph type: (G)enre, Rating (Y)ear, (R)ating: ").upper()
        print()

# Genre Graph

        if gchoice == "G":
            listGenre = []
            for g in range(len(rawData)):
                listGenre.append(rawData[g][6])
            
            genreGraph(listGenre,countFilms(listGenre,6),'Genre Graph','Genre','Number of Movies')
        
# Release Year  Graph

        elif gchoice == "Y":
            listYear = [] #genre in range of years
            for y in range(len(rawData)):
                listYear.append(rawData[y][6])

            yearGraph(listYear,countFilms(listYear,6),'Years Graph','Genre','Number of Movies')

# Rating Graph

        elif gchoice == "R":
            listRating = []
            for r in range(len(rawData)):
                listRating.append(rawData[r][4])
            
            ratingGraph(listRating,countFilms(listRating,4),'Rating Graph','Rating','Number of Movies')
        else:
            print()
            print("Error ! Please choose a valid graph type (╥﹏╥)")


        
# Exit
    else: 
        print("Please choose a valid option ! (╥﹏╥)")
        print()
    choice = input("Enter the option: (A)dd filters, (P)rint names, (G)raph data or e(X)it: ")


