from task6_text_editor import TextEditor
from task6_linked_stack import LinkedStackADT

option = 0
my_doc = TextEditor()
actions = LinkedStackADT()
try:
    while option != 8:
        print("Pick an option:")
        print("1. insert num:")
        print("2. read filename:")
        print("3. write filename:")
        print("4. print num1 num2:")
        print("5. delete num:")
        print("6. search word:")
        print("7. undo")
        print("8. quit")
        option = int(input("what option? "))

        if option == 1:
            insert_num = int(input("num? "))
            text = input("text? ")
            my_doc.insert_num(insert_num, text)
            command = ["insert", insert_num]
            actions.push(command)

        if option == 2:
            saved_doc = my_doc
            filename = input("filename? ")
            my_doc.read_filename(filename)
            command = ["read", saved_doc]
            actions.push(command)

        if option == 3:
            file_name = input("filename? ")
            saved_doc = TextEditor()
            saved_doc.read_filename(file_name)
            my_doc.write_filename(file_name)
            command = ["write", saved_doc, file_name]

        if option == 4:
            num_one = int(input("num1? "))
            num_two = int(input("num2? "))
            my_doc.print_lines(num_one, num_two)

        if option == 5:
            delete_num = int(input("num? "))
            value = my_doc[delete_num]
            my_doc.delete_num(delete_num)
            command = ["delete", delete_num, value]
            actions.push(command)

        if option == 6:
            word = input("word? ")
            print(my_doc.search_word(word))

        if option == 7:
            action = actions.pop()
            if action[0] == "insert":
                my_doc.delete_num(action[1])
            elif action[0] == "delete":
                my_doc.insert_num(action[1], action[2])
            elif action[0] == "read":
                my_doc = action[1]
            else:
                old_doc = action[1]
                old_file_name = action[2]
                old_doc.overwrite_filename(old_file_name)
except ValueError:
    print("?")
except IndexError:
    print("?")
except StopIteration:
    print("?")
