


class Player:
    def __init__(self, player_name, latest_id):
        # self.random()
        self.name = player_name
        self.id = latest_id

class User_Manager:
  def __init__(self):
    self.first_ID = 1
    self.player_list = []

  def create_user(self):
    player_name = input(f"Hi! Who am I playing with today?\n")
    latest_id = self.first_ID
    new_player = Player(player_name, latest_id)
    self.player_list.append(new_player)
    print(f"Your game ID is: {latest_id}")
    self.first_ID += 1
    self.show_player()
    return(latest_id)

    
  def show_player(self):
    print("""
    **************************
    Don't Hang Me Leaderboard:
    """)
    for person in self.player_list:
      print(person)

    print("""

    **************************
    """)
    return print(f"player_list")

  def update_player(self):
    latest_id = int(input(f"Enter the ID of the player to update: \n"))
    latest_id = latest_id - 1
    player_name = input(f"What is the new name for player {latest_id}: \n")
    player_to_update = self.player_list[int(latest_id)]
    player_to_update.name = player_name
    return print(f"Your player information has been updated: {player_to_update}")
    self.show_player() 

  def delete_player(self):
    latest_id = int(input(f"Enter the ID of the player to delete: \n"))
    latest_id = latest_id - 1
    self.player_list.pop(latest_id)
    print(f"The player has been deleted!")
    self.show_player()  