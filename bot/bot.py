from helper import *
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import numpy as np





class Bot:
    def __init__(self):
        pass

    def before_turn(self, playerInfo):
        """
        Gets called before ExecuteTurn. This is where you get your bot's state.
            :param playerInfo: Your bot's current state.
        """
        self.PlayerInfo = playerInfo

        




    def execute_turn(self, gameMap, visiblePlayers):
        return create_attack_action(Point(0,-1))
        """This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players."""
        x = self.PlayerInfo.Position.x
        y = self.PlayerInfo.Position.y
        x = x - gameMap.xMin
        y = y - gameMap.yMin
        
       
        matrice = (gameMap.prin()[1]).tolist()
        grid = Grid(matrix=matrice)

        resources = gameMap.prin()[0]
        print(resources)
        liste = []
        for resource in resources:
            print(resource.Position.x,resource.Position.y)
            liste.append(resource)
        print(liste)
        
        start = grid.node(x,y)
        end = grid.node((45 - gameMap.xMin),(8 - gameMap.yMin))

        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, grid)

        print('operations:', runs, 'path length:', len(path))
        print(grid.grid_str(path=path, start=start, end=end))
        
        #Write your bot here. Use functions from aiHelper to instantiate your actions.
        
        a=np.array(path)        
        print(a)
        print(str(np.subtract(a[1],a[0]).tolist()))
        return create_move_action(Point((np.subtract(a[0],a[1]).tolist())[0],(np.subtract(a[0],a[1]).tolist())[1]))



  

    


    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass


    
