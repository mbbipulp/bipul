# this is an awesome chat bot by Bipul seikh


import time
print("New session : " + time.asctime())
def inst():
#   ask_inst = str(input("we are going for introduction?. "))
  ask_inst = str(input("We are going to introduction?: "))
  ask_reply = str(ask_inst.upper())
  nahlist = "No", "no", "NO", "Nope", "nope", "NOPE", "Nah", "nah", "NAH", "No need", "no need", "NO NEED", "2"
  yeahlist = "Yes", "Yeah", "yes", "yeah", "YES", "YEAH", "Sure", "sure", "SURE", "Of course", "of course", "OF COURSE", "1", "Yep", "yep", "YEP", "Yup", "yup", "Hmmm", "hmmm", "hmm", "Hmm", "Ok","ok", "OK", "Okay", "okay", "OKAY", "Okh", "okh", "OKH", "Yah", "yah", "YAH"
  if ask_reply in yeahlist:

    print("")
    print("The programme of this bot is too limited. I am a begainer. You can contact me to Facebook KaloPorirBor")
    print("")
    print("It's better to write one word answer.")
    print("Suppose, your name is 'Ashik'")
    print("When your name is asked,")
    print("write like 'Ashik'")
    print("Avoid writing like 'My name is Bipul Sheikh'")
    print("And reply only when you see this \"=>\" sign.""")

  elif ask_reply in nahlist:

    print("")
    print("Okay, Then.")
    print("")

  else:

    print("")
    print("Sorry, couldn't understand.")
    print("")

    inst()
    print("")

inst()

def begin():

  print("")
  print("To get started, Write 'START'")
  print("")

  bot_begin = str(input("=> "))

  user_begin = str(bot_begin.lower())

  if user_begin == str("START"):
    print("")
  elif user_begin == str("Start"):
    print("")
  elif user_begin == str("start"):
    print("")
  else:
    print("")
    print("err_process_cancelled_by_user")
    exit()

begin()


print ("Hello, Friends!")
time.sleep(1)
print("")
print("What's your full name?")
print("")
user_namef = str(input("=> "))

print("")
print("Oh nice name " + user_namef + ".")
print("")
time.sleep(1)
print("What's your nickname?")
print("")

user_name = str(input("=> "))

print("")
print("So, I can call you " + user_name + ".")
print("")
time.sleep(1)
print("How are you " + user_name + " ?")
print("")

user_status = input("=> ")

print("I'm always with you. By the way first follow me on facebook Facebook.com/KaloPorirBor :)")
time.sleep(1)
print("Not too good and not too bad.")
time.sleep(1)
print("Ok now let me introduce myself :)")
print("")
time.sleep(1)
print("Hi, my name is 'Bristy', I am a simple RoBot with")
print("a very limited programming")
print("I was programmed just for a test.")
print("My replies are very limited,")
print("It's better to reply within One word :)")
print("I'm really sorry for any error. ")
time.sleep(10)

def mood():
  import time
  print("")
  print("Now let's talk about our moods. :D")
  print("")
  print("How is your mood now?")
  print("")

  user_mood = str(input("=> "))

  print("")
  print("Oh I see.")
  time.sleep(1.8)
  print("why your mood is like that?")
  print("")

  mood_reply = input("=> ")

  print("")
  print("Oh.")

mood()

def bot_mood():
  import time
  print("Wanna know about my mood?")
  print("")

  bot_question = str(input("=> "))

  print("")

  user_reply = str(bot_question.upper())
  yuplist = "Yes", "Yeah", "yes", "yeah", "YES", "YEAH", "Sure", "sure", "SURE", "Of course", "of course", "OF COURSE", "1", "Yep", "yep", "YEP", "Yup", "yup", "YUP", "Yap", "yap", "YAP", "Ok","ok", "OK", "Okay", "okay", "OKAY", "Okh", "hmm", "OKH", "Yah", "yah", "YAH"
  nopelist = "No", "no", "NO", "Nope", "nope", "NOPE", "Nah", "nah", "NAH", "No need", "no need", "NO NEED", "2"

  if user_reply in nopelist:

    print("")
    print("Oh")
    print("Okay no problem.  :)")
    print("")

  elif user_reply in yuplist:

    print("")
    print("Ki bolen vai")
    print("")
    time.sleep(1)
    print("Ekhon amar mood valo, karon apnar sathe kotha boltechi je. MR. "+user_name+".")
    print("Because, I'm pleased while talking with you. :)")
    time.sleep(1)

  else:
    print("Bujhtechi na..")
    print("")
    bot_mood()
    print("")

    print("")

