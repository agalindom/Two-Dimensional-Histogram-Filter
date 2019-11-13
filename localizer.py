import pdb
from helpers import normalize, blur
import numpy as np

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []
    inter_ = []
    #
    # TODO - implement this in part 2
    #
    height = len(beliefs)
    width = len(beliefs[0])
    for i in range(height):
        row = []
        for j in range(width):
            belief = beliefs[i][j]
            g = grid[i][j]
            hit = (color == g)
            row.append(belief * (hit * p_hit + (1-hit) * p_miss))
        inter_.append(row)
    
    inter_sum = np.matrix(inter_).sum()
    
    for i in range(height):
        row = []
        for j in range(width):
            belief = beliefs[i][j]
            g = grid[i][j]
            hit = (color == g)
            row.append((belief * (hit * p_hit + (1-hit) * p_miss))/inter_sum)
        
        new_beliefs.append(row)
    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i - dy ) % height
            new_j = (j - dx ) % width
            #pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)