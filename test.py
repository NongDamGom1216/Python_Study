def add_to_dict(dict, *arg):
    if str(type(dict)) == "<class 'dict'>" :
        if len(arg) == 2:
            if arg[0] in dict:
                print(f"{arg[0]} is already on the dictionary. Won't add.")
            else:
                dict[arg[0]] = arg[1]
                print(f"{arg[0]} has been added.")
        else:
            print("You need to send a word and a definition.")
    else:
        print("You need to send a dictionary. You sent: <class 'str'")

def main():
    import os
    os.system('clear')

    my_english_dict = {}
    print(type(my_english_dict))

    # Should not work. First argument should be a dict.
    print('add_to_dict("hello", "kimchi"):')
    add_to_dict("hello", "kimchi")

    # Should not work. Definition is required.
    print('\nadd_to_dict(my_english_dict, "kimchi"):')
    add_to_dict(my_english_dict, "kimchi")

    # Should work.
    print('\nadd_to_dict(my_english_dict, "kimchi", "The source of life."):')
    add_to_dict(my_english_dict, "kimchi", "The source of life.")

    # Should not work. kimchi is already on the dict
    print('\nadd_to_dict(my_english_dict, "kimchi", "My fav. food"):')
    add_to_dict(my_english_dict, "kimchi", "My fav. food")

main()