############### initialization ###############

from random import randint
import time
#from player_t import player_turn
#import player_t

############### player stats ###############

player_init_hp = 100
player_punch_force = 15
#player_kick_force = 10
player_punch_accuracy = 0.6
#player_kick_accuracy = 0.3
player_dodge_chance = 0.2

#------------------------
player_hand = ('л', 'п')
player_punch_type = ('п', 'х', 'а')
player_block = ('л', 'п')



############### enemy stats ###############

enemy_init_hp = 100
enemy_punch_force = 14
#enemy_kick_force = 10
enemy_punch_accuracy = 0.5
#enemy_kick_accuracy = 0.3
enemy_dodge_chance = 0.2

#------------------------
enemy_hand = ('л', 'п')
enemy_punch_type = ('п', 'х', 'а')
enemy_block = ('л', 'п')



############### player turn ###############

def chance(a):
    from random import randint 
    rand = randint(1, 100)
    if a * 100 >= rand:  #defines if player is hitted or missed
        return 1
    else:
        return 0

#player_hit = chance(player_punch_accuracy)
#player_dodge = chance(player_dodge_chance)


############### enemy turn ###############

#enemy_turn()




############### hints ###############



############### fight ###############
def fight():
    global player_taken_damage
    global enemy_taken_damage
    global player_taken_damage_print
    global enemy_taken_damage_print
    global player_given_damage
    global enemy_given_damage
    global player_given_damage_print
    global enemy_given_damage_print

#   ############ player_turn ############
    player_hit = chance(player_punch_accuracy)
    player_dodge = abs(1 - chance(player_dodge_chance))
    player_hand_which = input("рука (л, п): ")

    
    if player_hand_which == player_hand[0]:
        print("руки совпали")
    else:
        print("руки не совпали")
    
#   ############ enemy_turn ############
    enemy_hit = chance(enemy_punch_accuracy)
    enemy_dodge = abs(1 - chance(enemy_dodge_chance))
    enemy_hand_which = enemy_hand[chance(0.5)]
    print(enemy_hand_which)

    
    #---player's damage
    player_given_damage = player_punch_force * player_hit #defines how much damage player will provide
    if player_hit == 0:
        player_given_damage_print = "You missed!"
    else:
        player_given_damage_print = str(player_given_damage)
    
    #---enemy's damage
    enemy_given_damage = enemy_punch_force * enemy_hit #defines how much damage enemy will provide
    if enemy_hit == 0:
        enemy_given_damage_print = "Enemy missed!"
    else:
        enemy_given_damage_print = str(enemy_given_damage)
    #---damage to player
    #player_dodge
#    print(player_dodge)
#    player_dodge = 0
    player_taken_damage = enemy_given_damage * player_dodge
    if player_dodge == 0:
        player_taken_damage_print = "You dodged!"
    else:
        player_taken_damage_print = str(player_taken_damage)

    #---damage to enemy
    #enemy_dodge
    enemy_taken_damage = player_given_damage * enemy_dodge
    if enemy_dodge == 0:
        enemy_taken_damage_print = "Enemy dodged!"
    else:
        enemy_taken_damage_print = str(enemy_taken_damage)

player_hp = player_init_hp
enemy_hp = enemy_init_hp
while (player_hp >= 1) and (enemy_hp >= 1):
#    turn = input("Press Enter to fight")
    time.sleep(1/5)
    fight()
    player_hp = player_hp - player_taken_damage
    enemy_hp = enemy_hp - enemy_taken_damage


    print("{:>20} {:<12} {:>20} {:<12}".format("Правая рука:", player_given_damage_print, "Правая рука:", enemy_given_damage_print))
    print("{:>20} {:<12} {:>20} {:<12}".format("Левая рука:", player_given_damage_print, "Левая рука:", enemy_given_damage_print))
    print("{:>20} {:<12} {:>20} {:<12}".format("Player's damage:", player_given_damage_print, "Enemy's damage:", enemy_given_damage_print))
    print("{:>20} {:<12} {:>20} {:<12}".format("Damage to player:", player_taken_damage_print, "Damage to enemy:", enemy_taken_damage_print))
    print("{:>20} {:<12} {:>20} {:<12}".format("Player's HP:", player_hp, "Enemy's HP:", enemy_hp))
#    print("{:>20} {:<12} {:>20} {:<12}".format("Player's dodge:", abs(player_dodge - 1), "Enemy's dodge:", abs(enemy_dodge-1))) #abs - absolute number (without minus)
    if (player_hp < 1) and (enemy_hp < 1):
        print("No one survived")
    elif player_hp < 1:
        print("You lose")
    elif enemy_hp < 1:
        print("You win")
    

#import sampl
#print (sampl)
#print (sampl_var)
#print (sampl.u)
#print (arg)
#funct()









