def calculate_ticket_price_for_performer(regular_ticket_price, performer_type):

   if performer_type == "Juggler":
    discount = 0.50
    discounted_ticket_price = regular_ticket_price - (regular_ticket_price * discount)
    return discounted_ticket_price

   elif performer_type == "Fire Twirler":
    discount = 0.25 
    discounted_ticket_price = regular_ticket_price - (regular_ticket_price * discount)
    return discounted_ticket_price

   elif performer_type == "Magician":
    discount = 0.80
    discounted_ticket_price = regular_ticket_price - (regular_ticket_price * discount)
    return discounted_ticket_price

   elif performer_type == "Escape Artist":
    discount = 1.00
    discounted_ticket_price = regular_ticket_price - (regular_ticket_price * discount)
    return discounted_ticket_price

   else:
    discount = 0.20
    discounted_ticket_price = regular_ticket_price - (regular_ticket_price * discount)
    return discounted_ticket_price

print(calculate_ticket_price_for_performer(100, "Juggler")) # returns 50

print(calculate_ticket_price_for_performer(200, "Magician")) # returns 40

print(calculate_ticket_price_for_performer(10, "Tight Rope Walker")) # returns 8

print(calculate_ticket_price_for_performer(150, "Escape Artist")) # returns 0