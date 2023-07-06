#!/bin/python3
import mechanicalsoup
import sys
# fill in your username, password, and URL as strings
username =
password =
thriftcartURL =
if len(sys.argv) < 2:
    month, year = sys.stdin.read().rstrip().split(" ")
else:
    month = sys.argv[1]
    year = sys.argv[2]
monthInt = int(month)
lookup = [
    31,
    28,
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31
        ]
browser = mechanicalsoup.StatefulBrowser()
browser.open(thriftcartURL)
browser.select_form()
browser["username"] = username
browser["password"] = password
browser.submit_selected()
browser.follow_link("posreports")
browser.follow_link("admin_dailysummaryreport.php")
browser.select_form()
browser["daycount"] = lookup[monthInt-1]
browser["startdate"] = month+"-01-"+year
browser.submit_selected()
page = browser.page
result = page.find(class_="bottomrow").findChildren()[3].text
browser.follow_link("logout")
print("{}-{},{}".format(month,year,result.translate(str.maketrans('','','$,'))))

