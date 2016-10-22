#!usr/bin/python3
############### initialization ###############

from random import randint
#from player_t import player_turn

############### player stats ###############

player_init_hp = 100
player_punch_force = 15
#player_kick_force = 10
player_punch_accuracy = 0.6
#player_kick_accuracy = 0.3
player_dodge_chance = 0.2



############### enemy stats ###############

enemy_init_hp = 100
enemy_punch_force = 14
#enemy_kick_force = 10
enemy_punch_accuracy = 0.5
#enemy_kick_accuracy = 0.3
enemy_dodge_chance = 0.2




############### player turn ###############

def player_turn():
    global player_dodge
    global player_hit

    player_hit_random = randint(1, 100)
    if player_hit_random <= player_punch_accuracy * 100:  #defines if player is hitted or missed
        player_hit = 1
    else:
        player_hit = 0
    #print(player_hit)
#    player_given_damage = player_punch_force * player_hit #defines how much damage player will provide
#    print (player_given_damage)

    player_dodge_random = randint(1, 100)
    if player_dodge_random <= player_dodge_chance * 100:  #defines if player is dodged or not
        player_dodge = 0 #player will dodge
    else:
        player_dodge = 1 #player won't dodge



############### enemy turn ###############

def enemy_turn():
    global enemy_dodge
    global enemy_hit

    enemy_hit_random = randint(1, 100)
    if enemy_hit_random <= enemy_punch_accuracy * 100:  #defines if enemy is hitted or missed
        enemy_hit = 1
    else:
        enemy_hit = 0
    #print(enemy_hit)
#    enemy_given_damage = enemy_punch_force * enemy_hit #defines how much damage enemy will provide
#    print (enemy_given_damage)

    enemy_dodge_random = randint(1, 100)
    if enemy_dodge_random <= enemy_dodge_chance * 100:  #defines if enemy is dodged or not
        enemy_dodge = 0 #enemy will dodge
    else:
        enemy_dodge = 1 #enemy won't dodge


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
#    from player_t import player_turn         ###################################################
    player_turn()
    enemy_turn()
    #---player's damage
    player_given_damage = player_punch_force * player_hit #defines how much damage player will provide
    if player_hit == 0:
        player_given_damage_print = "You missed!"
    else:
#        player_given_damage_print = str(player_given_damage)
        player_given_damage_print = "You hit him!"
    
    #---enemy's damage
    enemy_given_damage = enemy_punch_force * enemy_hit #defines how much damage enemy will provide
    if enemy_hit == 0:
        enemy_given_damage_print = "Enemy missed!"
    else:
#        enemy_given_damage_print = str(enemy_given_damage)
        enemy_given_damage_print = "Enemy hits you!"
    #---damage to player
    #player_dodge
#    print(player_dodge)
#    player_dodge = 0
    player_taken_damage = enemy_given_damage * player_dodge
    if player_dodge == 0:
        player_taken_damage_print = "You dodged!"
    else:
        player_taken_damage_print = str(0-player_taken_damage)
        
    #---damage to enemy
    #enemy_dodge
    enemy_taken_damage = player_given_damage * enemy_dodge
    if enemy_dodge == 0:
        enemy_taken_damage_print = "Enemy dodged!"
    else:
        enemy_taken_damage_print = str(0-enemy_taken_damage)

player_hp = player_init_hp
enemy_hp = enemy_init_hp
while (player_hp >= 1) and (enemy_hp >= 1):
    turn = input("Press Enter to fight")
    fight()
    player_hp = player_hp - player_taken_damage
    enemy_hp = enemy_hp - enemy_taken_damage
#"""
#    print("%30s %-10s %30s %-10s" % ("Player's damage:", player_given_damage_print, "Enemy's damage:", enemy_given_damage_print))
#    print("%30s %3d %30s %3d" % ("Damage to player:", player_taken_damage, "Damage to enemy:", enemy_taken_damage))
#    print("%30s %3d %30s %3d" % ("Player's HP:", player_hp, "Enemy's HP:", enemy_hp))
#    print("%30s %3d %30s %3d" % ("Player's dodge:", abs(player_dodge - 1), "Enemy's dodge:", abs(enemy_dodge-1))) #abs - absolute number (without minus)
#"""

    print("{:>20} {:<16} {:>30} {:<7}".format("Player's damage:", player_given_damage_print, "Enemy's damage:", enemy_given_damage_print))
#    print("{:>20} {:<12} {:>20} {:<12}".format("Damage to player:", player_taken_damage_print, "Damage to enemy:", enemy_taken_damage_print))
    print("{:>20} {:<3} {:<12} {:>30} {:<3} {:<12}".format("Player's HP:", player_hp, player_taken_damage_print, "Enemy's HP:", enemy_hp, enemy_taken_damage_print))
#    print("{:>20} {:<12} {:>20} {:<12}".format("Player's dodge:", abs(player_dodge - 1), "Enemy's dodge:", abs(enemy_dodge-1))) #abs - absolute number (without minus)

    if (player_hp < 1) and (enemy_hp < 1):
        print("No one survived")
    elif player_hp < 1:
        print("You lose")
    elif enemy_hp < 1:
        print("You win")
    

#print("%20s %2d %20s %2d" % ("Player's damage:", player_given_damage, "Enemy's damage:", enemy_given_damage))
#print("%20s %2d %20s %2d" % ("Damage to player:", player_taken_damage, "Damage to enemy:", enemy_taken_damage))
#print("%20s %2d %20s %2d" % ("Player's HP:", player_hp, "Enemy's HP:", enemy_hp))
#import sampl
#print (sampl)
#print (sampl_var)
#print (sampl.u)
#print (arg)
#funct()









