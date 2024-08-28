def main():
    plate = input("Plate: ").lower()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if start_two_letters(plate) and two_six_charac(plate) and is_zero(plate) and no_middle_no(plate) and no_symbols(plate):
        return True
    else:
        return False

def start_two_letters(plate):
    if plate[0:2].isalpha():
        return True
    else:
         return False

def two_six_charac(plate):
    x = len(plate)
    if x >= 2 and x <=  6:
        return True
    else:
        return False

def no_middle_no(plate):
    len_of_string = len(plate)
    is_it_valid = True

    for i in range(len_of_string - 1):
        first_l = plate[i]
        sec_l = plate[i + 1]
        is_first_a_letter = first_l.isalpha()
        is_sec_a_letter = sec_l.isalpha()
        if is_first_a_letter == False and is_sec_a_letter == True:
            is_it_valid = False
    return is_it_valid


def is_zero(plate):
    len_of_string = len(plate)
    is_it_valid = True

    for i in range(len_of_string - 1):
        first_l = plate[i]
        sec_l = plate[i + 1]
        is_first_a_letter = first_l.isnumeric()
        if is_first_a_letter == False and sec_l == "0":
            is_it_valid = False

    return is_it_valid


def no_symbols(plate):
    len_of_string = len(plate)
    valid_ = True

    for i in range(len_of_string - 1):
        chara = plate[i]
        is_it_a_no = chara.isnumeric()
        is_it_a_let = chara.isalpha()
        if is_it_a_no == False and is_it_a_let == False:
            valid_ = False
    return valid_

main()
