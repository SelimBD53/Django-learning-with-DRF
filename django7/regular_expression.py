# import re 
# findall,sub,split,match,search
#syntax
# . > #matches any character except newline -> a.z
# ^,$ > # matches the start and end of a string

# text = "a brown fox jumps over the lazy dog and dig a hole"
# print(re.findall(r"j..p", text))
# a,*b = re.split(r"^a", text) # start
# a,*b = re.split(r"hole$", text) # end
# print(a, b)

# text1 = "zoom"
# text2 = "zooo"
# text3 = "zo"
# text4 = "z"
# print(re.findall(r"zo*", text4))
# print(re.findall(r"zo+", text4))

# text5 = "color"
# text6 = "colour"
# print(re.findall(r"colou?r", text5))
# print(re.findall(r"colou?r", text6))

# [ch] # > matches any character in the brackets
# [a-z], [0-9] > matches any character in the ranges
# \d = matches any digit
# \w = matches any alphanumeric characters [a-zA-Z0-9_]
# \s = matches any whitespace character[\t\n\r\f\v]
# i = case-insensitive