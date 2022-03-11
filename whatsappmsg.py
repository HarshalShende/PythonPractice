# # importing the module
# import pywhatkit
#
# # using Exception Handling to avoid
# # unprecedented errors
# try:
#
#     # sending message to receiver
#     # using pywhatkit
#     pywhatkit.sendwhatmsg("+918805643291",
#                           "Hello from GeeksforGeeks",
#                           22, 28)
#     print("Successfully Sent!")
#
# except:
#
#     # handling exception
#     # and printing error message
#     print("An Unexpected Error!")

# importing the module
import pywhatkit

# using Exception Handling
# to avoid exceptions
try:

    # it plays a random YouTube
    # video of GeeksforGeeks
    pywhatkit.playonyt("GeeksforGeeks")
    print("Playing...")

except:

    # printing the error message
    print("Network Error Occured")