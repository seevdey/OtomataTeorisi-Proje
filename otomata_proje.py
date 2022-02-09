from exrex import generate
import re 

alfabe = input("Alfabe giriniz: ").split(',')
print("Alfabe:", alfabe)

duzenli_ifade = input("Düzenli ifadeyi giriniz: ")

def di_Kontrol(alinan_di: str, escape: bool):
    try:
        if escape: 
            re.compile(re.escape(alinan_di))
        else: 
            re.compile(alinan_di)
        is_valid = True
    except re.error:
        is_valid = False
    return is_valid

#print("Girilen düzenli ifade geçerliliği : {}.".format(di_Kontrol(duzenli_ifade, escape = False)))

if di_Kontrol(duzenli_ifade, escape = False):
    print("Düzenli ifade girilen alfabeden üretilebilir...")
    kelime = int(input("L dilinin kaç kelimesini görmek istiyorsunuz: "))
    eslesme = list(generate(duzenli_ifade,kelime))
    sinir = eslesme[:kelime] 
    print("Dile ait {} tane kelime :".format(kelime), sinir)
    
    kontrol = input("Kontrol edilecek kelimeyi giriniz : ")
    if re.match(duzenli_ifade, kontrol):
        print("Bu kelime L diline aittir...")
    else: 
        print("Bu kelime L diline ait değildir...")
        
else:
    print('\nDüzenli ifade geçerli değil, eşleşme yok.') 