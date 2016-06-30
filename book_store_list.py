def book_store(juvenile, ya, new_age, picture, adult):
	book_store_list = []
	book_store_list.append(10 *juvenile)
	print(book_store_list)
	book_store_list.append(20 *ya)
	print(book_store_list)
	book_store_list.append(15*new_age)
	book_store_list.append(3.75 * picture)
	book_store_list.append(19.50 * adult)
	print(book_store_list)

	total_price= 0
	for i in range(4):
		item_price = book_store_list[i]
		total_price = total_price + item_price

	total_price = 0
	for item_price in book_store_list:
		print(item_price)
		total_price = total_price + item_price
	

	return(total_price)


price = book_store(20, 3000, 500, 98, 2)
name = "Ellie"
date_delivered = "6/16/16"
approval = "Amy"
print("To be ordered to {}.\nTo be delived by {}.\nApproved by {}. \nPrice: {}".format(name, date_delivered, approval, price))