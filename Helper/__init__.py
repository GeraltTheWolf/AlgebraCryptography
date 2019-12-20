def helper_get_menu_selection(max_menu_selection):
    user_input = 0
    while True:
        try:
            user_input = int(input("Enter menu option: "))
        except ValueError:
            print("Enter number choice from 0 - " + str(max_menu_selection))
            continue
        else:
            if user_input < 0 or user_input > max_menu_selection:
                print("Enter choice from 0 - " + str(max_menu_selection))
                continue
            break
    return user_input
