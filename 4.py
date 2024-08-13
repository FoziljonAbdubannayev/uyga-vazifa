left_hand = set("1!qaz2@wsx3#edc4$rfv5%tgb")
right_hand = set("6^yhn7&ujm8*ik,9(ol.0)p;/'[]{}")

def count_hand_use(file_name):
    left_count = 0
    right_count = 0

    with open(file_name, 'r') as file:
        text = file.read().lower()

    for char in text:
        if char in left_hand:
            left_count += 1
        elif char in right_hand:
            right_count += 1

    return left_count, right_count


file_name = input("Fayl nomini kiriting: ")
left, right = count_hand_use(file_name)

print(f"Chap qol bilan {left} ta belgi ishlatilgan.")
print(f"Ong qol bilan {right} ta belgi ishlatilgan.")
