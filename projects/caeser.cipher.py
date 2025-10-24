#DM 2cnd Ceaser cipheer
# make 2 functions one that decodes a inputed message and one that encrypts a message
def decode():
   Dmsg = input(" what would you like to decode")

   

#use an If statement to ask the user which one they would like to do
user_in = input('do you want to encrypt or decode a ceaser cipher message? if so please input "decode" or "encrypt"')
if user_in == "decode":
#if they decode the message it will ask to input a message  they want to decode
   decode_msg = input("whats message do you want to decode?") 
#then use my decoding function to decode their message and display it
#elif they want to encrypt a message it will ask the user to input what message they want to encrypt
elif user_in == "encrypt":
   encrypt_msg = input("what message do you want to encrypt?")
   

#then using my encrpyt function it will encrypt their message
#then display their now encrypted message
#else display thats not a viable response
else:
   print("thats not a real input")
   