#!/usr/bin/python

import cgi
import matplotlib.pyplot as plt
def htmlTop():
    print '''Content-type:text/html\n\n
    <!DOCTYPE html>
    <html lang="en-US">
        <head>
            <meta charset="utf-8" >
            <title> Population Data Analysis </title>
        </head>
        <body>
        <h1> Population Data Analysis of the World by Region</h1>'''


def htmlTail():
    print '''</body>
        </html>'''
def getData():
    file = open("International_data-2.csv",'r')
    data = file.readlines()
    file.close()
    return data

def main():
    lines = getData()
    htmlTop()
    for i in range(1,4):
        if i == 1:
            print '''<a href={}>Link to Source</a> <br>'''.format(lines[i])
        else:
            print str(lines[i]) + "<br>"
    regions = dict()
    for value in lines[8:16:-1]:
        value = value.split(",")
        print str(value)
        regions[value[1]] = value[2:]

    # print ''' <form action="filterRegion.py" method="post">
    #           <select name="region" id=regionid">'''
    print regions
    for i in regions.values():
        print str(i)
    # <option value="world">World Population</option>
    # <option value=""></option>
    # <option value=""></option>
    # <option value=""></option>
    # <option value=""></option>
              # '''</select>
              # <input type="submit" value="Submit">
              # </form>
              # '''
    htmlTail()


if __name__ == '__main__':
    try:
        main()
    except:
        cgi.print_extension()
