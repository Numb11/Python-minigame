import smtplib,hashlib
from random import randint

SENDER_EMAIL = "tempforproject2@gmail.com"
SERVER = smtplib.SMTP("smtp.gmail.com",587) #put in main
hash = hashlib.new("sha256")


def view_leaderboard():
        leaderboard = open("leaderboard", "r")
        print("The leaderboard is as follows: ")
        for i in list(lambda x: x.append(scores) for scores in leaderboard.readlines()):
            print(i)
        leaderboard.close()
        return None


class Player:

    def __init__ (self,name,email):
        self.name = name
        self.email = email

    def verify(self):
        emails = open("emails.txt", "r")
        hash.update((self.email).encode())
        if hash.hexdigest() in emails.readlines():
            print("Account verified")
            return True
        emails.close()


        OTP = "".join([str(randint(1,9)) for i in range(5)])
        SERVER.starttls()
        SERVER.login(SENDER_EMAIL, "mkbjvnpaqckszzso")
        try:
            SERVER.sendmail(SENDER_EMAIL, self.email, f"Your unique OTP (One Time Password) is {OTP}")
        except:
            print("incorrect email format, restart program")
            return False
        
        print("A OTP has been sent to your email inbox to verify your account.")

        for i in range(3):
            if input("Please enter the unique password: ") == OTP:
                print("Account verified")
                emails = open("emails.txt","a")
                emails.write(hash.hexdigest())
                emails.close()
                return True
            
        print("You have reached the maximum verification tries, try again later.")

    def store_score (self,score):
        leaderboard = open("leaderboard","a")
        leaderboard.write(self.name, score)
        leaderboard.close()
        
