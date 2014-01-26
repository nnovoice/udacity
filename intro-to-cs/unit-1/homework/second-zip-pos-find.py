# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# For example,
#text = 'all zip files are zipped' 
# >>> 18
# text = 'all zip files are compressed'
# >>> -1

text = "all zip files are zipped" 
#text = 'all zip files are compressed'
#text = 'no zi p files here'

#ENTER CODE BELOW HERE
first_zip_pos = text.find("zip")
if (first_zip_pos != -1):
    second_zip_pos = text.find("zip", first_zip_pos + 1)
    print second_zip_pos
else:
    print first_zip_pos