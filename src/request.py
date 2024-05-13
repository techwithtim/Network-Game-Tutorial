class Request:
    def __init__(self, id, player):
        self.id = id
        self.player = player

    def get_net_id(self):
        return int(self.id)
    
    def get_player(self):
        return self.player