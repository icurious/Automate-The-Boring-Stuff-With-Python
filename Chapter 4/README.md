**Comma Code**


`Say you have a list value like this:`
`spam = ['apples', 'bananas', 'tofu', 'cats']`

`Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with and
inserted before the last item. For example, passing the previous spam list to
the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it.`

**Character Picture Grid**

Say you have a list of lists where each value in the inner lists is a one-character
string, like this:

```
grid = 
[      
['.', '.', '.', '.', '.', '.'],  
['.', 'O', 'O', '.', '.', '.'],  
['O', 'O', 'O', 'O', '.', '.'],  
['O', 'O', 'O', 'O', 'O', '.'],  
['.', 'O', 'O', 'O', 'O', 'O'],  
['O', 'O', 'O', 'O', 'O', '.'],  
['O', 'O', 'O', 'O', '.', '.'],  
['.', 'O', 'O', '.', '.', '.'],  
['.', '.', '.', '.', '.', '.']  
]  

You can think of grid[x][y] as being the character at the x- and
y-coordinates of a “picture” drawn with text characters. The (0, 0) origin
will be in the upper-left corner, the x-coordinates increase going right,
and the y-coordinates increase going down.
Copy the previous grid value, and write code that uses it to print the image.


 ..OO.OO..    
 .OOOOOOO.    
 .OOOOOOO.  
 ..OOOOO..  
 ...OOO...  
 ....O....  
 
