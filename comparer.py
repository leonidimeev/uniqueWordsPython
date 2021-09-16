#Open the file
my_File = open("comparer.txt", 'r')
#Read the file
read_File = my_File.read()
#Split the words
words = read_File.split()
#Using a set will only save the unique words
unique_words = set(words)
#You can then print the set as a whole or loop through the set etc
for word in unique_words:
     print(word)