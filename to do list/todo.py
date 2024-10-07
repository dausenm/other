def main():
    spins = 0

    todo = []   

    while 1:
        if spins == 0:
            print("welcome to dausen's to do list!\n\n\n\t(features to be added)\n\nto add a task, enter \"add [task]\"\n")
            user_input = input("-")

        if spins != 0: 
            user_input = input("-")

        elif user_input == "help":
            print("help to be implemented later. look at todo.py on github.com/dausenm/other/to-do-list")
            break

        if user_input.startswith("add "):
            todo.append(user_input[4:])

        elif user_input == "view":
            for index, item in enumerate(todo):
                print(f"{index}: {item}")
                print("\n")

        elif user_input.startswith("rm "):
            index = int(user_input[3:])
            if 0 <= index < len(todo):  # Check if the index is valid
                todo.pop(index)
            else:
                print("Invalid index")

        elif user_input.startswith("echo "):
            print(user_input[5:])

        elif user_input == "stop":
            print("thanks for using my to do utility!\n\n")
            break
            
        else:
            print("command not recognized. use \'help\' to print a list of supported commands\n")

        spins += 1
    return


if __name__ == "__main__":
    main()