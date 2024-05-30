from math import sqrt

def find_closer(x: float,y: float) -> tuple[int, int]:
    """return the closest point around (x,y)

    Args:
        x (float): coordinate x of the point
        y (float): coordinate y of the point

    Returns:
        tuple[int, int]: the closest point around (x,y)
    """
    coords_around:list[tuple[int,int]]=[]
    for i in range(2):
        point_y:int=int(y)+i
        ajout:list[tuple[int,int]]=[(int(x),point_y),(int(x)+2,point_y)]if int(x)%2==int(not((point_y+1)%2)) else [(int(x)-1,point_y),(int(x)+1,point_y)]
        coords_around.extend(ajout)
    
    closest:tuple[int,int]=coords_around[0]
    closest_dist:float=compute_distance((x,y),coords_around[0])
    for i in range(1,4):
        temp_dist:float=compute_distance((x,y),coords_around[i])
        closest=closest if closest_dist<temp_dist else coords_around[i]
        closest_dist=closest_dist if closest_dist<temp_dist else temp_dist
        
    return closest

def compute_distance(coord1 : tuple[int,int],coord2 : tuple[int,int]) -> float:
    """Compute the distance between coord1 and coord2

    Args:
        coord1 (tuple[int,int]): the first coordinate
        coord2 (tuple[int,int]): the second coordinate

    Returns:
        float: the distance between coord1 and coord2
    """
    distance:float=sqrt((coord1[0]-coord2[0])**2+(coord1[1]-coord2[1])**2)
    return distance

def position_in_list(x: int,y: int, liste: list) -> bool:
    """check if an element with coordinate (x,y) is in the list

    Args:
        x (int): coordinate x of the searched element
        y (int): coordinate y of the searched element
        liste (list): list of elements in which we search

    Returns:
        bool: true if an element with coordinate (x,y) is in the list
    """
    for elem in liste:
        if elem.get_box()==(x,y):
            return True
    return False

def get_index(x:int,y:int,liste: list) -> int:
    """return the index of an element with coordinate (x,y)

    Args:
        x (int): coordinate x of the searched element
        y (int): coordinate y of the searched element
        liste (list): list of elements in which we search

    Returns:
        int: index of an element with coordinate (x,y) in the list
    """
    for i in range(len(liste)):
        if liste[i].get_box()==(x,y):
            return i
    return -1

def find_line_player(player:int,liste:list) -> int:
    """return the index of the line of the player

    Args:
        player (int): the player number
        liste (list): the list in which we search

    Returns:
        int: the index of the line of the player in the list
    """
    for i in range(len(liste[2:])):
        if liste[2+i][1]==player:
            return i
    return -1

def get_middle(x1:int,y1:int,x2:int,y2:int) -> tuple[int,int]:
    """find the middle point of a line

    Args:
        x1 (int): x coord of the first point
        y1 (int): y coord of the first point
        x2 (int): x coord of the second point
        y2 (int): y coord of the second point

    Returns:
        tuple[int,int]: the coords of the middle point
    """
    return (int((x1+x2)/2),int((y1+y2)/2))

def get_around_middle(x1:int,y1:int,x2:int,y2:int) -> tuple[tuple[int,int],tuple[int,int]]:
    """return the coords of the two points around the middle of the line

    Args:
        x1 (int): x coord of the first point of the line
        y1 (int): y coord of the first point of the line
        x2 (int): x coord of the second point of the line
        y2 (int): y coord of the second point of the line

    Returns:
        tuple[tuple[int,int],tuple[int,int]]: coords of the two points around the middle of the line in a tuple
    """
    diff_x:int=(x2-x1)/4
    diff_y:int=(y2-y1)/4
    middle:tuple[int,int]=get_middle(x1,y1,x2,y2)
    return ((int(middle[0]-diff_x),int(middle[1]-diff_y)),(int(middle[0]+diff_x),int(middle[1]+diff_y)))


def get_line_index(x:int,y:int,x1:int,y1:int,liste:list) -> int:
    """
    returns the index of the line selected in the list

    Args:
        x (int): x coord of the first point of the line
        y (int): y coord of the first point of the line
        x1 (int): x coord of the second point of the line
        y1 (int): y coord of the second point of the line
        liste (list): list of the lines in which we search

    Returns:
        int: -1 if the line made with the two points is not in the list or the index of the line in the list
    """
    for i in range(len(liste)):
        if ((x,y),(x1,y1))==liste[i][0]:
            return i
    return -1

def get_index_next_line(x:int,y:int,liste:list,act_index:int,player:int) -> int:
    """
    Returns the index of the next line with o point of coordinates x,y in its points

    Args:
        x (int): x coord of the point
        y (int): y coord of the point
        liste (list): list of lines 
        act_index (int): index of the actual line
        player (int): id of the player

    Returns:
        int: index of the first line coming after the actual one that has the point (x,y)
    """
    new_index:int=(act_index+1)%len(liste)
    while liste[new_index][1]!=player or (not pos_in_line(x,y,liste[new_index])):
        new_index=(new_index+1)%len(liste)
    return new_index
        
def pos_in_line(x:int,y:int,line:list) -> bool:
    """
    This function check if the point (x,y) is in the line

    Args:
        x (int): x coord of the point
        y (int): y coord of the point
        line (list): line in which we search

    Returns:
        bool: true if the point (x,y) is in the line False otherwise
    """
    if (float(x),float(y)) in line[0] or (x,y)==get_middle(line[0][0][0],line[0][0][1],line[0][1][0],line[0][1][1]) or (x,y) in get_around_middle(line[0][0][0],line[0][0][1],line[0][1][0],line[0][1][1]):
        return True
    return False

def possible_position(x:int,y:int,liste:list) -> bool:
    """
    Checks if a ring can be placed i the position 

    Args:
        x (int): x coord of the point
        y (int): y coord of the point
        liste (list): list of coordinates in which the pawn cannot be placed

    Returns:
        bool: True if the ring can be place on (x,y) false otherwise
    """
    return (x,y) not in liste and 1<=x<=11 and 1<=y<=19 and x%2==y%2

def get_all_index_line(player:int,liste:list) -> list[int]:
    """
    This method gets all the index of the lines of a player in a list and returns it

    Args:
        player (int): id of the player
        liste (list): list of the lines

    Returns:
        list: list of all the indices of the lines of the player selected 
    """
    return [i for i in range(len(liste)) if liste[i][1]==player]