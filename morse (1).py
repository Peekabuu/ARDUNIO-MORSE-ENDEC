def morseTranslate(input):
    translatedMessage = ""
    inputList = input.split(" ")
    for element in inputList:

        if ".-" == element:
            translatedMessage += "A"
        elif "-..." == element:
            translatedMessage += "B"
        elif "-.-." == element:
            translatedMessage += "C"
        elif "-.." == element:
            translatedMessage += "D"
        elif "." == element:
            translatedMessage += "E"
        elif "..-." == element:
            translatedMessage += "F"
        elif "--." == element:
            translatedMessage += "G"
        elif "...." == element:
            translatedMessage += "H"
        elif ".." == element:
            translatedMessage += "I"
        elif ".---" == element:
            translatedMessage += "J"
        elif "-.-" == element:
            translatedMessage += "K"
        elif ".-.." == element:
            translatedMessage += "L"
        elif "--" == element:
            translatedMessage += "M"
        elif "-." == element:
            translatedMessage += "N"
        elif "---" == element:
            translatedMessage += "O"
        elif ".--." == element:
            translatedMessage += "P"
        elif "--.-" == element:
            translatedMessage += "Q"
        elif ".-." == element:
            translatedMessage += "R"
        elif "..." == element:
            translatedMessage += "S"
        elif "-" == element:
            translatedMessage += "T"
        elif "..-" == element:
            translatedMessage += "U"
        elif "...-" == element:
            translatedMessage += "V"
        elif ".--" == element:
            translatedMessage += "W"
        elif "-..-" == element:
            translatedMessage += "X"
        elif "-.--" == element:
            translatedMessage += "Y"
        elif "--.." == element:
            translatedMessage += "Z"
        elif "-----" == element:
            translatedMessage += "0"
        elif ".----" == element:
            translatedMessage += "1"
        elif "..---" == element:
            translatedMessage += "2"
        elif "...--" == element:
            translatedMessage += "3"
        elif "....-" == element:
            translatedMessage += "4"
        elif "....." == element:
            translatedMessage += "5"
        elif "-...." == element:
            translatedMessage += "6"
        elif "--..." == element:
            translatedMessage += "7"
        elif "---.." == element:
            translatedMessage += "8"
        elif "----." == element:
            translatedMessage += "9"
        elif "/" == element:
            translatedMessage += " "

    return translatedMessage


def translateToMorse(input):
    morseCode = ""
    inputList = []
    for element in input.upper().split():
        inputList.append(element)
        inputList.append(" ")

    for element in inputList:
        for chr in element:
            if " " == chr:
                morseCode += "/"
            elif "A" == chr:
                morseCode += ".-"
            elif "B" == chr:
                morseCode += "-..."
            elif "C" == chr:
                morseCode += "-.-."
            elif "D" == chr:
                morseCode += "-.."
            elif "E" == chr:
                morseCode += "."
            elif "F" == chr:
                morseCode += "..-."
            elif "G" == chr:
                morseCode += "--."
            elif "H" == chr:
                morseCode += "...."
            elif "I" == chr:
                morseCode += ".."
            elif "J" == chr:
                morseCode += ".---"
            elif "K" == chr:
                morseCode += "-.-"
            elif "L" == chr:
                morseCode += ".-.."
            elif "M" == chr:
                morseCode += "--"
            elif "N" == chr:
                morseCode += "-."
            elif "O" == chr:
                morseCode += "---"
            elif "P" == chr:
                morseCode += ".--."
            elif "Q" == chr:
                morseCode += "--.-"
            elif "R" == chr:
                morseCode += ".-."
            elif "S" == chr:
                morseCode += "..."
            elif "T" == chr:
                morseCode += "-"
            elif "U" == chr:
                morseCode += "..-"
            elif "V" == chr:
                morseCode += "...-"
            elif "W" == chr:
                morseCode += ".--"
            elif "X" == chr:
                morseCode += "-..-"
            elif "Y" == chr:
                morseCode += "-.--"
            elif "Z" == chr:
                morseCode += "--.."
            elif "0" == chr:
                morseCode += "-----"
            elif "9" == chr:
                morseCode += "----."
            elif "8" == chr:
                morseCode += "---.."
            elif "7" == chr:
                morseCode += "--..."
            elif "6" == chr:
                morseCode += "-...."
            elif "5" == chr:
                morseCode += "....."
            elif "4" == chr:
                morseCode += "....-"
            elif "3" == chr:
                morseCode += "...--"
            elif "2" == chr:
                morseCode += "..---"
            elif "1" == chr:
                morseCode += ".----"
            morseCode += " "

    return morseCode
