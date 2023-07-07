#!/bin/bash
#Be sure to change where you want your sales file to point to
date --date="last month" "+%m %Y" | ./getReport.py >> ~/automaticSales/sales.csv
