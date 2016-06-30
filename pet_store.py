def fish_store(gold, beta, shark, puffer, jelly, plecostomus, angler):
	gold_price = gold * 100
	beta_price = beta *10000
	shark_price = shark * .10
	puffer_price = puffer * 2
	jelly_price = jelly * .25
	plecostomus_price = plecostomus *1000000
	angler_price = angler* 5
	total_fish = gold + beta + shark + puffer + jelly + plecostomus + angler
	total_price = gold_price+ beta_price + shark_price  + puffer_price + jelly_price + plecostomus_price + angler_price
	print("Your order of {} fish is ${}".format(total_fish, total_price))
	return(total_price)
fish_store(10, 4, 317, 89, 39, 4, 20)

