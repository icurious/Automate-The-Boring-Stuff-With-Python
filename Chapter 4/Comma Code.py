
def comma_code(user_list):

    string_with_and = ",".join(user_list[:-1]) + " and " + user_list[-1]
    print((string_with_and))


user_input = input("Enter your list: ")
user_list = user_input[1:-1].split(",")
comma_code(user_list)

