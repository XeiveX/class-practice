banks = {
    'Bank Mellat': [610433, 627412],
    'Bank Refah': [589463],
    'Bank Maskan': [628023],
    'Bank Sepah': [589210],
    'Bank Keshavarzi': [603770],
    'Bank Melli Iran': [603799],
    'Bank Tejarat': [627353],
    'Bank Saderat Iran': [603769],
    'Export Development Bank': [627648],
    'Post Bank Iran': [627760],
    'Central Bank of Iran': [936450],
    "Tose'e Credit Inst.": [628157],
    'Bank Saman': [621986],
    'Bank Karafarin': [627488],
    'Bank Parsian': [622106],
    'Bank Eghtesad Novin': [627412],
    'Bank Pasargad': [639347, 502229],
    'Bank Sarmayeh': [639607],
    'Bank Sina': [639346],
    'Mehr Credit Inst.': [606737],
    'Bank Shahr': [502806],
    "Bank Tose'e Ta'avon": [502908],
    'Bank TAT': [636214],
    'Bank Dey': [502938],
    'Bank Ansar': [627381]
} #i gave the excel folder to Ai and told to put them in dict.

user = input("Put a Random card number : ")
#user_n = int(user[:6]) #i first tought of making a loop that saves the first 6 numbers of user
#but then asked ai if theres a faster way with shorter code and it tought me about " Slicing "
#which is this : user[:6] . But be aware ! it only works with strings !
for bank , num in banks.items() :
    if num in user:
        print("yes")
