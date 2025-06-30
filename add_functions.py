import random as r

def com_comp_me():
    k_number = r.choice(range(1, 21))
    print("1 dan 20 gacha son o'yladim. Topa olasizmi?")
    my_count = 0
    while True:
        my_count += 1
        my_number = int(input('>> '))
        if my_number < k_number:
            print("Xato men o'ylagan son bundan kattaroq. Yana harakat qiling!!")
        elif my_number > k_number:
            print("Xato men o'ylagan son bundan kichikroq. Yana harakat qiling!!")
        else:
            print(f"TOPDINGIZ! {k_number} sonini o'ylagan edim. Siz {my_count} ta urinishda topdingiz. Tabriklayman!")
            break
    return my_count

def com_me_comp():
    quyi = 1
    yuqori = 20
    print("1 dan 20 gacha son o'ylang. Men topishga harakat qilaman.")
    input("Son o'ylagan bo'lsangiz istalgan tugmani bosing")
    comp_count = 0
    while True:
        if quyi != yuqori:
            k_number1 = r.randint(quyi, yuqori)
        else:
            k_number1 = quyi
        comp_count += 1
        butt = input(f"Siz {k_number1} sonini o'yladingiz: to'g'ri (t), men o'ylagan son bundan kattaroq (+), kichikroq (-)?? ")
        if butt == "+":
            quyi = k_number1 + 1
        elif butt == "-":
            yuqori = k_number1 -1
        else:
            break
    print(f"Soningizni {comp_count} ta taxmin bilan topdim!")
    return comp_count