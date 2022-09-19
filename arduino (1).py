from engi1020.arduino.api import *
from time import sleep
import morse

# When Input is Button


def buttonReader(led, buzzer):
    buzzer_frequency(5, 1023)
    sleep(0.50)
    buzzer_stop(5)

    sampleCode = ""
    while analog_read(0) != 1023:
        sampleCode += " "
        while digital_read(6) == True:
            digital_write(4, led)
            if buzzer == True:
                buzzer_frequency(5, 90)

            sampleCode += str(digital_read(6))

        digital_write(4, False)
        buzzer_stop(5)

        sampleCode += " "
        sampleCode += str(analog_read(0))

    sampleCodeList = sampleCode.split(" ")

    codeList = []
    for element in sampleCodeList:
        if element == "0":
            pass
        elif element == "":
            pass
        else:
            codeList.append(element)

    code = ""
    for element in codeList:
        if element.isnumeric():
            if 0 < int(element) < 200:
                code += " "
            elif 200 < int(element) < 800:
                code += " / "
            else:
                pass
        else:
            if len(element) > 5:
                code += "-"
            elif 4 <= len(element) <= 5:
                code += "."
            else:
                pass

    return code


def morseToOutput(input, ledState, buzzerState, terminalState):
    if terminalState == True:
        print("Translation: ")
        print(input)
    else:
        pass

    for code in input:
        if code == "-":
            digital_write(4, ledState)
            if buzzerState == True:
                buzzer_frequency(5, 90)
            sleep(0.50)
            digital_write(4, False)
            buzzer_stop(5)
        elif code == ".":
            digital_write(4, ledState)
            if buzzerState == True:
                buzzer_frequency(5, 90)
            digital_write(4, False)
            buzzer_stop(5)
        elif code == "/":
            digital_write(4, False)
            buzzer_stop(5)
            sleep(0.50)
        else:
            digital_write(4, False)
            buzzer_stop(5)
            sleep(0.5)


def toDisplay(input, terminalState, oledState):
    terminalMsg = ""
    oledMsg = ""

    if terminalState == True:
        terminalMsg = input
    else:
        pass

    if oledState == True:
        oledMsg = input
    else:
        pass

    oled_print(oledMsg)
    print("""Translation: """)
    print(terminalMsg)
