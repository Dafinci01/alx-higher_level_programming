#!/usr/bin/python3

"""defines a peak finding algorithm"""


def find_peak(list_of_integers):
    """return a peak ina alist of unsoerted integers"""
    if list_of_integers == []:
        return None

#get the size of the list 
    size = len(list_of_integers)
    if size == 1 #if there is only one element that element is peak
        return list_of_integers[0]
#if there are two elements. return the maximum as peak
    elif size == 2:
        return max(list_of_integers)
#calculate the middle index of the list 
    mid = int(size / 2)
#get the middle element
    peak = list_of_integers[mid]
    #check id the middle  element is greteter than its neighbors
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak 
    elif  peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
