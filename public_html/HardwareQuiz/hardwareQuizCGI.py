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
                        <title> Hardware Quiz Grader </title>
                </head>
                <body> <h1> Hardware Quiz Grade </h1>'''

def htmlTail():
    print '''</body>
            </html>'''

def convertToDict(fs):
    ans = dict()
    for key in fs:
        ans[key] = fs.getvalue(key)
    return ans
def main():
    # stories = {"cat and mouse":"getStory.html","journal":"getJournal.html","wildlife":"getNonFiction.html","fairy tale":"getFairyTale.html"}
    formData = cgi.FieldStorage()
    grade = 0
    orderans = ["c2","c1","c5","c1","c4",["c1","c2","c3","c5"],["c1","c2"],"c5",["c1","c3","c4"],"c2"]
    answers = {}
    data = convertToDict(formData)
    for num in range(10):
        answers[str(num+1)] = orderans[num]

    htmlTop()
    # print str(answers) + "<br>"
    # print str(data) + "<br>"
    print "<ol>"
    for i in data.keys():
        if data[i] == answers[i]:
            print "<li> correct <br> </li>"
            grade += 10
        elif isinstance(answers[i],list):
            print "<li> incorrect, the correct answers are choices "
            for ans in answers[i]:
                 print ans[1:]
                 if ans != answers[i][-1]:
                     print ",",

            print " <br> </li>"
        else:
            print "<li> incorrect, the correct answer is choice",answers[i][1:]," <br> </li>"
    print "</ol>"
    print "<h2> Your grade:", str(grade),"% </h2>"
    # for key in stories.keys():
    #     if data["story"] == key:
    #         print '''<meta http-equiv="refresh" content="0; URL='{}'" />'''.format(stories[key])

    htmlTail()



if __name__ == "__main__":
    try:
        main()
    except:
        cgi.print_exception()
