try:
    Full_name = input('Full name: ')
    age = input('age: ')
    university = input('University: ')
except:
    Full_name = ''
    age = ''
    university = ''

print( Full_name,'is',age,'years old and studying at',university+'.' )