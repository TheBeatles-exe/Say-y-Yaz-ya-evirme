sayi = input("Lütfen en fazla 4 basamaklı bir sayı giriniz :")

birler = ["","bir","iki","üç","dört","beş","alt","yedi","sekiz","dokuz"]
onlar =  ["","on","yirmi","otuz","kırk","elli","atmış","yetmiş","seksen","doksan"]
yuzler = ["","yüz","ikiyüz","üçyüz","dörtyüz","beşyüz","altıyüz","yediyüz","sekizyüz","dokuzyüz"]
binler = ["","bin","ikibin","üçbin","dörtbin","beşbin","altıbin","yedibin","sekizbin","dokuzbin"]

s = str(sayi)
if (sayi == "0"):
    print("sıfır")
elif (len (sayi) == 3) :
    print(yuzler[int(s[0])],onlar[int(s[1])],birler[int(s[2])])
elif (len (sayi) == 2) :
        print(onlar[int(s[0])],birler[int(s[1])])
elif (len (sayi) == 1) :
    print(birler[int(s[0])])
else :
    print(binler[int(s[0])],yuzler[int(s[1])],onlar[int(s[2])],birler[int(s[3])])
    
