from random import choice, shuffle
import hashlib
import requests


class Password_manager(object):

    def __init__(self):

        self.capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.small = self.capital.lower()
        self.number = '123546890'
        self.special_chr = '!@#$%^=&*_+|}{][)('

    def is_pwned(self, password):

        sha1_pswd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        check_pswd = sha1_pswd[5:]
        query_pswd = sha1_pswd[:5]
        url = f'https://api.pwnedpasswords.com/range/{query_pswd}'

        try:
            api_req = requests.get(url)
        except Exception:
            raise ConnectionError
        else:
            if api_req.status_code == 200:

                hash_val_list = api_req.text.rsplit()
                hash_dict = {}

                for hash_val in hash_val_list:
                    hash, val = hash_val.split(':')
                    hash_dict[hash] = val

                if check_pswd in hash_dict.keys():
                    return hash_dict[check_pswd]
                else:
                    return False
            else:
                raise ConnectionError

    def check_pswd(self, password):

        smal = 0
        cptl = 0
        num = 0
        spcl_chr = 0
        lnth = len(password)

        for char in password:

            if char in self.small:
                smal += 1

            if char in self.capital:
                cptl += 1

            if char in self.number:
                num += 1

            if char in self.special_chr:
                spcl_chr += 1

        return {'lnth': lnth, 'smal': smal, 'cptl': cptl, 'num': num, 'spcl_chr': spcl_chr}

    def strong_pswd(self, length, site):

        temp_pswd = ''

        while True:

            temp_pswd += choice(self.capital)
            if len(temp_pswd) == length:
                break

            temp_pswd += choice(self.small)
            if len(temp_pswd) == length:
                break

            temp_pswd += choice(self.number)
            if len(temp_pswd) == length:
                break

            temp_pswd += choice(self.special_chr)
            if len(temp_pswd) == length:
                break

        temp_pswd_lst = list(temp_pswd)
        shuffle(temp_pswd_lst)
        strong_pswd = ''.join(temp_pswd_lst)

        with open('passwords.txt', 'a') as file:
            file.write(f"{site} password : {strong_pswd}\n")

        return strong_pswd
