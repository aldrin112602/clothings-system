import sys
womenClothing = ['Shirt', 'Dress', 'Skirt', 'Jeans', 'Tops', 'Trousers', 'Blouse']
womenClothingPrice = [500, 700, 350, 750, 300, 750, 400]
menClothing = ['Shirt', 'Polo', 'Shorts', 'Jeans']
menClothingPrice = [500, 600, 400, 800]

def getPriceForWomen(x):
	price = int(womenClothingPrice[x])
	return  price
	
def getPriceForMen(x):
	price = int(menClothingPrice[x])
	return  price
	
def getChange(price):
	money = float(input('Enter amount of money: '))
	change = money - price
	return  change
	
	
print("1. Women's clothing")
print("2. Momen's clothing")
x = int(input('Select: '))
if x == 1:
	print("Women's clothing:")
	i = 1
	for item in womenClothing:
		print(str(i) + '. ' + item)
		i += 1
else:
	print("Men's clothing:")
	i = 1
	for item in menClothing:
		print(str(i) + '. ' + item)
		i += 1
		
i = int(input('Select type of clothing: '))

price = 0
if x == 1:
	#For women
	price = getPriceForWomen((i - 1))
else:
	price = getPriceForMen((i - 1))

i = int(input('Enter number of item: '))
total = price * i
print('The total price of the item is: ', total)
c = getChange(total)
print('Your change is: ', c)
