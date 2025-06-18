# f = open("file.txt")
# data = f.read()
# print(data)
# f.close

# file write -------------
# str = "Let's test these code"
# f = open("generatedFile.txt", "w")
# f.write(str)
# f.close()

# read lines -------------

# f = open("file.txt")
# # a = f.readlines()
# a = f.readline()
# a2 = f.readline()
# a3 = f.readline()
# a4 = f.readline()
# print(a, type(a))
# print(a2, type(a))
# print(a3, type(a))
# print(a4 == "", type(a))
# f.close()

# read lines -------------
# str = "Let's test these code"
# f = open("generatedFile.txt", "a")
# f.write(str)
# f.close()

# with -------------
# f = open("file.txt")
# print(f.read())
# f.close()

# # The same can be written using with statement like this:
# with open("file.txt") as f:
#     print(f.read())

# # You dont have to explicitly close the file