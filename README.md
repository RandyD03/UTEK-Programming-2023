**Problem Statement**

Research shows that Mars is the most liveable planet in our solar system after Earth. Since Earth is becoming less liveable due to global warming and the water crisis, humans are considering moving. To start off, some kingdoms start moving to Mars, including the Hadfield Kingdom, the Garneau Kingdom, and the Chretien Kingdom. However, their rulers don’t get along. Every kingdom wants to inhabit exactly one city on Mars to stay amongst itself. All members of the kingdom are to build houses for their families within that city. Their houses will be organized based on the hierarchy of the kingdom from highest to lowest ranks (e.g. the King/Queen would have the highest rank). The kingdom's ruler will not be happy if all of the homes are not in the order of hierarchy, or if a home is not in the city where the rest of the kingdom is located.

The members of the kingdom have all arrived in a single spaceship. As a result, some of the families are with families from other kingdoms. Your job is to group everyone to be with families of only their own kingdom and sort them based on hierarchy within their kingdom. The final grouping will decide the order and place of the houses being built.  

How can you reorganize the citizens most efficiently such that all rulers will be happy when the houses are built?

Problem Description
The problem has been broken down into parts, so by the time you complete all parts, a solution to the main problem will be formed.

Part 1
You are to organize the families so that each kingdom’s members reside within that kingdom’s city, which means all elements that represent the same kingdom (i.e. start with the same letter) are next to each other. You must also order the kingdoms alphabetically. One way to verify that you have placed the elements correctly is that for n kingdoms, you can clearly draw n-1 lines that separate the kingdoms, where the prefix of the element on the right comes later in the alphabet than the one on the left. 

Below are examples of invalid arrangements for a2 a1 a3 b1 b3 b2 c3 c2 c1. The red elements are the ones with the issue.

a2 b1 a3 a1 b3 b2 c3 c2 c1
a2 c1 a3 b1 b3 b2 c3 c2 a1
c1 c2 c3 b2 b1 b3 a1 a2 a3

In the first two examples, there are 3 kingdoms, and you cannot draw 2 lines such that each kingdom is separated from the other. In the third example, while lines can be drawn to separate the kingdoms, they are not in alphabetical order as c is before b and b is before a.

Additionally, you don’t want to unnecessarily cause hassle to the new inhabitants. So, you will need to perform the smallest number of swaps to achieve a valid arrangement. Note that in this part, you do not need to account for the number associated with each element (the suffix).

Part marks will be provided if only some constraints are met. 

Example Input:
3
3
b2 c1 a3 b1 b3 a2 c3 c2 a1
# There are 3 cities, each with 3 homes, and the order in which the humans arrived is provided.

Example Output:
Swap a1 and c1
Swap b2 and a2

Part 2
Now, the kingdoms’ rulers have decided that they not only want their own city but also want the citizens to be arranged in a manner that respects their rank. Hence, you are now to ensure that in addition to the constraints of Part 1, the ranks of the elements within each kingdom’s city go from highest to lowest as you move left to right, where a higher rank is represented by a lower number. This means that all elements with the same letter should be ordered such that their numbers are in increasing order. This is an example of an invalid arrangement for a1 a2 a3 b1 b2 b3 c1 c2 c3. The red elements are the ones with the issue.

a1 a3 a2 c1 b2 b3 b1 c2 c3

In this example, a3 has an element of higher rank to its right. c1 and b3 are surrounded by people who are not from their kingdom (remember the constraint from Part 1!). 

Part marks will be provided if only some constraints are met. 

Input: Format as given in Part 1.
Output: Format as given in Part 1. 
Part 3
The disdain amongst the kingdoms has grown worse. They not only do not want to reside only amongst their own people, but also want to avoid crossing anyone from a different kingdom as much as possible. Hence, in addition to the constraints in Part 1 and Part 2, the swaps you perform have associated costs. 

Note that we defined a person’s correct city as the group of elements that belong to that kingdom in the final, organized array. 

To demonstrate the concept of the correct city, consider the following input:
b1 a2 c2 b1 b2 a1 c1 a3 c3

Here, there are 3 letters, where each letter has 3 associated numbers. The final, organized array should look like the following:

a1 a2 a3 b1 b2 b3 c1 c2 c3
0      1     2    3      4     5     6     7     8

The positions of the elements are written in bold below each element. Thus, the correct city for any element with a prefix a is positions 0, 1, and 2. Likewise, the correct cities for elements with prefixes b or c are 3, 4 and 5, and 6, 7, and 8 respectively.

The following outlines the rules for the cost:

A swap that results in at least person not being in their correct city has a cost of 10
A swap in which the above is not true has a cost of 5

Part marks will be provided if only some constraints are met. 
Input: Format as given in Part 1.
Output: Format as given in Part 1 and line showing total cost (Format: Total cost is 10)
