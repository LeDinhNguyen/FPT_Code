from server import Server
from formula import distance

class User:
    def __init__(self, location: tuple) -> None:
        self.location: tuple = location
    
    def find_nearby_servers(self, server_list: list[tuple], radius: float = 1) -> list[Server]:
        nearby_servers = []
        for server in server_list:
            if distance(self.location, server) < radius:
                nearby_servers.append(Server(server))
        return nearby_servers

def main():
    return 0


if __name__ == "__main__":
    main()