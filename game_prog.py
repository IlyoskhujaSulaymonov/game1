import add_functions as func

my_count = 0
comp_count = 0
count = True
while count:
    my_count = func.com_comp_me()
    comp_count = func.com_me_comp()
    if my_count == comp_count:
        print(f"Durrang!!! Ikkimiz ham {my_count} urinishda topdik")
    elif my_count > comp_count:
        print(f"Men {comp_count} urinishda topdim va yutdim!")
    else:
        print(f"Siz {my_count} urinishda topdingiz va yutdingiz!")
    count = int(input("Yana o'ynaymizmi: ha(1)/ yo'q (0): "))