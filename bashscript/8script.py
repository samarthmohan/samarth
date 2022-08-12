def solution(inputString):
    input_text=inputString.strip()
    input_text=input_text.lower()
    input_text2=input_text.split()
    input_text3=""
    for word in input_text2:
        input_text3+=word
    #print input_text
    #print input_text2
    #print input_text3
    reverse_text=""
    for i in range(len(input_text3)-1,-1,-1):
        reverse_text+=input_text3[i]
    if input_text3 == reverse_text:
        return True
    else:
        return False

print(solution('abac'))
