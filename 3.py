def nechta_nol_bor(s):
    count = 0
    for char in s:
        if char == '0':
            count += 1
        else:
            break
    return count


s = input("Sonni --> ")

natija = nechta_nol_bor(s)
print(f"Sonning boshida {natija} ta nol bor.")
