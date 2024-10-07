

def main():
    spins = 0

    todo = []    

    while True:
        if spins == 0:
            print("welcome to dausen's to do list!\n\n\n\t(features to be added)\n\nto add a task, enter \"add [task]\"\n")
            user_input = input("-")

            print("great! now, use \"view\" to view the list, or use \"remove [task number]\" to remove the task corresponding to the number.")

        user_input = input("-")

        if user_input.startswith "add ":
        
            
        spins += 1
        
        break
    return


if __name__ == "__main__":
    main()