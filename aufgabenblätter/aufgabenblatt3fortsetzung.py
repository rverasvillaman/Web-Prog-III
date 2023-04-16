search_term = input(">> Welches Wort soll erraten werden?")
lines = ""
for i in search_term:
    lines += "_"
print(">> Perfekt, lasset die Spiele beginnen")
print(lines)
goon = True
used_letters = []
while goon:
    letter = input(">> Ein Buchstabe bitte: ")
    # 1. Buchstabe wurde bereits verwendet
    if letter in used_letters:
        print(">> Der Buchstabe wurde bereits verwendet")
        print(f">> Bereits verwendete Buchstaben: {used_letters}")
    # 2. Buchstabe ist enthalten
    elif letter in search_term:
        used_letters.append(letter)
        print(">> Der Buchstabe ist enthalten!")
        part_solution = ""
        for j in search_term:
            if j in used_letters:
                part_solution += j
            else:
                part_solution += "_"
        print(part_solution)
    # 3. Buchstabe ist nicht enhalten
    else:
        print(">> Leider ist der Buchstabe nicht enthalten.")
        used_letters.append(letter)
        print(f">> Bereits verwendete Buchstaben: {used_letters}")

    complete = True
    for i in search_term:
        if i not in used_letters:
            complete = False
    if complete:
        goon = False