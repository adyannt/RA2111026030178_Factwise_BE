def to_words(n):
    single = ["one","two","three","four","five","six","seven","eight","nine"]
    tens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    multiples = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    
    if n == 1000:
        return "one thousand"

    word = ""
    
    if n >= 100:
        word = word + single[(n // 100) - 1] + " hundred"
        n = n % 100
        if n > 0:
            word = word + " and "
        
    if n > 20:
        word = word + multiples[(n // 10) - 2]
        n = n % 10
        if n > 0:
            word = word + " "
         
    if 10 < n < 20:
        word = word + tens[n - 10]
    elif 0 < n <= 10:
        word = word + single[n - 1]
    
    return word.strip()

total_letters = 0
for i in range(1, 1001):
    num_word = to_words(i)
    total_letters += len(num_word.replace(" ", ""))

print("Total letters used:", total_letters)
