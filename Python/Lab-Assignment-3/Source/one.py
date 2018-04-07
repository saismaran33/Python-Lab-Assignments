#Importing csv, numpy, lda
import csv
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis


x_axis = []
y_axis = []
# Writing the data into x_axis and y_axis
with open("dataset.csv") as f:
    csvfile = csv.reader(f, delimiter=',')
    next(csvfile)
    for line in csvfile:
        loan = float(line[0])
        deposit = float(line[1])
        amount = float(line[2])
        interest = float(line[3])
        area = 1 if float(line[4]) > 0 else 0
        x_axis.append([loan, deposit, amount, interest])
        y_axis.append(area)
# Converting the data in x_axis and y_axis  into numpy array
np_x = np.array(x_axis)
np_y = np.array(y_axis)
# Performing LDA
model = LinearDiscriminantAnalysis()
model.fit(np_x, np_y)
# prediction that loan may be issued
loan = 50
deposit = 100
interest = 0.1
amount = 100
print("To meet the loan requirements: "
      "loan [%f] should be in the particular range, "
      "deposit [%f] must be assigned as per the loan, "
      "interest [%f] in percentage is calculated,"
      " and  amount [%f] in certain limit" % (loan, deposit, amount, interest))
if model.predict([[loan, deposit, amount, interest]])[0]:
    print("Loan may be issued.")
else:
    print("Loan may not be issued.")
# prediction that loan may not be issued
loan = 100
deposit = 500
interest = 0.2
amount = 1000
print("To meet the loan requirements: "
      "loan [%f] should be in the particular range, "
      "deposit [%f] must be assigned as per the loan, "
      "interest [%f] in percentage is calculated,"
      " and  amount [%f] in certain limit" % (loan, deposit, amount, interest))
if model.predict([[loan, deposit, amount, interest]])[0]:
    print("Loan may be issued.")
else:
    print("Loan may not be issued.")