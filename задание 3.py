a=input("Введите текст:")
alphabet="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMйцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
forbidden_symbols=";{}[].1234567890-=!@#$%^&*()_+:<>?, "
slovar={ i:0 for i in alphabet}
for i in a:
        if i not in forbidden_symbols:
            slovar[i]+=1

for i in alphabet:
    if slovar[i]!=0:
        print(i,":",slovar[i])
while True:
    try:
        b=input("Какую букву вы хотите найти:")
        if len(b) != 1 and b not in alphabet:
            raise ValueError
        if b in alphabet:
            print(slovar[b])
        break
    except ValueError:
        print("Введена не буквы. Попробуйте еще раз")