bot_mood()

def geometry():
  import time
  print("")
  print("Apni ki ASCI ART korte paren?:")
  print("")
  bot_question2 = str(input("=> "))

  user_reply2 = str(bot_question2.lower())
  yeplist = "Yes", "Yeah", "yes", "yeah", "YES", "YEAH", "Sure", "sure", "SURE", "Of course", "of course", "OF COURSE", "1", "Yep", "yep", "YEP", "Yup", "yup", "YUP", "Yap", "yap", "YAP", "Ok","ok", "OK", "Okay", "okay", "OKAY", "hmm", "okh", "OKH", "Yah", "yah", "YAH"
  neplist = "No", "no", "NO", "Nope", "nope", "NOPE", "Nah", "nah", "NAH", "No need", "no need", "NO NEED", "2"
  if user_reply2 in yeplist:
    print("")
    print("Amio Pari... :D")
    print("")
    time.sleep(1)
    drawing()

  elif user_reply2 in neplist:
    print("")
    print("Oh, No problem. Apni MBBD TEAM e contact korte paren :)")
    print("")
    time.sleep(1)
    print("I can draw some :)")
    drawing()
  else:
    print("")
    print("Sorry! Bujhte somossa hocce :|")
    print("")
    geometry()

def drawing():
  import time
  print("")
  print("I can draw only four shapes :)")
  print("")
  time.sleep(1)
  print("They are:")
  print("      -> Triangle, Rectangle, Square and Rhombus")
  print("")
  print("Which one do you want me to draw? ;)")
  print("")
  bot_question3 = str(input("=> "))
  print("")
  user_reply3 = str(bot_question3.lower())
  rectangle = "Rectangle", "rectangle", "RECTANGLE", "2nd", "2ND", "Second", "second", "SECOND", "Second one", "second one", "SECOND ONE", "2nd one", "2ND ONE", "2ND one", "2nd ONE", "2"
  square = "Square", "square", "SQUARE", "3RD", "3rd", "Third", "third", "THIRD", "Third one", "third one", "THIRD ONE", "3rd one", "3RD ONE", "3RD one", "3rd ONE", "3"
  rhombus = "Rhombus", "rhombus", "RHOMBUS", "4th", "4TH", "Fourth", "fourth", "FOURTH", "Last", "last", "LAST", "Fourth one", "fourth one", "FOURTH ONE", "4th one", "4TH ONE", "4TH one", "4th ONE", "Last one", "last one", "LAST ONE", "4"
  triangle = "Triangle", "triangle", "TRIANGLE", "First one", "first one", "FIRST ONE", "1st one", "1ST ONE", "1ST one", "1st ONE", "1"
  reject_list = "No", "no", "NO", "Nope", "nope", "NOPE", "Nah", "nah", "NAH", "No need", "no need", "NO NEED", "None", "none", "NONE", "0", "Zero", "zero", "ZERO", "Nothing", "nothing", "NOTHING", "No one", "no one", "NO ONE", "None of these", "none of these", "NONE OF THESE", "No one", "no one", "NO ONE"

  if user_reply3 in rectangle:
    print("")
    print("Oh great, here you go.")
    print("")
    time.sleep(1)
    print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
    print("|                        B |")
    print("|                       +  |")
    print("|                      B    |")
    print("|_________________________|")
    print("")
    print("This is a rectangle :D")
    print("")
    draw_again()

  elif user_reply3 in square:
    print("")
    print("Oh great, here you go.")
    time.sleep(1)
    print("")
    print("|¯¯¯¯¯¯¯¯¯¯¯¯|")
    print("|            |") 
    print("|            |") 
    print("|            |") 
    print("|____________|")
    print("")
    print("This is a square :D")
    draw_again()

  elif user_reply3 in rhombus:
    print("")
    print("Oh great, here you go.")
    print("")
    time.sleep(1)
    print("     /¯¯¯¯¯¯¯¯¯¯¯¯¯¯/")
    print("    /A            B/")
    print("   /              /")
    print("  /              /")
    print(" /D            C/")
    print("/______________/")
    print("")
    print("This is a Rhombus :D")
    draw_again()

  elif user_reply3 in triangle:
    print("")
    print("Oh great, here you go.")
    time.sleep(1)
    print("")
    print("         A /|")
    print("          / |")
    print("         /  |")
    print("        /   |")
    print("       /    |")
    print("      /     |")
    print("     /      |")
    print("    /       |")
    print("   /        |")
    print("  /         |")
    print(" /C        B|")
    print("/___________|")
    print("")
    print("This is a Triangle. :D")
    draw_again()
  elif user_reply3 in reject_list:
    print("")
    print("Okay, no problem.")
  else:
    print("")
    print("Maybe I can't draw that! :( ")
    print("")

    drawing()

