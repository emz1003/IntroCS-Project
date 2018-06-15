#!/usr/bin/python

import cgi
import random

def htmlTop():
    print '''Content-type:text/html\n\n
    <!DOCTYPE html>
    <html lang="en-US">
        <head>
            <meta charset="utf-8" >
            <link rel="stylesheet" type="text/css" href="mystyle.css" >
            <title>Magic 8 Ball </title>
        </head>
        <body>'''


def htmlTail():
    print '''</body>
        </html>'''

def main():
    L = ['It is certain'
    ,'It is decidedly so'
    ,'Without a doubt'
    ,'Yes definitely'
    ,'You may rely on it'
    ,'You can count on it'
    ,'As I see it, yes'
    ,'Most likely'
    ,'Outlook good'
    ,'Yes'
    ,'Signs point to yes'
    ,'Absolutely'
    ,'Reply hazy try again'
    ,'Ask again later'
    ,'Better not tell you now'
    ,'Cannot predict now'
    ,'Concentrate and ask again'
    ,'Don\'t count on it'
    ,'My reply is no'
    ,'My sources say no'
    ,'Outlook not so good'
    ,'Very doubtful'
    ,'Chances aren\'t good' ]
    ans = (lambda: random.choice(L))
    htmlTop()
    print '<img src="8ball.png" width="300" alt = "hello" class="center"> '
    print '''<<input type = "button" value = "Ask the Magic 8 Ball" onclick = "alert('{}')">'''.format(ans())
    print "<a href='./8_ballCGI.py'>Ask another question</a>"
    htmlTail()


if __name__ == '__main__':
    try:
        main()
    except:
        cgi.print_exception()
