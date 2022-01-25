
# # Python3 program to check
# # URL is valid or not
# # using regular expression
# import re
 
# # Function to validate URL
# # using regular expression
# def isValidURL(str):
 
#     # Regex to check valid URL
#     regex = ("((http|https)://)(www.)?" +
#              "[a-zA-Z0-9@:%._\\+~#?&//=]" +
#              "{2,256}\\.[a-z]" +
#              "{2,6}\\b([-a-zA-Z0-9@:%" +
#              "._\\+~#?&//=]*)")
     
#     # Compile the ReGex
#     p = re.compile(regex)
 
#     # If the string is empty
#     # return false
#     if (str == None):
#         return False
 
#     # Return if the string
#     # matched the ReGex
#     if(re.search(p, str)):
#         return True
#     else:
#         return False
 
# # Driver code
 
# # Test Case 1:
# url = "https://playerserver.walkme.com/Search/Search?userGuid=2d0cb951c1404f5fa275068c81ec055d&query=help&source=3"
 
# if(isValidURL(url) == True):
#     print("Yes")
# else:
#     print("No")

import re
 
def check_url(SearchGuid):
# Regular expression for URL
    re_exp = ("((http|https)://)(www.)?" + "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" + "{2,6}\\b([-a-zA-Z0-9@:%" + "._\\+~#?&//=]*)")

    exp = re.compile(re_exp)

    if (SearchGuid == None):
        print("Input string is empty")

    if(re.search(exp, SearchGuid)):
        print("Input URL is valid!")
    else:
        print("Input URL is invalid!")

ip_url = input("Enter the string: ")
check_url(SearchGuid)