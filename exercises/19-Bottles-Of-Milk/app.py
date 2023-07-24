# Your code here!
#using formatted string.
#f'The point in XY plane is ({x},{y})'

def song():
    for i in range(99, 0, -1):
        #print(i)
        if (i == 1):
            print("1 bottle of milk on the wall, 1 bottle of milk. Take one down and pass it around, no more bottles of milk on the wall.")
        elif i == 0: 
            print("No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall.");
        elif i== 2: 
            print(f'{i} bottles of milk on the wall, {i} bottles of milk. Take one down and pass it around, {i -1} bottle of milk on the wall.');
        else: 
            print(f'{i} bottles of milk on the wall, {i} bottles of milk. Take one down and pass it around, {i -1} bottles of milk on the wall.');
        

    

song()