Flavors = ["Kettle", "Buttered", "Plain", "Caramel"]
Orders = []
Flavor = 0
Order = 0
Box_Sales = "How many boxes of" Flavors[Flavor] "were sold?" 
for Flavor in Flavors:
    Orders.append(input(Box_Sales))
    