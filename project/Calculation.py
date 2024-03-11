from math import sqrt

def find_closer(x: float,y: float) -> tuple[int, int]:
    coords_around=[]
    for i in range(2):
        point_y=int(y)+i
        ajout=[(int(x),point_y),(int(x)+2,point_y)]if int(x)%2==int(not((point_y+1)%2)) else [(int(x)-1,point_y),(int(x)+1,point_y)]
        coords_around.extend(ajout)
    
    closest=coords_around[0]
    closest_dist=compute_distance((x,y),coords_around[0])
    for i in range(1,4):
        temp_dist=compute_distance((x,y),coords_around[i])
        closest=closest if closest_dist<temp_dist else coords_around[i]
        closest_dist=closest_dist if closest_dist<temp_dist else temp_dist
        
    return closest

def compute_distance(coord1 : tuple[int,int],coord2 : tuple[int,int]) -> float:
    distance=sqrt((coord1[0]-coord2[0])**2+(coord1[1]-coord2[1])**2)
    return distance