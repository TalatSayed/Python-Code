alpha = ["a","b","c","d","e" , "f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def main(orignal_txt , shift_amount , inpt):
    cipher = ""
    #hello 
    if inpt =="decode":
            shift_amount*=-1
    for x in orignal_txt:

        if x not in alpha:
            cipher+=x

        else:
            shifted_position = alpha.index(x)+shift_amount
            shifted_position%=len(alpha)
            cipher+=alpha[shifted_position]
    
    print(f"here is the {inpt}d result:{cipher}")

a = True
while a:
 shift = int(input("Please enter the shift number "))
 endecode = input("Please enter encode to Encode and decode for decoding the string").lower()
 string = str(input("Please enter the string")).lower()
 main(orignal_txt = string , shift_amount=shift , inpt=endecode ) 
 sta = input("Do you want to continue").lower()
 if sta =="no": 
    a = False
    print("GoodBye")



        