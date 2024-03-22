import os

# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesn't exist

f = open("lesson22/names.txt")
# print(f.read())
# print(f.read(4))

# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = open("lesson22/names.txt")
    print(f.read())
except:
    print("The file you want to read doesn't exist")
finally:
    f.close()

# Append - creates the file if it doesn't exist
f = open("lesson22/names.txt", "a")
f.write("Neil\n")
f.close()

f = open("lesson22/names.txt")
print(f.read())
f.close()

# Write (overwrite)
f = open("lesson22/context.txt", "w")
f.write("I deleted all of the context")
f.close()

f = open("lesson22/context.txt")
print(f.read())
f.close()

# Two ways to create a new file

# Opens a file for writing, creates the file if it does not exist
f = open("lesson22/name_list.txt", "w")
f.close()

# Creates the specified file, but returns an error if the file exists
if not os.path.exists("lesson22/dave.txt"):
    f = open("lesson22/dave.txt", "x")
    f.close()

# Delete a file

# avoid an error if it doesn't exist
if os.path.exists("lesson22/dave.txt"):
    os.remove("lesson22/dave.txt")
else:
    print("The file you wish to delete does not exist")


# with has built-in implicit exception handling
# close() will be automatically called
with open("lesson22/more_names.txt") as f:
    content = f.read()

with open("lesson22/names.txt", "w") as f:
    f.write(content)
