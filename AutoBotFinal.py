from gtts import gTTS
from googletrans import Translator
import os
import pytesseract as tess
tess.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
from twilio.rest import Client

print("\nWelcome!!!! How can I help you?")
print("\nLets start with language selection !!! ")
translator = Translator()
while True:
    print("\nEnter the language first !!!\n")
    print("1 :- हिंदी (Hindi)\n2 :- française (French)\n3 :- Deutsche (German)\n4 :- 日本語 (Japanese)\n5 :- Española (Spanish)\n6 :- русский (Russain)\n7 :- Portuguesa (Portuguese)\n8 :- Polskie (Polish)\n9 :- 한국어 (Korean)\n10 :- English (English)")
    print("ALWAYS WRITE YOUR TEXT ACCORDING TO YOUR LANGUAGE PHONETICS\n")
    options = ["hi", "fr", "de", "ja", "es", "ru", "pt", "pl", "ko", "en-us"]
    pref = int(input("Now please enter your preference : "))

    if pref <= 11:
        language = options[pref - 1]
    if pref == 0:
        exit(0)

    text11 = "\nThis translator will convert message into your selected language!!!"
    print(text11)
    print("\nThere are two input methods a) Accepting text b) Accepting image.\nSelect the options as per your requirements.\n")
    print("\na) Text method")
    text1 = "1) Are you going to write Message? Y for yes, N for no, (y/n) ---> "
    ct = input(text1)
    if ct == 'y' or ct == 'Y':
        text2 = "Please enter your sentence: "
        enteredtxt = input(text2 + "---> ")
        dt1 = translator.detect(enteredtxt)
        print("Detected language ---> "+dt1.lang)
        translated21 = translator.translate(enteredtxt, dest=language)
        anstext21=translated21.text
        print("Translated message ---> "+ anstext21)
        print("\n")
        text21 = "2) Do you want speech for text? 1 for yes, Press 1 for yes. Or press any other key. ---> "
        ip2 = (input(text21+" ---> "))
        if (ip2 == '1'):
            MyVoice = gTTS(translated21.text)
            MyVoice.save("Speech.mp3")
            os.system("Speech.mp3")
        choicetext=(input("\n3) Do you want to send the above message? Press 1 for yes. Or press any other key to exit."))
        if choicetext=='1':
            convertedtext = anstext21
            client = Client('ACb5578ff37ee05de4d0b2ea49dc1a1422', 'ea1d0a9efdd9b13b0e51c0e69c2ce980', '')
            client.messages.create(to='+919969471631', from_='+13344656050', body=convertedtext)
            print("\nMessage sent!!!")
        print("\nThank You!!!")
        exit(0)
    print("\nb) Image method ")
    text3 = "1) Are you going to upload image for translation? (y/n) ---> "
    ct = input(text3)
    if ct == 'y' or ct == 'Y':
        text31 = "\nPlease enter your image name with extension (Example image.png) "
        imageinput = input(text31+"---> ")
        img = Image.open(imageinput)
        text = tess.image_to_string(img)
        print("Input given ---> "+text)
        t32 = translator.translate(text, dest=language)
        print("Translated text ---> "+t32.text)
        anstext32=t32.text
        text21 = "\n2)Do you want speech for text? Press 1 for yes. (Any other key to exit) "
        ip2 = (input(text21+" ---> "))
        if (ip2 == '1'):
            MyVoice = gTTS(anstext32)
            MyVoice.save("Speech.mp3")
            os.system("Speech.mp3")
        choicetext = (input("\n3)Do you want to send the above message? Press 1 for yes. (Any other key for exit) "))
        if choicetext == '1':
            convertedtext = anstext32
            client = Client('ACb5578ff37ee05de4d0b2ea49dc1a1422', 'ea1d0a9efdd9b13b0e51c0e69c2ce980', '')
            client.messages.create(to='+919969471631', from_='+13344656050', body=convertedtext)
            print("Message sent!!!")
        print("\nThank You!!!")
        exit(0)

    if pref == 0:
        exit(0)
    print("\nThank you!!")
    exit(0)