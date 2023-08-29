NO GENERATIVE AI SUCH AS CHATGPT, BARD, BINGCHAT ETC. IS ALLOWED!
SOLUTIONS ARE MEANT TO BE YOUR OWN ATTEMPT AT THE PROBLEM AND PLAGIARISM USING CODE SNIPPETS FROM ONLINE IS NOT ALLOWED!

You will be required to also leave comments that clearly explain how your code works.

-------------------------------------------------------------------------------------------------------------------------
PROBLEM STATEMENT:

Create a function that takes the RGB values of a colour and converts it to the corresponding HEX value for that colour.

The function should take 3 arguments, the red value, the green value and the blue value. 

The function should return the HEX value represented as a string. Example inputs and outputs can be found below:

rgbToHex(255, 255, 255) --> "FFFFFF"
rgbToHex(255, 255, 300) --> "FFFFFF"
rgbToHex(0, 0, 0)       --> "000000"
rgbToHex(148, 0, 211)   --> "9400D3"

The use of any prebuilt hex conversion functions/libraries WILL NOT be allowed to solve this problem.

Extra credit is awarded for code that takes edge cases into account.
Extra credit is awarded for writing unit tests. These unit tests should also test for the edge cases.

If you have finished this challenge within the time limit, write a second function that converts from RGB to CMYK.

The following are examples of inputs and outputs:

rgbToCmyk(255, 255, 255) --> [0, 0, 0, 0]
rgbToCmyk(100, 50, 75)   --> [0, 50, 25, 61]
rgbToCmyk(0, 0, 0)       --> [0 , 0, 0, 100]
