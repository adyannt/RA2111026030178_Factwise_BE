def to_words(n):
    single = ["one","two","three","four","five","six","seven","eight","nine","ten"]
    tens = ["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty"]
    multiples = ["thirty","forty","fifty","sixty","seventy","eighty","ninety","hundred"]
    
    if n == 1000:
        return "one thousand"

    word = ""
    
    if n >= 100:
        word = word + single[(n // 100) - 1] + " hundred "
        n = n % 100
        if n > 0:
            word = word + "and "
        
    if n > 20:
        word = word + multiples[(n // 10) - 3]
        n = n % 10
         
    if n > 10:
        word = word + " " + tens[n - 11]
        return word
        
    if 10 >= n > 0:
        word = word + " " + single[n - 1]
    
    return word.strip()
total_letters = 0
for i in range(1, 1000):
    num_word = to_words(i)
    total_letters += len(num_word.replace(" ", ""))

print("Total letters used:", total_letters)


