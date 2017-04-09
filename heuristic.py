# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 12:20:43 2017

@author: RandySteven
"""



def available_moves(data):
    columns=[data.column1,data.column2,data.column3,data.column4,data.column5]
    available_cols = [abs(6-sum(b)) for b in columns]
    rows=[data.row1,data.row2,data.row3,data.row4,data.row5]
    available_rows = [abs(6-sum(b)) for b in rows]
    print(sum(available_cols)+sum(available_rows))
    

    
import dots

data=dots.RC();
board = dots.create_board(data)          
board =dots.make_a_move(data,'r',1,3)
board =dots.make_a_move(data,'c',1,1)
board =dots.make_a_move(data,'c',1,2)
print(board.gameboard)
print(dots.is_valid_move(data,'c',1,2))
available_moves(data)

