#!/usr/bin/python

import cgi

def htmlTop():
    print '''Content-type:text/html\n\n
    <!DOCTYPE html>
    <html lang="en-US">
        <head>
            <meta charset="utf-8" >
            <title>My first server-side script. </title>
        </head>
        <body>'''


def htmlTail():
    print '''</body>
        </html>'''

def main():
    htmlTop()
    htmlTail()


if __name__ == '__main__':
    try:
        main()
    except:
        cgi.print_extension()
