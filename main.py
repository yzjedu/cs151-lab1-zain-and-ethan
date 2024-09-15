

#Prompt the necessary amount of miles that the user needs to travel
required_miles = input("Enter the number of miles you need to travel:")
required_miles = float(required_miles)


#Prompt for the amount of Miles Per Gallon (MPG) that the users car has
miles_per_gallon = input("Enter the miles per gallon that your car has:")
miles_per_gallon = float(miles_per_gallon)


#Prompt for the cost of gas per gallon, for the user
gas_price = input("Enter the current gas price per gallon:")
gas_price = float(gas_price)

#Create a new calculation for the overall price.
overall_cost = (required_miles/miles_per_gallon) * gas_price


#Output the result
print("Your overall cost of gas for the trip will be:",overall_cost )

