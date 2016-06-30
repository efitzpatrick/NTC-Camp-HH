#Bottle Cap Ordering
# Emaline ordered 300,000 bottle caps
# 300 boxes of 1000
# 10 boxes of 100
counter = 0
for big_box in range(300):
	for medium_box in range(100):
		for small_box in range(10):
			counter = counter +1

print(counter)