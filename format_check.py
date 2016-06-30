def book_store(juvenile, ya, new_age, picture, adult):
	juvenile_price = 10 *juvenile
	ya_price = 20 *ya
	new_age_price = 15 * new_age
	picture_price = 3.75 * picture
	adult_price = 19.50 * adult
	total_price = juvenile_price + ya_price + new_age_price + picture_price + adult_price
	return(total_price)


price = book_store(20, 3000, 500, 98, 2)
name = "Ellie"
date_delivered = "6/16/16"
approval = "Amy"
print("To be ordered to {}.\nTo be delived by {}.\nApproved by {}.\\tPrice: {}".format(name, date_delivered, approval, price))

price = book_store(15, 19,300, 984, 90)	
print("To be ordered to {}. To be delived by {}. Approved by {}. Price: {}".format(name, date_delivered, approval, price))
