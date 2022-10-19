import requests
import json
import pymongo

class Player():
    def __init__(self, data):
        self.file = data
        self.player_data = {'name': self.file['name'], 'id': self.file['id']['id'], 'platform': self.file['id']['platform']}
        self.player_stats = self.file['stats']['core']
        self.player_boost_stats = {x: self.file['stats']['boost'][x] for x in ['bpm', 'avg_amount', 'amount_collected', 'amount_stolen', 'amount_overfill', 'amount_overfill_stolen', 'amount_used_while_supersonic', 'time_zero_boost', 'time_full_boost']}
        self.player_movement_stats = {x: self.file['stats']['movement'][x] for x in ['avg_speed', 'total_distance', 'time_supersonic_speed', 'time_boost_speed', 'time_slow_speed', 'time_ground', 'time_low_air', 'time_high_air', 'time_powerslide', 'time_powerslide', 'time_powerslide', 'count_powerslide', 'avg_powerslide_duration']}
        self.player_demo_stats = {f"demos {x}": self.file['stats']['demo'][x] for x in ['inflicted', 'taken']}

    def display_player_data(self):
        for x in self.player_data:
            print(f"{x}: {self.player_data[x]}")
        for x in self.player_stats:
            print(f"{x}: {self.player_stats[x]}")
        for x in self.player_boost_stats:
            print(f"{x}: {self.player_boost_stats[x]}")
        for x in self.player_movement_stats:
            print(f"{x}: {self.player_movement_stats[x]}")
        for x in self.player_demo_stats:
            print(f"{x}: {self.player_demo_stats[x]}")

class Replay():
    def __init__(self, file):
        self.blue_team = [Player(x) for x in file['blue']['players']]
        self.orange_team = [Player(x) for x in file['orange']['players']]

    def parse_data(self):
        pass

class Ballchasing():
    def __init__(self, key):
        self.key = key
        self.upload_url = "https://ballchasing.com/api/v2/upload?visibility=public"
        self.get_replay_url = "https://ballchasing.com/api/replays/"

    def upload_replay(self, replay):
        pass

    def get_replay(self, id):
        r = requests.get(url = f"{self.get_replay_url}{id}", headers = {'Authorization': self.key})
        data = r.json()
        return Replay(r.json())
    



if __name__ == "__main__":
    api = Ballchasing("ZMteLc7brLqXYuexmqeppeuXJPXZLBxKnalz4y3x")
    file = api.get_replay("a813182a-d3a8-4bbb-8f92-89b48a160afd")
    data = file.parse_data()

    client = pymongo.MongoClient("mongodb+srv://Eth:Aidan3546*@ballchasing.bp7zecs.mongodb.net/test")

    database = client.get_database('ballchasing-data')
    # database.create_collection('yoo')

    print(database)


    print('finished task')

