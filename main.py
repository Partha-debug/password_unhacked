# A simple password manager tool

from pwd_manager import Password_manager

def show_logo():

    print("""
                        PASSWORD
  _    _ _   _ _    _          _____ _  ________ _____  
 | |  | | \ | | |  | |   /\   / ____| |/ /  ____|  __ \ 
 | |  | |  \| | |__| |  /  \ | |    | ' /| |__  | |  | |
 | |  | | . ` |  __  | / /\ \| |    |  < |  __| | |  | |
 | |__| | |\  | |  | |/ ____ \ |____| . \| |____| |__| |
  \____/|_| \_|_|  |_/_/    \_\_____|_|\_\______|_____/ 
                                                        
                                            ©Partha-debug                                                                                                                                                                
         """)


def pswd_check_main():

    provided_pswd = input("Please enter your password to check it's strength: ").strip()

    pswd_checker = Password_manager()

    strength_profiles = pswd_checker.check_pswd(provided_pswd)

    if (strength_profiles['lnth'] >= 8) & (strength_profiles['smal'] >=2) & (strength_profiles['cptl'] >=2) & (strength_profiles['num'] >=2) & (strength_profiles['spcl_chr'] >=2):
        print(f"\n[+]Your password is strong it is of {strength_profiles['lnth']} characters contains {strength_profiles['smal']} small {strength_profiles['cptl']} capital {strength_profiles['num']} numeric and {strength_profiles['spcl_chr']} special characters.") 

    elif (strength_profiles['lnth'] >= 6) & (strength_profiles['smal'] >=1) & (strength_profiles['cptl'] >=1) & (strength_profiles['num'] >=1) & (strength_profiles['spcl_chr'] >=1):
        print(f"\n[-] Your password is of medium strength it is of {strength_profiles['lnth']} characters contains {strength_profiles['smal']} small {strength_profiles['cptl']} capital {strength_profiles['num']} numeric and {strength_profiles['spcl_chr']} special characters.\n\n[+] A Strong password must contain atleast 2 capital, 2 small,2 numeric and 2 special characters...") 
    else:
        print(f"\n[-] Your password is weak it is of {strength_profiles['lnth']} characters contains {strength_profiles['smal']} small {strength_profiles['cptl']} capital {strength_profiles['num']} numeric and {strength_profiles['spcl_chr']} special characters.\n\n[+]A Strong password must contain atleast 2 capital, 2 small,2 numeric and 2 special characters...")


def pwned_check_main():

    provided_pswd = input("Please enter your password to check it's in the hacked password's database: ").strip()
    pwned_checker = Password_manager()

    try:
        pwned_info = pwned_checker.is_pwned(provided_pswd)

        if pwned_info:
            print(f"\n[-] Your password was found in {pwned_info} hacked password data bases, change it as soon as possible...")
        else:
            print("\n[+] You got a secure password, There is no instance of this password in the hacked password databases...")
    except ConnectionError:
        print("There occured some error while connecting, Please check your network connection and try again!")


def pswd_gen_main():

    try:
        provided_length = int(
            input("Please enter the length of the random password you want to generate, It's length must be of atleast 8 characters: ").strip())
        if provided_length >= 8:
            pass
        else:
            provided_length = int(input(
                "Invalid length, Please enter a valid intiger which is greater than or equals to 8: ").strip())

    except ValueError:
        provided_length = int(input(
            "The length can only be an integer, Please enter a valid value greater than or equals to 8: ").strip())

    used_site = input(
        "please enter the website where you want to use this password: ").strip()

    if used_site:
        pass
    else:
        used_site = input(
            "You can't leave this field blank, please enter the website where you want to use this password: ").strip()

    print(
        f"\n[+] Generating a strong password with {provided_length} characters... ")


    pswd_manager = Password_manager()
    generated_pswd = pswd_manager.strong_pswd(provided_length, used_site)

    print(
        f"\n[+] Your generated {used_site} password is '{generated_pswd}', It will be saved in the passwords.txt file")


def main():

    print("Please choose a option: ")
    print("[+] 1 - Check the strength of your password.")
    print("[+] 2 - Check if your password is compromised before. (Requires internet connection)")
    print("[+] 3 - Generate a strong random password.")
    
    choice = input().strip()

    if choice == '1':
        pswd_check_main()

        print("\nHit enter to go back to home screen")
        print("Enter any other key to exit.")
        
        opt = input()
        
        if opt == '':
            main()
        else:
            raise KeyboardInterrupt

    elif choice == '2':
        pwned_check_main()

        print("\nHit enter to go back to home screen")
        print("Enter any other key to exit.")
        
        opt = input()
        
        if opt == '':
            main()
        else:
            raise KeyboardInterrupt

    elif choice == '3':
        pswd_gen_main()

        print("\nHit enter to go back to home screen.")
        print("Enter any other key to exit.")
        
        opt = input()
        
        if opt == '':
            print('\n')
            main()
        else:
            raise KeyboardInterrupt
    else:
        print("Invalid choice please try again!")
        print('\n')
        main()


if __name__ == "__main__":

    try:
        show_logo()
        main()
    except KeyboardInterrupt:
        print("Exiting...\n")
    except Exception as e:
        print(f"Some error occured, error details: {e}")
    