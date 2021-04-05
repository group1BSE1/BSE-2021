hours = int(input('Enter hours: '))
rate = int(input("Enter rate: "))
pay = rate * hours
if hours>40:
#extra time
  nhours = hours - 40
#etra pay
  npay = nhours*(10*1.5)
#pay for initial 40 hours 
  nnpay = 40 * rate
#new pay
  newpay = nnpay + npay
  print(newpay)
else: print(pay)