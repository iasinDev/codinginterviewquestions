# Minimum Distance


Company| Amazon
---|---
Date|10/19/2018
Platform|AspiringMinds

Amazon Fresh is a grocery delivery services that offers consumers the option of purchasing their groceries online and having them delivered on schedule. The Amazon Fresh team is planning a route for a delivery truck to deliver customer orders in the city of Techlandia. The planner will create a delivery area for each order to effectively paln the route. The area is abstracted as a grid. Not all locations are accessible by road. The truck only needs to make a single delivery.

Write an algorithm to determine the minimum distance required for the truck to deliver the order.

Assumptions:
* Some places in the delivery area connot be accessed by the driver, as there are no roads into those locations.
* The delivery area can be represented as a two-dimensional grid of integers, where each integer represents one cell.
* The truck must start from the top-left corner of the area, which is always accessible, and can move one cell up, down, left, or right at a time.
* The truck must navigate around the areas without roads and cannot leave the area.
* The accessible areas are represented as 1, areas with without roads are represented by 0 and the order destination is ... 

#####Output
Return an integer representing the total distance traversed to deliver the order else return -1

#####Constraints
_1 <= numRows, numColumns <= 1000_

#####Example
Input:
_numRows_ = 3
_numColumns_= 3
_area_ = 
[[1, 0, 0], 
[1, 0, 0], 
[1, 9, 1]]

######Output:
3

Explanation:
Starting from the top-left corner, the truck traversed the cells (0,0) -> (1,0) -> (2,0) -> (2,1). The truck traversed the total distance 3 to deliver the order.
So, the output is 3.