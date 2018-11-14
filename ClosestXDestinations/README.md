# Closest X Destinations


Company| Amazon
---|---
Date|10/19/2018
Platform|AspiringMinds

Amazon Fresh is a delivery service. Please write an algorithm that select the closest x destinations.

#####Output
Return a list of elements where each element of the list represents the x and y integer coordinates of the delivery destinations.

#####Constraints
_numDeliveries <= numDesitinations_

#####Note
The plan starts form the truck's location [0,0]. The distance of the truck from a delivery destination (x,y) is the square root of x^2 + y^2. If there are ties then return any of the locations as long as you satisfy returning X deliveries.

#####Example
Input:
_numDestiations_ = 3
_allLocations_ = [[1,2], [3,4], [1,-1]]
_numDeliveries_ = 2

######Output:
[[1,-1],[1,2]]

Explanation:
The distance of the truck from location [1,2] is square root(5) = 2.236
The distance of the truck from location [3,4] is square root(25) = 5