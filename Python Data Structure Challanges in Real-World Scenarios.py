#Tast 1: Library System Enhancement
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

#Add functionality to insert new books into 'library'. Ensure that adding duplicate books are handled appropriately.
#define a new function to add books to the library
def Add_Book():
    #prompt the user for the books title and author
    title = str(input("What is the title of the book? "))
    author = str(input("Who is the author of the book? "))

    #create a new tuple using the title and author provided
    new_book = (title, author)
    #make a variable set to False as default to check later for duplicate books
    duplicate_book = False

    #iterate through the library list
    for i in range(len(library)):
        #assigning the current list iteration as its own temporary variable
        current_book = library[i]
        #if both the title and author of the added book are the same as the current iteration, it is a duplicate
        #using .lower() method to ensure formatting is universal
        if title.lower() == current_book[0].lower() and author.lower() in current_book[1].lower():
            duplicate_book = True

    #if it is a duplicate, tell the user and do not add the new book to the library list
    if duplicate_book == True:
        print("Sorry, our library already has this book.")
    #if not, split the title and author, iterate through them and format them correctly
    #then join them back into their original variables, and store them back into the new_book tuple
    else:
        split_title = title.split()
        for i in range(len(split_title)):
            split_title[i] = split_title[i].capitalize()
        title = " ".join(split_title)

        split_author = author.split()
        for j in range(len(split_author)):
            split_author[j] = split_author[j].capitalize()
        author = " ".join(split_author)

        new_book = (title, author)

        #add the new book to the library list after formatting
        library.append(new_book)

#call the function and display the curreny library
Add_Book()
print(library)