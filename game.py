
class Game:
    def __init__(self):
  
        self.leaderboard = {}


  def readJson(self):
        try:
            with open("leaderboard.json", "r") as read_file:
                self.leaderboard = json.load(read_file)
        except Exception as e:
            pass

    def writeJson(self):

        try:
            with open("leaderboard.json", "w") as write_file:
                json.dump(self.leaderboard, write_file, indent=4)
        except Exception as e:
            pass

    def show_leaderboard(self):
        self.readJson()
        print("""
    ***************************
    Welcome to Don't Hang Me Game, lets see how long you can survive!!!
    """)