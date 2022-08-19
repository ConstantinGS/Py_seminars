
def complex_calc(number1, number2, action):
    number1 = number1.replace(' ', '')
    number2 = number2.replace(' ', '')
    action= action.replace(' ', '')
    
    sign = ["+","-","*","/"]
    act_part_n1 = ""
    im_part_n1 = ""
    condition = ""
    count = 0
    condition += f"({number1}){action}({number2})"

    while count < len(number1) and number1[count] not in sign:
        if number1[count] == "i":
            act_part_n1 = "0"
            break
        act_part_n1 += number1[count]
        count+=1
    
    if count < len(number1) and number1[count]!="-":
        count+=1
    while count < len(number1) and number1[count] != "i":
        im_part_n1 += number1[count]
        count+=1

    act_part_n2 = ""
    im_part_n2 = ""
    count = 0

    while count < len(number2) and number2[count] not in sign :
        if number2[count] == "i":
            act_part_n2 = "0"
            break
        act_part_n2 += number2[count]
        count+=1
    if count < len(number2) and number2[count]!="-" :
        count+=1
    while count < len(number2) and number2[count] != "i":
        im_part_n2 += number2[count]
        count+=1
    
    if act_part_n1 == "": act_part_n1 = "0+"
    if act_part_n2 == "": act_part_n2 = "0+" 
    if im_part_n1 == "": im_part_n1 = "+0"
    if im_part_n2 == "": im_part_n2 = "+0"  


    

    if action == "+":
        act_part_n = float(act_part_n1)+float(act_part_n2)
        im_part_n = float(im_part_n1)+float(im_part_n2)

    elif action == "-":
        act_part_n = float(act_part_n1)-float(act_part_n2)
        im_part_n = float(im_part_n1)-float(im_part_n2)
    
    elif action == "*":

        part_n1 = float(act_part_n1)*float(act_part_n2)
        part_n2 = float(act_part_n1)*float(im_part_n2)
        part_n3 = float(im_part_n1)*float(act_part_n2)
        part_n4 = float(im_part_n1)*float(im_part_n2)

        im_part_n = part_n2 + part_n3
        act_part_n = part_n1 + (part_n4*(-1))
    
    elif action == "/":

        part_n1_1 = float(act_part_n1)*float(act_part_n2)
        part_n2_1 = float(act_part_n1)*(-float(im_part_n2))
        part_n3_1 = float(im_part_n1)*float(act_part_n2)
        part_n4_1 = float(im_part_n1)*(-float(im_part_n2))

        im_part_n_1 = part_n2_1 + part_n3_1
        act_part_n_1 = part_n1_1 + (part_n4_1*(-1))

        part_n1_2 = float(act_part_n2)*float(act_part_n2)
        part_n4_2 = float(im_part_n2)*(-float(im_part_n2))

        act_part_n_2 = part_n1_2 + (part_n4_2*(-1))

        im_part_n = im_part_n_1 / act_part_n_2
        act_part_n = act_part_n_1 / act_part_n_2

    
    if act_part_n == 0: return (f"{condition}={im_part_n}i")
    if im_part_n>0: return(f"{condition}={act_part_n}+{im_part_n}i")
    elif im_part_n<0: return(f"{condition}={act_part_n}{im_part_n}i")
    else: return (f"{condition}={act_part_n}  ")


print(complex_calc("5+5i", "5", "+"))

    


            
            

