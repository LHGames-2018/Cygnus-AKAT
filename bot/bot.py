from helper import *


class Bot:
    def __init__(self):
        pass

    def before_turn(self, playerInfo):
        return create_move_action(Point(0, 1))
        
        """
        Gets called before ExecuteTurn. This is where you get your bot's state.
            :param playerInfo: Your bot's current state.
        """
        self.PlayerInfo = playerInfo

    def execute_turn(self, gameMap, visiblePlayers):
        
        """
        This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players.
        """

        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        
    
    

    def after_turn(self):
        return create_move_action(Point(0, 1))
        """
        Gets called after executeTurn
        """
        pass
