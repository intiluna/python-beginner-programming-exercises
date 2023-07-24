# Your code here!!
def sing():
    my_lyrics = "";
    for i in range(11):
        if i == 4:
            my_lyrics += 'whisper words of wisdom, '
        elif i == 10: 
            my_lyrics += 'there will be an answer, let it be'
        else:
            my_lyrics += 'let it be, '
    
    return my_lyrics;

print(sing())

# expected result
#"let it be, let it be, let it be, let it be, whisper words of wisdom, let it be, let it be, let it be, let it be, let it be, there will be an answer, let it be"
