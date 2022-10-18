# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 10-18-2022
# Description: Takes as a parameter the name of a text file that contains a list of numbers, and sums the values in the
# file and writes the sum to a text file named sum.txt

def file_sum(filename):
    """Sums values in file and writes sum to sum.txt file"""
    sums = 0
    with open('numberlist.txt', 'r') as infile:
        for numbers in infile:
            sums += float(numbers)
    with open('sum.txt', 'w') as outfile:
        outfile.write(str(sums))
        return sums
