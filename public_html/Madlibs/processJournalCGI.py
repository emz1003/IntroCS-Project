#!/usr/bin/python

import cgi
import cgitb

cgitb.enable()

def htmlTop():
    print '''Content-type:text/html\n\n
          <!DOCTYPE html>
          <html lang="en-US">
                <head>
                        <meta charset="utf-8" />
                        <title> Journal </title>
                </head>
                <body>'''

def htmlTail():
    print '''</body>
            </html>'''

def convertToDict(fs):
    ans = dict()
    for key in fs:
        ans[key] = fs.getvalue(key)
    return ans


def main():
    formData = cgi.FieldStorage()
    data = convertToDict(formData)
    fileIn = open('journal.txt','r')
    text = fileIn.read()
    htmlTop()
    print text.format(**data)
    htmlTail()
    fileIn.close()



if __name__ == "__main__":
    try:
        main()
    except:
        cgi.print_exception()
