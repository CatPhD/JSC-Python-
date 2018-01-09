import re

sourceText =""

def convert(text):
    mphPattern = r"\d+\.?\d*\smph"
    floatPattern = r"\d+\.?\d*"
    match = re.finall(mphPattern, text)
    for item in match:
        value = re.finall(floatPattern, item)
        kmValue = float(value[0])*1.60934
        kmph = format(kmValue, ".1f") + "km/h"
        text = text.replace(item, kmph)
    return text



print(sourceText)
convertedText = convert(sourceText)
print(convertedText)
