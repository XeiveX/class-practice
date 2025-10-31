import random
import unicodedata #added this cause i noticed it didn't accept my answers
def normalize_fa (text): #beacuase some of my ketboard letters are arabic
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("ي", "ی").replace("ك", "ک") #and this reads the arabic letters the same to a persian one
    return text.strip()

words = {
    "beautiful": "زیبا",
    "strong": "قوی",
    "friend": "دوست",
    "dream": "رویا",
    "hope": "امید",
    "light": "نور",
    "dark": "تاریک",
    "happy": "خوشحال",
    "sad": "غمگین",
    "truth": "حقیقت",
    "freedom": "آزادی",
    "power": "قدرت",
    "peace": "صلح",
    "love": "عشق",
    "life": "زندگی",
    "heart": "قلب",
    "time": "زمان",
    "memory": "خاطره",
    "voice": "صدا",
    "world": "جهان"
}

while words:
    key = random.choice(list(words.keys()))
    print(words[key]) #remove after finished the scripting
    user = normalize_fa(input(f"Meaning of '{key}' : "))
    correct = normalize_fa(words[key])
    while user != correct:
        print("Try again !")
        print(words[key]) #remove after finished the scripting
        user = normalize_fa(input(f"Meaning of '{key}' : "))

    print("Correct !")
    words.pop(key)
print("All words Finished !")


