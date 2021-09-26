
john_index = {"Father": 0, "God": 0, "Christ": 0,
              "Spirit": 0, "spirit": 0, "life": 0,
              "man": 0}

book_of_john_file = open("book of John text.txt","r")
book_of_john = book_of_john_file.read()
book_of_john_list = book_of_john.split()

for word in book_of_john_list:
    for key in john_index:
        if key == word:
            john_index[key] += 1

print("Father:", john_index["Father"])
print("God:", john_index["God"])
print("Christ:", john_index["Christ"])
print("Spirit:", john_index["Spirit"])
print("spirit:", john_index["spirit"])
print("life:", john_index["life"])
print("man:", john_index["man"])
