import arduino
import morse
from engi1020.arduino.api import *
import sys
from pick import pick
from time import *

state = True
while state:
    oled_clear()

    translationTitle = "Select type of translation: "
    translationOptions = ["Morse", "English"]

    translationOption = pick(
        translationOptions, translationTitle, indicator='>')

    if "Morse" in translationOption:
        morseInputTitle = "Select input: "
        morseInputOptions = ["Button", "Terminal"]

        morseInputOption = pick(
            morseInputOptions, morseInputTitle, indicator='>')

        morseOutputTitle = "Select output(s): "
        morseOutputOptions = ["OLED Screen", "Terminal"]

        morseOutputOption = pick(
            morseOutputOptions, morseOutputTitle,
            indicator='>', min_selection_count=1, multiselect=True)

        ledAid = False
        buzzerAid = False
        if "Button" in morseInputOption:
            morseAidTitle = "Select input aid(s): "
            morseAidOptions = ["LED", "Buzzer"]
            morseAidOption = pick(
                morseAidOptions, morseAidTitle,
                indicator='>', multiselect=True, min_selection_count=1)

            for element in morseAidOption:
                for output in element:
                    if "LED" == output:
                        ledAid = True
                    elif "Buzzer" == output:
                        buzzerAid = True
                    else:
                        pass
        else:
            pass

        if "Button" in morseInputOption:
            n = input("Press Enter to start...")
            morseButton = arduino.buttonReader(ledAid, buzzerAid)
            translatedText = morse.morseTranslate(morseButton)
            oled = False
            morseTerminal = False
            for element in morseOutputOption:
                for output in element:
                    if output == "OLED Screen":
                        oled = True
                    elif output == "Terminal":
                        morseTerminal = True
            arduino.toDisplay(translatedText, morseTerminal, oled)

        else:
            morseText = input("Enter morse text: ")
            translatedText = morse.morseTranslate(morseText)
            oled = False
            morseTerminal = False
            for element in morseOutputOption:
                for output in element:
                    if output == "OLED Screen":
                        oled = True
                    elif output == "Terminal":
                        morseTerminal = True
            arduino.toDisplay(translatedText, morseTerminal, oled)

    else:
        englishInputTitle = "Select input: "
        englishInputOptions = ["Terminal"]

        englishInputOption = pick(
            englishInputOptions, englishInputTitle, indicator='>')

        englishOutputTitle = "Select output(s): "
        englishOutputOptions = ["LED", "Buzzer", "Terminal"]

        englishOutputOption = pick(
            englishOutputOptions, englishOutputTitle, indicator='>',
            multiselect=True, min_selection_count=1)

        if "Terminal" in englishInputOption:
            englishText = input("Input text to be translated: ")
            morseCode = morse.translateToMorse(englishText)

            led = False
            buzzer = False
            console = False

            for element in englishOutputOption:
                for output in element:
                    if output == "LED":
                        led = True
                    elif output == "Buzzer":
                        buzzer = True
                    elif output == "Terminal":
                        console = True

            arduino.morseToOutput(morseCode, led, buzzer, console)

        else:
            pass

    sleep(5)

    cont = pick(["Y","N"],"Do you want to continue?", indicator='>')
    if "N" in cont:
        state = False

print("Thank you for using the translator! I am here whenever you want me. See you soon!")
