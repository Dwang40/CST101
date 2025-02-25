# Imports 
import time
import math
import random
import main
import check
import encounter
import command

#How much a player deals to an enemy
def playerDamage(player, enemy):
    damage = math.floor((player[2] * 1.5) - enemy[2])
    if(damage < 0):
        return 0;
    else:
        return damage

#How much a enemy deals to an player
def enemyDamage(enemy, player):
    damage = math.floor((enemy[1] * 1.5) - player[3])
    if(damage < 0):
        return 0;
    else:
        return damage
