#Taylor M. Smith
#Lucky's Furniture store has the best furniture in town!


#Creating lovely_loveseat_description variable and setting price
luckys_loveseat_description = """

Luckys loveset is the most comfortable loveseat around, it is made of tufted hand-sown wool. This loveset is 32 inches high x 40 inches wide x 30 inches deep. This loveseats come in Purple, Deep Blue, Red, or White.
"""

lucky_loveseat_price = 2200.00


#Creating a stylish_settee_description & setting price
stylish_settee_description = """

The Stylish Sette is one of our more popular pieces. It is made of faux leather on birch. This Sette is 29.50 inches high x 54.75 inches wide x 28 inches deep. This Sette comes only in Black.
"""
stylish_settee_price = 1475.00


#Creating a luxurious_lamp_description & setting price
luxurious_lamp_description = """

Lucky's Luxurious Lamps are antique and delicate, but great for smaller spaces. This lamp is made of glass and iron and is 36 inches tall. It comes in either White or Brown with cream shade.
"""

luxurious_lamp_price = 200.00

#Defining sales tax
sales_tax = .50

#Calulation the Whitman's purchase total & sales tax
Whitman_total = 0
Whitman_itemization = ""

#Adding in the price of Lucky's Loveseat
Whitman_total += 2200.00
Whitman_itemization += """

Luckys loveset is the most comfortable loveseat around, it is made of tufted hand-sown wool. This loveset is 32 inches high x 40 inches wide x 30 inches deep. This loveseats come in Purple, Deep Blue, Red, or White.
"""

#Updating the price for Lucky's Luxurious Lamp
Whitman_total += 200.00
Whitman_itemization += """

Lucky's Luxurious Lamps are antique and delicate, but great for smaller spaces. This lamp is made of glass and iron and is 36 inches tall. It comes in either White or Brown with cream shade.
"""
Whitman_tax = Whitman_total * sales_tax

Whitman_total += Whitman_tax

print("Whitman's Purchases:" + Whitman_itemization)
print("Whitman's Total:")
print(Whitman_total)