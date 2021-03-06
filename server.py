import os

import cherrypy

from board import Board
from move import determine_move

"""
This is a simple Battlesnake server written in Python.
For instructions see https://github.com/BattlesnakeOfficial/starter-snake-python/README.md
"""


class Battlesnake(object):

    games = dict()

    @cherrypy.expose
    def index(self):
        # If you open your snake URL in a browser you should see this message.
        return "Ongoing games: {}".format(self.games)

    @cherrypy.expose
    def ping(self):
        # The Battlesnake engine calls this function to make sure your snake is working.
        return "pong"

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def start(self):
        # This function is called everytime your snake is entered into a game.
        # cherrypy.request.json contains information about the game that's about to be played.
        # TODO: Use this function to decide how your snake is going to look on the board.
        data = cherrypy.request.json
        print("START")
        game_id = self.game_id(data)
        height = data["board"]["height"]
        width = data["board"]["width"]
        board = Board.from_height_and_width(height, width)
        board.update(data)
        self.games[game_id] = board

        return {"color": "#1a9128", "headType": "bendr", "tailType": "skinny"}

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def move(self):
        # This function is called on every turn of a game. It's how your snake decides where to move.
        # Valid moves are "up", "down", "left", or "right".
        # TODO: Use the information in cherrypy.request.json to decide your next move.
        data = cherrypy.request.json
        board = self.game_board(data)
        board.update(data)
        move = determine_move(board)

        print(f"MOVE: {move}")
        return {"move": move}

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def end(self):
        # This function is called when a game your snake was in ends.
        # It's purely for informational purposes, you don't have to make any decisions here.
        data = cherrypy.request.json
        game_id = self.game_id(data)
        print("Ending game {}".format(game_id))
        del self.games[game_id]
        return "ok"

    def game_board(self, data):
        game_id = self.game_id(data)
        return self.games[game_id]

    def game_id(self, data):
        return data["game"]["id"]


if __name__ == "__main__":
    server = Battlesnake()
    cherrypy.config.update({"server.socket_host": "0.0.0.0"})
    cherrypy.config.update(
        {"server.socket_port": int(os.environ.get("PORT", "8080")),}
    )
    print("Starting Battlesnake Server...")
    cherrypy.quickstart(server)
