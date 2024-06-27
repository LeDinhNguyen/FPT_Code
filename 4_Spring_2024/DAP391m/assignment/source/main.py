import pandas as pd

from user import User
from server import Server

def find_the_best_server(user: User, server_list: list[Server]):
    nearby_list = user.find_nearby_servers(server_list)
    best = nearby_list[0]
    for server in nearby_list:
        if len(server.available_users) < len(best.available_users):
            best = server
    return best

def main():
    users = pd.read_csv("../data/users/users-aus.csv")
    servers = pd.read_csv("../data/edge-servers/site.csv")

    user_list = list(users[["Latitude", "Longitude"]].itertuples(index=False, name=None))
    server_list = list(servers[["LATITUDE", "LONGITUDE"]].itertuples(index=False, name=None))
    user1 = User(user_list[0])

    # nearby_list = user1.find_nearby_servers(server_list)
    best_server = find_the_best_server(user1, server_list)
    print(best_server.location)
    return 0


if __name__ == "__main__":
    main()