from task5_text_editor import TextEditor

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

"""
ANALYSIS OF LINKED VS ARRAY-BASED LIST ADT IMPLEMENTATION IN PERFORMANCE

When using array-based List ADT, it would be less time efficient when the size of the file is unknown. This is because for array-based lists,
which we have made such that the underlying array is dynamic, when the list is full it would need to create another list and copy every item
into the the new list with increased size. Whereas for linked lists, it would have better performance if we do not know the size of the list
because we will not run out of space as long we have sufficient memory on our machine. As such, many insertions and deletions for array-based
lists will have a lower performance in terms of time complexity as we need to recreate the underlying array size. As for the linked list, once
we know the position of the node, it is O(1) time complexity to insert and delete elements from the list. In terms of memory performance,
if the list is relatively empty, the linked lists will be more memory efficient as we do not hold empty space for elements that arent in the
list, but if the list is relatively full, the array-based list will be more memory efficient. This is because for the linked lists, there are
two refernces, one to the object and one to the node it is pointing, compared to the array only having one reference. 
"""
