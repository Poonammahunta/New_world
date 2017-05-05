s = raw_input("Enter the string:  ")
new_s = ""
con = ["c","b","d","h","g"]
vow = ["a","e","i","o","u"]
if s[-2:] == "ie":
    l = s.replace("ie","y")
    new_s = l+"ing"
    print new_s
else:
    new_s == s+"ing"
    print new_s
