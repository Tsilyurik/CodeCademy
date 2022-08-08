## calculate shipping cost 
## Tsilyurik Evhen
## Loky_cooper
weight = 100.8
total_cost = 0
cost = 0
### “Ground Shipping”
if weight <= 2 :
  cost = 20 + 1.5*weight
elif weight <= 6 :
  cost = 20 + 3.0*weight
elif weight <= 10 :
  cost = 20 + 4.0*weight
elif weight > 10 :
  cost = 20 + 4.75*weight
else : print(" ur weight so empty")

print( 'Simple cost = ' + str(cost) )

### premium ground shipping.
prem_cost = 125.0
print("Premium cost is = " + str(prem_cost))
 ### Drone shipping
drone_cost = 0
if weight <= 2 :
  drone_cost = 4.5*weight
elif weight <= 6 :
  drone_cost = 9.0*weight
elif weight <= 10 :
  drone_cost = 12.0*weight
elif weight > 10 :
  drone_cost = 14.25*weight
else : print(" ur weight so empty")

print( 'Drone shipping will cost for you = ' + str(drone_cost) )

### cheapest method 

total_cost = prem_cost
if total_cost > cost :
  total_cost = cost
if total_cost > drone_cost :
  total_cost = drone_cost

print("Lowest price for shipping is : " + str(total_cost))
