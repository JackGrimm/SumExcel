# SumExcel
A small program that I use to see which numbers in a string list add up to a goal, while allowing some rounding.

This is my first public git program, so it is work in progress. There are many changes to be made to optimize the code. 

The input is a string of numbers seperated by a comma, the goal number as a string, and a leeway number string.

Example Input: Calculations("1.0,2,3.1,4,5,6,",
                            "10",
                            "0.5")

The input strings are all cleaned and the input list is seperated into an array. 
Calculations are done with recursion to see what numbers add up to the goal. 
The output is an array that contains all the arrays of combinations that add up to the goal number. 

Example Output:[
                [1.0, 2.0, 3.1, 4.0], 
                [1.0, 3.1, 6.0], 
                [1.0, 4.0, 5.0], 
                [2.0, 3.1, 5.0], 
                [4.0, 6.0]
                ]

The reason I've used the inputs as strings is the majority of work I use this for relies on a copy/paste from Excel.
These strings often contains whitespace characters in multiple forms. 

This is useful in accouting where you have an individual list of expenses, and a total, but you don't know the exact allocation that was used.

The only drawback that I have is that the calculations start taking exponentially longer when the input list is more than 20. 
