from os import listdir, mkdir

# CHANGE THIS INFO
name = "Your Full name"  
email = "yorkemail@my.yorku.ca"
your_student_id = "your_student_id"


lab_number = input("What is the Lab number? ")

lab_file_name = f"lab{lab_number}.py"

print(f"\ncreating {lab_file_name}")

comments_lab = f'''#Lab {lab_number}
#Author: {name}
#Email: {email}
#Student ID: {your_student_id}
'''

try:
    for lab in listdir("labs"):
        if lab == f"{lab_file_name}":
            print("CAUTION: A lab with this lab number already exists!")
            ask = input("Press Y to rewrite the file or N to exit: ")
            if ask.strip().lower() != 'y':
                exit("Bye")
            
except FileNotFoundError:
    print("labs dir not found!")
    ask = input("Would you like to make labs dir (y/n)? ")
    if ask.strip().lower() == 'y':
        mkdir("labs")
        print("Done making labs dir")
    else:
        exit("No folder named labs found exiting bye")
        

with open(f"labs/{lab_file_name}", "w") as p_file:
    p_file.write(comments_lab)

print(f"Done making labs/{lab_file_name} file, get set coding!")





"""
Note: Licensed as GNU General Public License v3.0 by Aayush Pokharel, Limitations: Liability, Warranty
"""