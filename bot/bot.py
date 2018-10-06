from helper import *


class Bot:
    def init(self):
        pass

    def before_turn(self, playerInfo):
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
        resources = gameMap.print()
        print("PLAYER POSITION: " + str(self.PlayerInfo.Position.x) + ',' + str(self.PlayerInfo.Position.y))
        for resource in resources:
            print("RESOURCE FOUND: " + str(resource.Position.x) + "," + str(resource.Position.y))

            print("HOUSE FOUND: " + str(self.PlayerInfo.HouseLocation.x) + "," + str(self.PlayerInfo.HouseLocation.y))
            if self.PlayerInfo.CarryingCapacity > 1000 and self.PlayerInfo.Position.x < self.PlayerInfo.HouseLocation.Position.x:
                    return create_move_action(Point(1, 0))

            if self.PlayerInfo.CarryingCapacity > 1000 and self.PlayerInfo.Position.x > self.PlayerInfo.HouseLocation.Position.x:
                    return create_move_action(Point(-1, 0))

            if self.PlayerInfo.CarryingCapacity > 1000 and self.PlayerInfo.Position.y > self.PlayerInfo.HouseLocation.Position.y:
                    return create_move_action(Point(0, 1))

            if self.PlayerInfo.CarryingCapacity > 1000 and self.PlayerInfo.Position.y < self.PlayerInfo.HouseLocation.Position.y:
                    return create_move_action(Point(0, -1))

            if self.PlayerInfo.Position.x < resources[0].Position.x:
                    return create_move_action(Point(1, 0))

            if self.PlayerInfo.Position.x > resources[0].Position.x:
                    return create_move_action(Point(-1, 0))

            if self.PlayerInfo.Position.y < resources[0].Position.y - 1:
                    return create_move_action(Point(0, 1))

            if self.PlayerInfo.Position.y > resources[0].Position.y - 1:
                    return create_move_action(Point(0, -1))

            if self.PlayerInfo.Position.y == resources[0].Position.y-1 and self.PlayerInfo.Position.x == resources[0].Position.x:
                    return create_collect_action(Point(0, 1))

    def after_turn(self):
            """
            Gets called after executeTurn
            """
            pass
