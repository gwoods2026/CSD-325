#Garrett Woods - 3/24/2026 - Module 1.3
#This code will count down from the number entered to 0, but to the tune of "99 bottles of beer on the wall"

def main():
    total = int(input('How many bottles of beer on the wall now?:'))

#loop to countdown and show the lyrics to the song
    for i in range(total, 0, -1):
        
        #removes the "s" at the end of bottles if only one bottle remains
        if total == 1:
            print(f'{total} bottle of beer on the wall, {total} bottle of beer!')
        else:
            print(f'{total} bottles of beer on the wall, {total} bottles of beer!')   
        total -= 1
        
        #removes the "s" at the end of bottles if only one bottle remains
        if total == 1:
            print(f'Take one down, pass it around, {total} bottle of beer on the wall!')
       
        #reminds the user to buy more beer once the countdown hits 0
        elif total == 0:
            print(f'Take one down, pass it around, {total} bottles of beer on the wall!')
            print(f'Time to buy more bottles of beer')    
        else:
            print(f'Take one down, pass it aoround, {total} bottles of beer on the wall!')        
main()