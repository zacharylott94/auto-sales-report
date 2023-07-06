#!/bin/bash
SALESFILE="./sales.csv"
date --date="last month" "+%m %Y" | ./getReport.py >> $SALESFILE
