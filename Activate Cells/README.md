# Activate Cells

Company| Amazon
---|---
Date|10/19/2018
Platform| aspiringminds.com

A colony of eight houses, represented as cell are arranged in a stright line. Each day every cell competes with its adjacent cells (neighbours). An integer value of 1 represents an active cell and value of 0 respresents an inactive cell. If both the neighbours are either active or inactive, the cell becomes inactive the next day; otherwise it becomes active on the next day. The two cells on the ends have a singe adjacent cell, so the other adjacent cell can be assumed to be always inactive. Even after updating the cell state, its previous state is considered for updateding the state of other cells. The cell information of all cells should be updated simulataneously.

Write an algorithm to output the state of the cells after the given number of days.

####Input
The input to the function/method consists of two arguments - 
* _states_, a list of integers representing the current state of cell.
* _days_, an integer representing the number of days.

#####Output
Return a list of integers representing the state of cells after the given number of days.

