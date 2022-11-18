from task4_text_editor import TextEditor

option = 0
my_doc = TextEditor()
try:
    while option != 7:
        print("Pick an option:")
        print("1. insert num:")
        print("2. read filename:")
        print("3. write filename:")
        print("4. print num1 num2:")
        print("5. delete num:")
        print("6. search word:")
        print("7. quit")
        option = int(input("what option? "))

        if option == 1:
            insert_num = int(input("num? "))
            text = input("text? ")
            my_doc.insert_num(insert_num, text)

        if option == 2:
            filename = input("filename? ")
            my_doc.read_filename(filename)

        if option == 3:
            file_name = input("filename? ")
            my_doc.write_filename(file_name)

        if option == 4:
            num_one = int(input("num1? "))
            num_two = int(input("num2? "))
            my_doc.print_lines(num_one, num_two)

        if option == 5:
            delete_num = int(input("num? "))
            my_doc.delete_num(delete_num)

        if option == 6:
            word = input("word? ")
            print(my_doc.search_word(word))
except ValueError:
    print("?")
except IndexError:
    print("?")
except StopIteration:
    print("?")
