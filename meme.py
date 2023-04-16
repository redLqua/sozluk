meme_sozlugu = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "GG": "iyi oyundu",
            "ff": "teslim olmak",
            "EZ": "kolaydı",
            
            }
            
            
            
kelime = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if kelime in meme_sozlugu.keys():
    print("kelime sözlükte var")
else:
    print("kelime sözlükte yok")
