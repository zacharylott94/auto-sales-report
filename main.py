from pathlib import Path
# fill in your username, password, sales file, and URL as strings  
username = "user"
password = "pass"
thriftcartURL = "null"
file = "sales.csv"
last = "last.txt"

def getLastMonth():
  import datetime
  today = datetime.date.today()
  first = today.replace(day=1)
  last_month = first - datetime.timedelta(days=1)
  return(last_month.strftime("%m %Y"))

def getReport(str):
  import mechanicalsoup
  month, year = str.rstrip().split(" ")
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
  return "{}-{},{}".format(month,year,result.translate(str.maketrans('','','$,')))

def appendToFile(str):
   with open(file, "a") as sales:
    sales.write(str + "\n")

def updateLastRun(str):
  with open(last, "w") as lastRun:
    lastRun.write(str)

def checkLastRun(str):
  Path(last).touch()
  with open(last, "r") as lastRun:
    return lastRun.read() == str

def main():
   lastMonth = getLastMonth()
   if checkLastRun(lastMonth):
     return
   Path(file).touch()
   appendToFile(getReport(lastMonth))
   updateLastRun(lastMonth)

if __name__ == "__main__":
   main()