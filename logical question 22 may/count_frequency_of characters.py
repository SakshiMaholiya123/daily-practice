#count the frequencies of character of string



def count_frequency(text):

    freq={}

    for char in text:
        freq[char]=freq.get(char,0)+1
    return freq

word="apple"
obj=count_frequency(word)
for key, value in obj.items():
    print(f"{key} : {value}")
    