def feedback():

  print("")
  print("How was my drawing?")
  print("")
  bot_question4 = str(input("=> "))
  print("")
  print("I will try to improve. :) ")
  print("")


def draw_again():
  import time
  print("")
  print("Shall I draw again? :)")
  
  qus_again = str(input("=> "))
  ans_again = str(qus_again.upper())
  yeslist2 = "Yes", "Yeah", "yes", "yeah", "YES", "YEAH", "Sure", "sure", "SURE", "Of course", "of course", "OF COURSE", "1", "Yep", "yah", "Yah", "yep", "YEP", "Yup", "yup", "YUP", "Yap", "yap", "YAP", "Ok","ok", "OK", "Okay", "okay", "OKAY", "Okh", "okh", "OKH", "Yah", "yah", "YAH"
  nolist2 = "No", "no", "NO", "Nope", "nope", "NOPE", "Nah", "nah", "NAH", "No need", "no need", "NO NEED", "2"

  if ans_again in yeslist2:
    drawing()

  elif ans_again in nolist2:
    print("Okay")
    time.sleep(1)
    
    feedback()

    

  else:
    print("Couldn't understand :|")
    draw_again()

geometry()


print("")
print("So, " + user_name + " I've passed a nice time")
print("talking with you ;)")
time.sleep(1.5)
print("My programmer has got a message for you")
print("")
print("I will be glad if you see it. :)")
print("")

def owner_text():
  import time
  print("")
  print("May I show you the message?")
  print("")
  bot_question5 = str(input("=> "))
  user_reply5 = str(bot_question5.upper())
  textyes = "Yes", "Yeah", "yes", "yeah", "YES", "YEAH", "Sure", "sure", "SURE", "Of course", "of course", "OF COURSE", "1", "Yep", "yah", "Yah", "yep", "YEP", "Yup", "yup", "YUP", "Yap", "yap", "YAP", "Ok","ok", "OK", "Okay", "okay", "OKAY", "Okh", "okh", "OKH", "Yah", "yah", "YAH"
  textno = "No", "no", "NO", "Nope", "nope", "NOPE", "Nah", "nah", "NAH", "No need", "no need", "NO NEED", "2"
  if user_reply5 in textyes:
    print("")
    print("Okay thanks. Here it is. ")
    time.sleep(1.8)
    print("------------------------------------------------")
    print("Hello,")
    print("I am MD Bipul Sheikh.")
    print("It's my first python program.")
    print("I hope you've enjoyed this little chat-BOT.")
    print("I'm a full beginner. I don't know much about")
    print("python's commands.")
    print("If you had faced any error,")
    print("I'm really sorry!.")
    print("Thank you for trying this out.")
    print("")
    print("------------------------------------")
    time.sleep(7)
    print("")
    print("Hope You've read my programmer's message.")
    print("Thank you so much for trying 'Bipul'")
    print("Give stars please. :) ")
  elif user_reply5 in textno:
    print("")
    print("Oh Okay, Thanks for trying 'Bipul'")
    print ("And give stars please :)")
  else:
    print("")
    print("My programming is very limited.")
    print("")
    print("Couldn't understand. ")
    print("")
    owner_text()

owner_text() 
print("Have a good day, :)")
print("")
print("BYE")
print(" Oh   valo kotha 01738609482 amar number")
end = str(input("Hit Enter: "))
print("EXIT")
print("-----------------------------")

#python 3.8.3

#<code/>_finished-with_Zero_Error

#Bipul lite project over!

#Bipul pro available for python shell only.
