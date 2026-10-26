def first_and_last(value):
    if not value:
        return {"first": "", "last":""}  
    
    return {
        "first": value[0],
        "last": value[-1]
    }


def str_len(value):
    count = 0
    for char in value:
        count += 1
    return count

def reverse_string(value):
    word = ""
    for i in range(len(value)-1):
        word += value[i]
    return word

def censor_words(text, banned_word):
    if not banned_word:
        return text
    return text.replace(banned_word, "***")

def smart_temperature(value):
    try:
        celsius = float(value)
    except (ValueError, TypeError):
        return "Invalid temperature"
    
    fahrenheit = celsius * 9 / 5 + 32
    
    if celsius <= 0:
        status = "freezing"
    elif celsius < 20:
        status = "cold"
    elif celsius <= 30:
        status = "warm"
    else:
        status = "hot"
        
    return (
        f"Celsius: {celsius}\n"
        f"Fahrenheit: {fahrenheit}\n"
        f"Status: {status}"
    )

def slug_maker(title):
    text = str(title)
    cleaned = text.lower().replace(",", "").replace(".", "")
    return "-".join(cleaned.split())



    Dapper@1122