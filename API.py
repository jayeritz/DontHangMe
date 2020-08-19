
import requests


class API:

    def __init__(self):
        self.url = "https://hangman-api.herokuapp.com/hangman"
        self.token = ""
        self.string = ""
        self.init()

    def init(self):
        try:
            res = requests.post(self.url)
        except Exception as e:
            print(e)
        else:
            if(res.status_code != 200):
                print("Server Error")
            else:
                self.token = res.json()['token']
                self.string = res.json()['hangman']

    def guess(self, letter):
        param = {
            "token": self.token,
            "letter": letter
        }

        try:
            res = requests.put(self.url, params=param)
        except Exception as e:
            print(e)
        else:
            self.string = res.json()['hangman']
            return res.json()['correct']

    def getSolution(self):
        param = {
            "token": self.token
        }
        try:
            res = requests.get(self.url, params=param)
        except Exception as e:
            print(e)
        else:
            return res.json()['solution']



    def getString(self):
        return self.string


# DEBUG CODE
if __name__=="__main__":
    test = API()
    print(len(test.getString()))
    print(test.getSolution())
    i = input()
    print(test.guess(i))
    print(test.getString())

