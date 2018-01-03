def scrollText(text, speed):
    length = len(text)
    print(text)
    new = text[speed:length] + text[:speed]
    while new != text:
        print(new)
        new = new[speed:length] + new[:speed]
      
speed = 4
scrollText('Hello World ', speed)


## 교수님
##
##def scrollWord(text, speed):
##    for i in range(0, len(text)//speed):
##        print(text)
##        text = text[speed:]+ text[:speed]
##
##scrollWord("Hello World!", 4)
