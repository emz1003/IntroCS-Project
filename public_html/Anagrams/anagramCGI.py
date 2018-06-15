#!/usr/bin/python

import cgi
import itertools

fin = open("/etc/dictionaries-common/words", 'r')
words = map(str.strip, fin.readlines())
words = map(str.lower, words)
fin.close
def htmlTop():
    print '''Content-type:text/html\n\n
          <!DOCTYPE html>
          <html lang="en-US">
                <head>
                        <meta charset="utf-8" />
                        <title> Process Name </title>
                </head>
                <body>'''

def htmlTail():
    print '''</body>
            </html>'''

def getData():
    formData = cgi.FieldStorage()
    word = formData.getvalue('word')
    return word


def main():
    
    s = getData()
    htmlTop()
    print "<ol>"
    for w in itertools.permutations(s):
        w = ''.join(list(w))
        if w in words:
            print "<li>",w,"</li>"
    print "</ol>"
    htmlTail()
    


if __name__ == "__main__":
    try:
        main()
    except:
        cgi.print_exception()



