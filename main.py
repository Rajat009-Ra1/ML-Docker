import joblib

mind = joblib.load('salary.pk1')

x=float(input("Year Of Experience ? "))

y= float(x)

y= mind.predict([[x]])

print("Estimated Salary: ",y)
