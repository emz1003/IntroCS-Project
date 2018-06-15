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
                        <title> Process Full Name </title>
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
    stories = {"cat and mouse":"getStory.html","journal":"getJournal.html","wildlife":"getNonFiction.html","fairy tale":"getFairyTale.html"}
    formData = cgi.FieldStorage()
    data = convertToDict(formData)
    htmlTop()
    for key in stories.keys():
        if data["story"] == key:
            print '''<meta http-equiv="refresh" content="0; URL='{}'" />'''.format(stories[key])

    htmlTail()



if __name__ == "__main__":
    try:
        main()
    except:
        cgi.print_exception()
