# String Formatting in Python 

# There are four different ways to string formatting 

a1 = "IndianTechProgrammer"
print(f"hello {a1}")

a2 = "hello {}".format("IndianTechProgrammer")
a3 = "hello {}".format(a1)
print(a2)
print(a3)

a4 = "hello {}"
print(a4.format("IndianTechProgrammer"))
print(a4.format(a1))

a5 = "hello {a}"
print(a5.format(a = "IndianTechProgrammer"))