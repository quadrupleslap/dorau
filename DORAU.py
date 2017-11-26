#Multibattle
import random #this is to enable the dice rolls
import sys #guess what this does!
Para = [0]
ISkill = []
CSkill = []
IHP = []
CHP = []
ILuck = []
CLuck = [] #the above are all pretty self explanatory.
state = [0] #save state
Inventory = ['Business Suit','Watch','NOKIA Brick','Suitcase','American Express Card']
MSkill = []
MHP = []
MText = []
MName = []
d1 = 0
d2 = 0
HAttack = 0
MAttack = 0
result = 0
over = [0] #over is a list/integer that determines if the battle has been fought to the end. If not, at the load, you must fight it all over again
# with the enemies at full HP. If so, then you are free to go on without a battle. This is saved in the save file.
noRepeat = []
def warn():
    with open("warning.txt", "r") as dowdell:
        for line in dowdell:
            print(line.rstrip())
        choice = input('Do you agree to these terms? (1 for yes, 2 for no.) ')
        if choice == '1':
            pass
        elif choice == '2':
            print('Nice.')
            sys.exit()
        else:
            print('Just choose one.')
            print('Closing...')
            sys.exit()

def end(typ):
    if typ == 'bad':
        f = open('save' + str(state[0]) + '.txt', 'w')
        f.write("You have achieved the 'end.'")
        f.close()
        print("You seriously didn't even try, did you?")
        print('No, this is not the true ending.')
        sys.exit()
    elif typ == 'normal':
        f = open('save' + str(state[0]) + '.txt', 'w')
        f.write("You have achieved the end.")
        f.close()
        print('Congragulations for completion of the game.')
        print('But yet, this is not the end you are looking for.')
        sys.exit()
    elif typ == 'evil':
        f = open('save' + str(state[0]) + '.txt', 'w')
        f.write("This may be the end.")
        f.close()
        print('Close.... but no cigar.')
        print('Ram, this evil end is for you. Congrats.')
        sys.exit()
    elif typ == 'good':
        f = open('save' + str(state[0]) + '.txt', 'w')
        f.write("This is the end.")
        f.close()
        print('Well done for achieving the end!')
        print('Yes, Weber, you can screw around with it now.')
        sys.exit()    
def death():#DEATH WORKS NOW. It automatically terminates the program.
    print('')
    print('You have been slain.')
    print('The save file will now be deleted.')
    f = open('save' + str(state[0]) + '.txt', 'w')
    f.write('You have died.')
    f.close()
    print('You have been terminated. Better luck next time...?')
    sys.exit()
#The actual battle.
def bossBattle(HP, MHP, plot_num, d, dec, TempString, cont, timer): #WORKS? Note that boss battles are hard coded.
    #print(plot_num)
    #print(d)
    fire = 0
    if cont == 1: #continue existing battle, or to start new one?
        del MSkill[:]
        del MText [:]
        del MHP [:]
        del MName[:]
        readMonster(0, plot_num, 1)
    else:
        if '4' in noRepeat:
            noRepeat.remove('4')
            MSkill.append(CSkill[0] - 2)
            MSkill.remove(MSkill[0])
        elif '3' in noRepeat:
            noRepeat.remove('3')
            MSkill.append(CSkill[0] - 2)
            MSkill.remove(MSkill[0])
        elif '2' in noRepeat:
            noRepeat.remove('2')
            MSkill.append(CSkill[0] - 2)
            MSkill.remove(MSkill[0])
        elif '1' in noRepeat:
            noRepeat.remove('1')
            MSkill.append(CSkill[0] - 2)
            MSkill.remove(MSkill[0])
        elif '0' in noRepeat:
            noRepeat.remove('0')
            MSkill.append(CSkill[0] - 2)
            MSkill.remove(MSkill[0])
    if MSkill[0] == -2:
        MSkill.append(CSkill[0] - 2)
        MSkill.remove(MSkill[0])
    elif MSkill[0] == -1:
        MSkill.append(CSkill[0] - 1)
        MSkill.remove(MSkill[0])
    elif MSkill[0] == 0:
        MSkill.append(CSkill[0])
        MSkill.remove(MSkill[0])
        #print(MSkill[0])
    elif MSkill[0] == +2:
        MSkill.append(CSkill[0] + 2)
        MSkill.remove(MSkill[0])
    elif MSkill[0] == -3:
        MSkill.append(CSkill[0] - 3)
        MSkill.remove(MSkill[0])
    elif MSkill[0] == -4:
        MSkill.append(CSkill[0] - 4)
        MSkill.remove(MSkill[0])
    elif MSkill[0] == +6:
        MSkill.append(CSkill[0] + 6)
        MSkill.remove(MSkill[0])
        #print(MSkill[0]) #PRINTINGGGG
        if MName[0] == 'Mothership Core':
            if '0' in noRepeat:
                MSkill.append(MSkill[0] + 1)
                MSkill.remove(MSkill[0])
                timer = 1
            elif '1' in noRepeat:
                MSkill.append(MSkill[0] + 2)
                MSkill.remove(MSkill[0])
                timer = 2
            elif '2' in noRepeat:
                MSkill.append(MSkill[0] + 3)
                MSkill.remove(MSkill[0])
                timer = 3
            elif '3' in noRepeat:
                MSkill.append(MSkill[0] + 3)
                MSkill.remove(MSkill[0])
                timer = 4
            elif '4' in noRepeat:
                MSkill.append(MSkill[0] + 3)
                MSkill.remove(MSkill[0])
                timer = 5
            #print(MSkill[0])
    multi = 0 #this is to see which enemy you are fighting against currently.
            #print(MSkill)
            #print(MHP)
            #print(MText)
    #print(MSkill[0])
    #print(noRepeat)
    f = open('save' + str(state[0]) + '.txt', 'w') #more preventation
    f.write(str(plot_num)+ '\n'+ str(CSkill[0])+'/'+str(ISkill[0])+ '\n'+ str(HP)+'/'+str(IHP[0])+ '\n'+ str(CLuck[0])+'/'+str(ILuck[0]) + '\n' + str(over[0]))
    TempString = ''
    for i in noRepeat:
        TempString += i + '/'
    f.write('\n' + TempString.rstrip('/'))
    f.write('\n-INVENTORY-\n') #autosave works here now.
    for i in Inventory:
        f.write(i)
        f.write('\n')
    f.close() #Autosave end 
    print('NOTE: Attack fights as normal. Heavy attack deals 2 extra damage, but at the')
    print('cost of 2 SKILL during battle. (You may also have other commands!)')
    command = input('Action(A to attack, H for a heavy attack): ')
    while True:
        command = command.upper()
        if command == 'A':
            result = fightScene(HP, MHP[multi], 0, multi)
            if result == 0: #if you draw.
                print('You are evenly matched. You skillfully parry, and neither fighter gives ground.')
                if MName[multi] == 'Kerrigan':
                    print('Kerrigan strikes at you again!')
                    print()
                    result = fightScene(HP,MHP[multi], 0,multi)
                    if result == 0 or result == 1:
                        print("You just manage to block Kerrigan's second strike. Her eyes narrow.")
                    else:
                        print("Kerrigan attacks with her second 'wing.' You are overwhelmed. Lose 2 HEALTH.")
                        HP = HP -2
                elif MName[multi] == 'Weetbix':
                    print("Weetbix's strikes damage even itself, such is its power! It loses 2 HEALTH.")
                    MHP[0] = MHP[0] - 2
                elif MName[multi] == 'Skeleton Weetbix':
                    print("Weetbix's strikes damage even itself, such is its power! It loses 1 HEALTH.")
                    MHP[0] = MHP[0] - 1
                    fire+= 1
                    if fire == 5:
                        print('Weetbix fires a stream of green necrofire at you. You lose 4 HEALTH to this')
                        print('blistering heat!')
                        HP = HP - 4
                        fire = 0
            elif result == 1: #if you win.
                if MName[0] == 'Weetbix':
                    print('You strike Weetbix. However, due to its hard scales, it loses 1 HEALTH.')
                    MHP[0] = MHP[0]-1
                    print("Weetbix's strikes damage even itself, such is its power! It loses 2 HEALTH.")
                    MHP[0] = MHP[0] - 2
                elif MName[0] == 'Skeleton Weetbix':
                    roll = rollDie(d1)
                    if roll >= 5:
                        print('The dragon blocks your strike with green necrofire. It roars.')
                    else:
                        if '¤Scimitar¤' in Inventory or '¤Callandor¤' in Inventory:
                            print('You wound the '+MName[multi] +'. They lose 3 Health.')
                            MHP[multi] = MHP[multi] - 3
                        else:
                            print('You wound the '+MName[multi] +'. They lose 2 Health.')
                            MHP[multi] = MHP[multi] - 2
                    print("Weetbix's strikes damage even itself, such is its power! It loses 1 HEALTH.")
                    MHP[0] = MHP[0] - 1
                    fire+= 1
                    if fire == 5:
                        print('Weetbix fires a stream of green necrofire at you. You lose 4 HEALTH to this')
                        print('blistering heat!')
                        HP = HP - 4
                        fire = 0
                elif '¤Scimitar¤' in Inventory or '¤Callandor¤' in Inventory:
                    if MName[0] == 'Shayla':
                        print("You wound Shayla. She loses 3 HEALTH.")
                        MHP[0] = MHP[0] - 3
                    else:
                        print('You wound the '+MName[multi] +'. They lose 3 Health.')
                        MHP[multi] = MHP[multi] - 3
                        if MName[multi] == 'Kerrigan':
                            print('Kerrigan strikes at you again!')
                            print()
                            result = fightScene(HP,MHP[multi], 0,multi)
                            if result == 0 or result == 1:
                                print("You just manage to block Kerrigan's second strike. Her eyes narrow.")
                            else:
                                print("Kerrigan attacks with her second 'wing.' You are overwhelmed. Lose 2 HEALTH.")
                                HP = HP -2
                else:
                    if MName[0] == 'Shayla':
                        print('You wound the dark elf. She loses 2 HEALTH.')
                        MHP[0] = MHP[0] - 2
                    else:
                        print('You wound the '+ MName[multi]+'. They lose 2 Health.')
                        MHP[multi] = MHP[multi]-2
                        if MName[multi] == 'Kerrigan':
                            print('Kerrigan strikes at you again!')
                            print()
                            result = fightScene(HP,MHP[multi], 0,multi)
                            if result == 0 or result == 1:
                                print("You just manage to block Kerrigan's second strike. Her eyes narrow.")
                            else:
                                print("Kerrigan attacks with her second 'wing.' You are overwhelmed. Lose 2 HEALTH.")
                                HP = HP -2
            else: #if you lose.
                if MName[multi] == 'Mothership Core':
                    if timer < 3:
                        MSkill.append(MSkill[0] + 1)
                        MSkill.remove(MSkill[0])
                        #print(MSkill[0])
                        print("The Mothership Core glows with a brilliant light. It's SKILL is now " + str(MSkill[0]) + '!')
                        noRepeat.append(str(timer))
                        if timer != 0:
                            noRepeat.remove(str(timer -1))
                        #print(timer)
                    elif timer == 3:
                        print('It feels as if the orb probes into the depth of your being, in preparation to')
                        print('wipe you out. You shiver at this premunition.')
                        noRepeat.append(str(timer))
                        noRepeat.remove(str(timer -1))
                        #print(timer)
                    else:
                        print('The orb extends its tendrils past your blade, and saps your very life!')
                        print('Lose 4 HEALTH.')
                        HP = HP - 4
                        if '3' in noRepeat:
                            noRepeat.remove('3')
                        if '4' not in noRepeat:
                            noRepeat.append('4')
                        #print(timer)
                    timer += 1
                elif MName[multi] == 'Kerrigan':
                    print(MText[multi])
                    HP = HP - 2
                    print('Kerrigan strikes at you again!')
                    print()
                    result = fightScene(HP,MHP[multi], 0,multi)
                    if result == 0 or result == 1:
                        print("You just manage to block Kerrigan's second strike. Her eyes narrow.")
                    else:
                        print("Kerrigan attacks with her second 'wing.' You are overwhelmed. Lose 2 HEALTH.")
                        HP = HP -2
                elif MName[multi] == 'Weetbix':
                    print(MText[random.randint(0,2)])
                    HP = HP -2
                    print("Weetbix's strikes damage even itself, such is its power! It loses 2 HEALTH.")
                    MHP[0] = MHP[0] - 2
                elif MName[multi] == 'Skeleton Weetbix':
                    HP = HP - 2
                    print(MText[random.randint(0,2)])
                    print("Weetbix's strikes damage even itself, such is its power! It loses 1 HEALTH.")
                    MHP[0] = MHP[0] - 1
                    fire += 1
                    if fire == 5:
                        print('Weetbix fires a stream of green necrofire at you. You lose 4 HEALTH to this')
                        print('blistering heat!')
                        HP = HP - 4
                        fire = 0
                elif MName[multi] == 'Shayla':
                    if MSkill[0] == CSkill[0] - 2:
                        print(MText[random.randint(0,3)])
                        HP = HP -4
                    else:
                        print(MText[0])
                        HP = HP-1
                    
        elif command == 'H':
            result = fightScene(HP, MHP[multi], 1, multi)
            if result == 0:
                print('You swing your weapon, and the '+MName[multi]+ ' jukes, but is too slow to strike back.')
                if MName[multi] == 'Weetbix':
                    print("Weetbix's strikes damage even itself, such is its power! It loses 2 HEALTH.")
                    MHP[0] = MHP[0] - 2
                elif MName[multi] == 'Skeleton Weetbix':
                    print("Weetbix's strikes damage even itself, such is its power! It loses 1 HEALTH.")
                    MHP[0] = MHP[0] - 1
                    fire+= 1
                    if fire == 5:
                        print('Weetbix fires a stream of green necrofire at you. You lose 4 HEALTH to this')
                        print('blistering heat!')
                        HP = HP - 4
                        fire = 0
                elif MName[multi] == 'Kerrigan':
                    print('Kerrigan strikes at you again!')
                    print()
                    result = fightScene(HP,MHP[multi], 0,multi)
                    if result == 0 or result == 1:
                        print("You just manage to block Kerrigan's second strike. Her eyes narrow.")
                    else:
                        print("Kerrigan attacks with her second 'wing.' You are overwhelmed. Lose 2 HEALTH.")
                        HP = HP -2
            elif result == 1:
                if MName[0] == 'Weetbix':
                    print('You strike Weetbix. However, due to its hard scales, it loses 1 HEALTH.')
                    MHP[0] = MHP[0]-1
                    print("Weetbix's strikes damage even itself, such is its power! It loses 2 HEALTH.")
                    MHP[0] = MHP[0] - 2
                elif MName[0] == 'Skeleton Weetbix':
                    roll = rollDie(d1)
                    if roll >= 5:
                        print('The dragon blocks your strike with green necrofire. It roars.')
                    else:
                        if '¤Scimitar¤' in Inventory or '¤Callandor¤' in Inventory:
                            print('You strike at the ' + MName[multi] + ' with a double-handed grip. They lose 5')
                            print('health.')
                            MHP[multi] = MHP[multi] - 5
                        else:
                            print('You strike the '+ MName[multi]+' with a heavy blow. They lose 4 Health.')
                            MHP[multi] = MHP[multi] - 4
                    print("Weetbix's strikes damage even itself, such is its power! It loses 1 HEALTH.")
                    MHP[0] = MHP[0] - 1
                    fire+= 1
                    if fire == 5:
                        print('Weetbix fires a stream of green necrofire at you. You lose 4 HEALTH to this')
                        print('blistering heat!')
                        HP = HP - 4
                        fire = 0
                elif '¤Scimitar¤' in Inventory or '¤Callandor¤' in Inventory:
                    print('You strike at the ' + MName[multi] + ' with a double-handed grip. They lose 5 Health.')
                    MHP[multi] = MHP[multi] - 5
                    if MName[multi] == 'Kerrigan':
                        print('Kerrigan strikes at you again!')
                        print()
                        result = fightScene(HP,MHP[multi], 0,multi)
                        if result == 0 or result == 1:
                            print("You just manage to block Kerrigan's second strike. Her eyes narrow.")
                        else:
                            print("Kerrigan attacks with her second 'wing.' You are overwhelmed. Lose 2 HEALTH.")
                            HP = HP -2
                else:
                    print('You strike the '+ MName[multi]+' with a heavy blow. They lose 4 Health.')
                    MHP[multi] = MHP[multi]-4
                    if MName[multi] == 'Kerrigan':
                        print('Kerrigan strikes at you again!')
                        print()
                        result = fightScene(HP,MHP[multi], 0,multi)
                        if result == 0 or result == 1:
                            print("You just manage to block Kerrigan's second strike. Her eyes narrow.")
                        else:
                            print("Kerrigan attacks with her second 'wing.' You are overwhelmed. Lose 2 HEALTH.")
                            HP = HP -2
            else:
                if MName[multi] == 'Mothership Core':
                    if timer < 3:
                        MSkill.append(MSkill[0] + 1)
                        MSkill.remove(MSkill[0])
                        #print(MSkill[0])
                        print("The Mothership Core glows with a brilliant light. It's SKILL is now " + str(MSkill[0]) + '!')
                        noRepeat.append(str(timer))
                        if timer != 0:
                            noRepeat.remove(str(timer -1))
                        #print(timer)
                    elif timer == 3:
                        print('It feels as if the orb probes into the depth of your being, in preparation to')
                        print('wipe you out. You shiver at this premunition.')
                        noRepeat.append(str(timer))
                        noRepeat.remove(str(timer -1))
                        #print(timer)
                    else:
                        print('The orb extends its tendrils past your blade, and saps your very life!')
                        print('Lose 4 HEALTH.')
                        HP = HP - 4
                        if '3' in noRepeat:
                            noRepeat.remove('3')
                        if '4' not in noRepeat:
                            noRepeat.append('4')
                        #print(timer)
                    timer += 1
                elif MName[multi] == 'Kerrigan':
                    print(MText[multi])
                    HP = HP -2
                    print('Kerrigan strikes at you again!')
                    print()
                    result = fightScene(HP,MHP[multi], 0,multi)
                    if result == 0 or result == 1:
                        print("You just manage to block Kerrigan's second strike. Her eyes narrow.")
                    else:
                        print("Kerrigan attacks with her second 'wing.' You are overwhelmed. Lose 2 HEALTH.")
                        HP = HP -2
                elif MName[multi] == 'Weetbix':
                    print(MText[random.randint(0,2)])
                    HP = HP -2
                    print("Weetbix's strikes damage even itself, such is its power! It loses 2 HEALTH.")
                    MHP[0] = MHP[0] - 2
                elif MName[multi] == 'Skeleton Weetbix':
                    HP = HP - 2
                    print(MText[random.randint(0,2)])
                    print("Weetbix's strikes damage even itself, such is its power! It loses 1 HEALTH.")
                    MHP[0] = MHP[0] - 1
                    fire += 1
                    if fire == 5:
                        print('Weetbix fires a stream of green necrofire at you. You lose 4 HEALTH to this')
                        print('blistering heat!')
                        HP = HP - 4
                        fire = 0
                elif MName[multi] == 'Shayla':
                    if MSkill[0] == CSkill[0] - 2:
                        print(MText[random.randint(0,3)])
                        HP = HP -4
                    else:
                        print(MText[0])
                        HP = HP-1
                    
        elif command == 'GATORADE': #this is a stub for the hp potion things
            if 'Gatorade' in Inventory:
                HP = (IHP[0])
                print('The Gatorade grants you the will to fight on!')
                Inventory.remove('Gatorade')
            else:
                print("Despair! Play the hidden minigame, 'Where's my Gatorade?' to get more.")
        elif command == 'STAMINADE': #this is a stub for the hp potion things
            if 'Staminade' in Inventory:
                HP = (IHP[0])
                print('The Staminade regenerates health and beauty!')
                Inventory.remove('Staminade')
            else:
                print("Nope. All empty.")  
        elif command == 'STATS':
            print('These are your current stats:')
            print('SKILL: ' + str(CSkill[0])+'/'+str(ISkill[0]))
            print('LUCK: '+str(CLuck[0])+'/'+str(ILuck[0]))
        elif command == 'E': #Escape battle command (DOES NOT WORK)
            if '#' in d:
                print('****************************************************')
                (story(HP, MHP,plot_num, d, dec, '#', TempString))
                #plot_num = printStory(CHP[0], MHP, plot_num, {}, 0, TempString)#THIS TOOK SO FXING LONG TO WORK OUT
                break
            else:
                print('This battle cannot be escaped!')
        elif command == 'MAGIC': #self explanitory
            if 'Magic' in Inventory:
                if 'm' in d:
                    print('****************************************************')
                    story(HP, MHP,plot_num, d, dec, 'm', TempString)
                    #plot_num = printStory(CHP[0], MHP, plot_num, {}, 0, TempString)
                    break
                else:
                    print('You cannot use magic right now!')
            else:
                print("You don't know magic. Seriously, don't cheat!")
                    
        else:
            print('Unknown battle technique. Is that some kind of dance?')
        print('Your current health: '+str(HP))
        if MName[0] == 'Shayla' and MSkill[0] == CSkill[0] - 2:
           print("Your opponent's health: "+str((MHP[multi])+3))
        else:
            print("Your opponent's health: "+str(MHP[multi]))
        f = open('save' + str(state[0]) + '.txt', 'w') #This autosave is to ensure a person doesn't go 'Oh, I'm on 2 HP, better load up that full HP save file.'
        f.write(str(plot_num)+ '\n'+ str(CSkill[0])+'/'+str(ISkill[0])+ '\n'+ str(HP)+'/'+str(IHP[0])+ '\n'+ str(CLuck[0])+'/'+str(ILuck[0]) + '\n' + str(over[0]))
        TempString = ''
        for i in noRepeat:
            TempString += i + '/'
        f.write('\n' + TempString.rstrip('/'))
        f.write('\n-INVENTORY-\n') #autosave works here now.
        for i in Inventory:
            f.write(i)
            f.write('\n')
        f.close() #Autosave end
        if HP <= 0:
            death() #function called DEATH
            break
        elif MHP[multi] <= 0:
            MHP.remove(MHP[0])
            MText.remove(MText[0])
            MSkill.remove(MSkill[0])
            MName.remove(MName[0])
            try:
                MHP[multi] #this is to fight the next opponent
                        #multi+= 1
                print('')
                print('Your next opponent engages you!')
                print(MName[multi]+' SKILL '+str(MSkill[multi])+' HEALTH '+str(MHP[multi]))
                command = input('Action: ')
            except IndexError:
                print('')
                if plot_num == '339' or plot_num == '340':
                    print('Shayla falls back. What could she possibly be doing...?')
                else:
                    print('Your enemies fall to you.')
                CHP.append(HP)
                CHP.remove(CHP[0])
                over.append(1)
                over.remove(over[0])
                break
        else:
            command = input('Action: ')
def battle(HP, MHP, plot_num, d, dec, TempString, cont):
    #print(d)
    #d = {} #the below is to update d in a battle. This is required for some actions.
    #with open('decisions.txt','r') as decide:
        #for line in decide:
            #line=line.rstrip()
            #if line == str(int(plot_num)+1):#breaks loop when number is one more than the para number. Put in an extra just in case.
                #dec = 0
                #break
            #elif dec == 1:
                #line = line.split('/')
                #d[line[0]] = line[1] #adds the decision to dictionary
            #elif line == plot_num:
                #dec = 1 #begins to record the dictionary.
    #print(d)
    if cont == 1: #continue existing battle, or to start new one?
        del MSkill[:]
        del MText [:]
        del MHP [:]
        del MName[:]
        readMonster(0, plot_num, 1)
    if MHP[0] == 0:
        MHP.append(HP)
        MHP.remove(MHP[0])
    multi = 0 #this is to see which enemy you are fighting against currently.
            #print(MSkill)
            #print(MHP)
            #print(MText)
    f = open('save' + str(state[0]) + '.txt', 'w') #more preventation
    f.write(str(plot_num)+ '\n'+ str(CSkill[0])+'/'+str(ISkill[0])+ '\n'+ str(HP)+'/'+str(IHP[0])+ '\n'+ str(CLuck[0])+'/'+str(ILuck[0]) + '\n' + str(over[0]))
    TempString = ''
    for i in noRepeat:
        TempString += i + '/'
    f.write('\n' + TempString.rstrip('/'))
    f.write('\n-INVENTORY-\n') #autosave works here now.
    for i in Inventory:
        f.write(i)
        f.write('\n')
    f.close() #Autosave end 
    print('NOTE: Attack fights as normal. Heavy attack deals 2 extra damage, but at the')
    print('cost of 2 SKILL during battle. (You may also have other commands!)')
    command = input('Action(A to attack, H for a heavy attack): ')
    while True:
        #print(MName[multi])
        command = command.upper()
        if command == 'A':
            result = fightScene(HP, MHP[multi], 0, multi)
            if result == 0:
                print('You are evenly matched. You skillfully parry, and neither fighter gives ground.')
            elif result == 1:
                if MName[multi] == 'Boar':
                    print('You punch the boar pathetically with your fist. It loses 1 Health.')
                    MHP[multi] = MHP[multi]-1
                else:
                    if '¤Scimitar¤' in Inventory or '¤Callandor¤' in Inventory:
                        print('You wound the '+MName[multi] +'. They lose 3 Health.')
                        MHP[multi] = MHP[multi] - 3
                        if MName[0] == 'Scarecrow Doppleganger':
                            print('It feels as if you are hitting yourself! Lose 1 HEALTH.')
                            HP = HP - 1
                    else:
                        print('You wound the '+ MName[multi]+'. They lose 2 Health.')
                        MHP[multi] = MHP[multi]-2
                        if MName[0] == 'Scarecrow Doppleganger':
                            print('It feels as if you are hitting yourself! Lose 1 HEALTH.')
                            HP = HP - 1
            else:
                if 'Suitcase Blade' in Inventory:
                    roll = rollDie(d1)
                    if roll == 6:
                        print('You block the assault skillfully with the suitcase blade.')
                    else:
                        if MName[multi] == 'Ancient Mariner':
                            print(MText[multi])
                            print('Lose 3 Health.')
                            HP = HP - 3
                        elif MName[multi] == 'Jelly Slime':
                            print(MText[multi])
                            HP = HP - 1
                        elif MName[multi] == 'King Midas':
                            print(MText[multi])
                            HP = 0
                        else:
                            print(MText[multi])
                            HP = HP - 2
                elif 'Winged Helmet' in Inventory:
                    roll = rollDie(d1)
                    if roll >= 5:
                        print('The '+ MName[multi] +' hits the helmet. You only lose 1 HEALTH.')
                        HP = HP - 1
                    else:
                        if MName[multi] == 'Ancient Mariner':
                            print(MText[multi])
                            print('Lose 3 Health.')
                            HP = HP - 3
                        elif MName[multi] == 'Jelly Slime':
                            print(MText[multi])
                            HP = HP - 1
                        elif MName[multi] == 'King Midas':
                            print(MText[multi])
                            HP = 0
                        else:
                            print(MText[multi])
                            HP = HP - 2
                else:
                    if MName[multi] == 'Ancient Mariner':
                        print(MText[multi])
                        print('Lose 3 Health.')
                        HP = HP - 3
                    elif MName[multi] == 'Jelly Slime':
                        print(MText[multi])
                        HP = HP - 1
                    elif MName[multi] == 'King Midas':
                        print(MText[multi])
                        HP = 0
                    else:
                        print(MText[multi])
                        HP = HP - 2
        elif command == 'H':
            result = fightScene(HP, MHP[multi], 1, multi)
            if result == 0:
                if MName[multi] == 'Boar':
                    print('The boar had a bit of a mind blank, but STILL dodges your fist. Damn, you suck.')
                else:
                    print('You swing your weapon, and the '+MName[multi]+ ' jukes, but is too slow to strike back.')
            elif result == 1:
                if MName[multi] == 'Boar':
                    print('You unleash the power of Falcon Punch. The boar loses TWO health. Great.')
                    MHP[multi] = MHP[multi]-2
                else:
                    if '¤Scimitar¤' in Inventory or '¤Callandor¤' in Inventory:
                        print('You strike at the ' + MName[multi] + ' with a double-handed grip. They lose 5 Health.')
                        MHP[multi] = MHP[multi] - 5
                        if MName[0] == 'Scarecrow Doppleganger':
                            print('It feels as if you are hitting yourself! Lose 1 HEALTH.')
                            HP = HP - 1
                    else:
                        print('You strike the '+ MName[multi]+' with a heavy blow. They lose 4 Health.')
                        MHP[multi] = MHP[multi]-4
                        if MName[0] == 'Scarecrow Doppleganger':
                            print('It feels as if you are hitting yourself! Lose 1 HEALTH.')
                            HP = HP - 1
            else:
                if 'Suitcase Blade' in Inventory:
                    roll = rollDie(d1)
                    if roll == 6:
                        print('You block the assault skillfully with the suitcase blade.')
                    else:
                        if MName[multi] == 'Ancient Mariner':
                            print(MText[multi])
                            print('Lose 3 Health.')
                            HP = HP - 3
                        elif MName[multi] == 'Jelly Slime':
                            print(MText[multi])
                            HP = HP - 1
                        elif MName[multi] == 'King Midas':
                            print(MText[multi])
                            HP = 0
                        else:
                            print(MText[multi])
                            HP = HP - 2
                elif 'Winged Helmet' in Inventory:
                    roll = rollDie(d1)
                    if roll >= 5:
                        print('The '+ MName[multi] +' hits the helmet. You only lose 1 HEALTH.')
                        HP = HP - 1
                    else:
                        if MName[multi] == 'Ancient Mariner':
                            print(MText[multi])
                            print('Lose 3 Health.')
                            HP = HP - 3
                        elif MName[multi] == 'Jelly Slime':
                            print(MText[multi])
                            HP = HP - 1
                        elif MName[multi] == 'King Midas':
                            print(MText[multi])
                            HP = 0
                        else:
                            print(MText[multi])
                            HP = HP - 2
                else:
                    if MName[multi] == 'Ancient Mariner':
                        print(MText[multi])
                        print('Lose 3 Health.')
                        HP = HP - 3
                    elif MName[multi] == 'Jelly Slime':
                        print(MText[multi])
                        HP = HP - 1
                    elif MName[multi] == 'King Midas':
                        print(MText[multi])
                        HP = 0
                    else:
                        print(MText[multi])
                        HP = HP - 2
        elif command == 'GATORADE': #this is a stub for the hp potion things
            if 'Gatorade' in Inventory:
                HP = (IHP[0])
                print('The Gatorade grants you the will to fight on!')
                Inventory.remove('Gatorade')
            else:
                print("Despair! Play the hidden minigame, 'Where's my Gatorade?' to get more.")
        elif command == 'STAMINADE': #this is a stub for the hp potion things
            if 'Staminade' in Inventory:
                HP = (IHP[0])
                print('The Staminade regenerates health and beauty!')
                Inventory.remove('Staminade')
            else:
                print("Nope. All empty.")        
        elif command == 'STATS':
            print('These are your current stats:')
            print('SKILL: ' + str(CSkill[0])+'/'+str(ISkill[0]))
            print('LUCK: '+str(CLuck[0])+'/'+str(ILuck[0]))
        elif command == 'E': #Escape battle command
            if '#' in d:
                if plot_num == '156':
                    if 'Floater' in Inventory:
                        print('****************************************************')
                        story(HP, MHP,plot_num, d, dec, '#', TempString)
                        break
                    else:
                        print('This battle cannot be escaped!')
                else:
                    print('****************************************************')
                    story(HP, MHP,plot_num, d, dec, '#', TempString) 
                    break
            else:
                print('This battle cannot be escaped!')
        elif command == 'MAGIC': #self explanitory
            if 'Magic' in Inventory:
                if 'm' in d:
                    print('****************************************************')
                    story(HP, MHP,plot_num, d, dec, 'm', TempString)
                    break
                    #return(plot_num)
                else:
                    print('You cannot use magic right now!')
            else:
                print("You don't know magic. Seriously, don't cheat!")
                    
        else:
            print('Unknown battle technique. Is that some kind of dance?')
        print('Your current health: '+str(HP))
        if MName[multi] == 'Boar':
            print("Your opponent's health: "+str(MHP[multi]+2))
        else:
            print("Your opponent's health: "+str(MHP[multi]))
        f = open('save' + str(state[0]) + '.txt', 'w') #This autosave is to ensure a person doesn't go 'Oh, I'm on 2 HP, better load up that full HP save file.'
        f.write(str(plot_num)+ '\n'+ str(CSkill[0])+'/'+str(ISkill[0])+ '\n'+ str(HP)+'/'+str(IHP[0])+ '\n'+ str(CLuck[0])+'/'+str(ILuck[0]) + '\n' + str(over[0]))
        TempString = ''
        for i in noRepeat:
            TempString += i + '/'
        f.write('\n' + TempString.rstrip('/'))
        f.write('\n-INVENTORY-\n') #autosave works here now.
        for i in Inventory:
            f.write(i)
            f.write('\n')
        f.close() #Autosave end
        if HP <= 0:
            death() #function called DEATH
            break
        elif MHP[multi] <= 0:
            MHP.remove(MHP[0])
            MText.remove(MText[0])
            MSkill.remove(MSkill[0])
            MName.remove(MName[0])
            try:
                MHP[multi] #this is to fight the next opponent
                        #multi+= 1
                print('')
                print('Your next opponent engages you!')
                print(MName[multi]+' SKILL '+str(MSkill[multi])+' HEALTH '+str(MHP[multi]))
                command = input('Action: ')
            except IndexError:
                print('')
                if plot_num == '141':
                    print('It seems that you have made the boar angry. Prepare to be rekt.')
                else:
                    print('Your enemies fall to you.')
                CHP.append(HP)
                CHP.remove(CHP[0])
                over.append(1)
                over.remove(over[0])
                break
        else:
            command = input('Action: ')
#dice rolling, as it seems
def rollDice(roll1, roll2):
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    #print(roll1, roll2)
    return (roll1+roll2)
#dice rolling, once again.
def rollDie(roll1):
    roll1 = random.randint(1,6)
    return(roll1)
def rollD3(roll1):
    roll1 = random.randint(1,2)
    return(roll1)
#actual fighting.
def fightScene(CHP, MHP, STYLE, multi):
    print("You fight!")
    roll = rollDice(d1, d2)
    #print(roll)
    if STYLE == 0:
        if '¤Excaliber¤' in Inventory:
            if MSkill[0] > CSkill[0] + 2:
                HAttack = CSkill[0] + 3 + roll
            else:
                HAttack = CSkill[0] + 2 + roll
        elif 'Suitcase Blade' in Inventory:
            HAttack = CSkill[0] + 1 + roll
        else:
            HAttack = CSkill[0] + roll
    else:
        if '¤Excaliber¤' in Inventory:
            if MSkill[0] > CSkill[0] + 2:
                HAttack = CSkill[0] + 1 + roll
            else:
                HAttack = CSkill[0] + roll
        elif 'Suitcase Blade' in Inventory:
            HAttack = CSkill[0] - 1 + roll
        else:
            HAttack = CSkill[0] + roll - 2
    #print(roll)
    #print(HAttack)
    if MName[0] == 'Night Beholder':
        roll = rollDice(d1, d2)
        MAttack = MSkill[multi] + roll
        roll = rollDice(d1,d2)
        MAttack+= roll
        #print(MAttack) #PRINTING
    else:
        roll = rollDice(d1, d2)
        MAttack = MSkill[multi] + roll
    if HAttack > MAttack:
        return 1
    elif HAttack == MAttack:
        return 0
    else:
        return 2
#reads in the monster stats from a text document.
def readMonster(read, plot_num, count):
    with open("monsters.txt", "r") as monster:
        for line in monster:
            #print(count)
            line = line.rstrip()
            if read == 1:
                if str(line).isnumeric():
                    count = 0
                    break
                elif (str(count/2))[-2:] == '.0':
                    MText.append(line)
                    count += 1
                else:
                    line = line.split('/')
                        #print(line)
                    MName.append(line[0])
                    MSkill.append(int(line[1]))
                    MHP.append(int(line[2]))
                    count += 1
            elif line == str(plot_num):
                read = 1
        if MName[0] == 'Weetbix':
            del MText [:]
            MText.append('Weetbix breathes a jet of flames! Lose 2 HEALTH.')
            MText.append('Weetbix slashes at you with its claws. You lose 2 HEALTH.')
            MText.append('Weetbix sweeps at your legs with its tail. Lose 2 HEALTH.')
        elif MName[0] == 'Skeleton Weetbix':
            MText.append('Weetbix swipes at you with its skeletal tail. Lose 2 HEALTH.')
            MText.append('Weetbix smashes its head at you. You block, but still lose 2 HEALTH.')
        elif MName[0] == 'Shayla':
            MText.append('Shayla strikes in a pattern you have never seen before. Lose 4 HEALTH.')
            MText.append('Shayla plunges a knife into your arm. Lose 4 HEALTH.')
            MText.append('Shayla seems to speed up suddenly, and you feel a nick on your torso. Lose 4 HP.')
#story telling.
def story(HP, MHP,plot_num, d, dec, plot_c, TempString):
    for i in d: #then find the corresponding paragraph
        if i == plot_c:
            plot_num = d[i] #and go to it
            d = {} #the below is to update d in a battle. This is required for some actions.
            with open('decisions.txt','r') as decide: #THIS ONE IS THE CORRECT ONE.
                for line in decide:
                    line=line.rstrip()
                    if line == str(int(plot_num)+1):#breaks loop when number is one more than the para number. Put in an extra just in case.
                        dec = 0
                        break
                    elif dec == 1:
                        line = line.split('/')
                        d[line[0]] = line[1] #adds the decision to dictionary
                    elif line == plot_num:
                        dec = 1 #begins to record the dictionary.
            #print(d) #PRINTINGGGGGGG
            #This part is slow: 1 paragraph earlier. Can become useful.
            with open("story" + str(plot_num) + ".txt", "r") as story:
                for line in story:
                    if line.startswith('+'):
                        Inventory.append((line.rstrip())[1:]) #adds the corresponding item to the inventory.
                    elif line.startswith('-'):
                                #print((line.strip())[1:])
                        if ((line.strip())[1:]) in Inventory:
                            Inventory.remove((line.rstrip())[1:]) #deletes items from the inventory.
                    elif line.startswith('@'): #checking if line should be printed
                        require = (line.rstrip())[1:line.index('&')]
                        #print(tList[0]) #Checking 123
                        #print(tItem) #Checking 123
                        if require == 'Deathnote': #this is for the deathnote combo pack.
                            if 'Death Note' in Inventory and 'Pen' in Inventory:
                                print((line.strip())[line.index('&') + 2:])
                            else:
                                pass
                        else:
                            if require in Inventory:
                                print((line.strip())[line.index('&') + 2:])
                            else:
                                pass
                    elif line.startswith('~'):
                        CSkill.append(CSkill[0] + int((line.rstrip())[1]))
                        CSkill.remove(CSkill[0])
                    elif line.startswith('^'):
                        CSkill.append(CSkill[0] + int((line.rstrip())[1]))
                        CSkill.remove(CSkill[0])
                        ISkill.append(ISkill[0] +int((line.rstrip())[1]))
                        ISkill.remove(ISkill[0])
                    elif line.startswith('`'): #this is only on spaceship AND for the holy smite spell. SPOILERS
                        noRepeat.append((line.rstrip())[1:])#that key is the one under the ESC key.
                    elif line.startswith('>'): #LOSING STATS
                        stat = line[1]
                        if stat == 'H':
                            CHP.append(CHP[0]-int((line.rstrip())[3:]))
                            CHP.remove(CHP[0])
                            if CHP[0]<1:
                                death()
                        elif stat == 'L':
                            if CLuck[0]-int((line.rstrip())[3:]) < 1:
                                CLuck.append(1)
                                CLuck.remove(CLuck[0])
                            else:
                                CLuck.append(CLuck[0]-int((line.rstrip())[3:]))
                                CLuck.remove(CLuck[0])
                        elif stat == 'S':
                            if CSkill[0]-int((line.rstrip())[3:]) < 1:
                                CSkill.append(1)
                                CSkill.remove(CSkill[0])
                            else:
                                CSkill.append(CSkill[0]-int((line.rstrip())[3:]))
                                CSkill.remove(CSkill[0])
                        elif stat == 'M': #TEST THIS
                            MHP.append(MHP[0] - int((line.rstrip())[3:]))
                            MHP.remove(MHP[0])
                        elif stat == 'K':
                            MSkill.append(MSkill[0] - int((line.rstrip())[3:]))
                            MSkill.remove(MSkill[0])
                    elif line.startswith('%'): #losing HP from spells. Need separate exert due to some things.
                        if 'Staff' in Inventory: #notice no need to type H
                            if int((line.rstrip()[2:])) - 3 < 1:
                                CHP.append(CHP[0] - 1)
                                CHP.remove(CHP[0])
                            else:
                                CHP.append(CHP[0] - (int((line.rstrip()[2:])) - 3))
                                CHP.remove(CHP[0])
                        elif '¤Callandor¤' in Inventory:
                            if int((line.rstrip()[2:])) - 3 < 1:
                                pass #NO LOSS OF HP WOOHOO
                            else:
                                CHP.append(CHP[0] - (int((line.rstrip()[2:])) - 3))
                                CHP.remove(CHP[0])
                        else:
                            CHP.append(CHP[0]-int((line.rstrip()[3:])))
                            CHP.remove(CHP[0])
                        if CHP[0]<1:
                            death()
                        #else:
                            #CHP.append(CHP[0]-int((line.rstrip()[3:])))
                            #CHP.remove(CHP[0])
                    elif line.startswith('<'): #GAINING STATS
                        stat = line[1]
                        if stat == 'H':
                            if CHP[0]+int((line.rstrip())[3:]) > IHP[0]:
                                CHP.append(IHP[0])
                                CHP.remove(CHP[0])
                            else:
                                if 'Ring of Healing' in Inventory:
                                    if CHP[0]+int((line.rstrip())[3:]) + 1 > IHP[0]:
                                        CHP.append(IHP[0])
                                        CHP.remove(CHP[0])
                                    else:
                                        CHP.append(CHP[0]+1+int((line.rstrip())[3:]))
                                        CHP.remove(CHP[0])
                                else:
                                    CHP.append(CHP[0]+int((line.rstrip())[3:]))
                                    CHP.remove(CHP[0])
                        elif stat == 'L':
                            if CLuck[0]+int((line.rstrip())[3:]) > ILuck[0]:
                                CLuck.append(ILuck[0])
                                CLuck.remove(CLuck[0])
                            else:
                                CLuck.append(CLuck[0]+int((line.rstrip())[3:]))
                                CLuck.remove(CLuck[0])
                        elif stat == 'S':
                            if CSkill[0]+int((line.rstrip())[3:]) > ISkill[0]:
                                CSkill.append(ISkill[0])
                                CSkill.remove(CSkill[0])
                            else:
                                CSkill.append(CSkill[0]+int((line.rstrip())[3:]))
                                CSkill.remove(CSkill[0])
                        elif stat == 'M':
                            MHP.append(MHP[0] + int((line.rstrip())[3:]))
                            MHP.remove(MHP[0])
                    else:
                        if '}' in line:
                            line = line.replace('}',str(int(CSkill[0] - 2)))
                        elif ']' in line:
                            line = line.replace(']','『　　』')
                        elif '[' in line:
                            line = line.replace('[',str(CHP[0]))
                        elif '{' in line:
                            line = line.replace('{',str(int(CSkill[0] + 2)))
                        elif '†' in line:
                            line = line.replace('†', str(int(CSkill[0])))
                        elif '‡' in line:
                            line = line.replace('‡', str(int(CSkill[0] + 6)))
                        elif 'Š' in line:
                            line = line.replace('Š', str(int(CSkill[0] - 4)))
                        print(line.strip())
            HP = CHP[0]
            if line.endswith("**BATTLE**"):
                over.append(0)
                over.remove(over[0])
                battle(HP, MHP, plot_num, d, dec, TempString, 1)
            elif line.endswith('**CONTINUE**'): #the battle continues after
                if MHP[0] < 1:
                    over.append(1)
                    over.remove(over[0])
                    print('The creature falls to your mighty magic.')
                    MHP.remove(MHP[0])
                    MText.remove(MText[0])
                    MSkill.remove(MSkill[0])
                    MName.remove(MName[0])
                else:
                    over.append(0) #failed commands or something.
                    over.remove(over[0])
                    battle(CHP[0], MHP, plot_num, d, dec, TempString, 0)
            elif line.endswith('¤¤ BOSS BATTLE ¤¤'):
                over.append(0)
                over.remove(over[0])
                bossBattle(HP, MHP, plot_num, d, dec, TempString, 1, 0)
            elif line.endswith('¤¤ CONTINUE ¤¤'): #the battle continues after
                if MHP[0] < 1:
                    over.append(1)
                    over.remove(over[0])
                    print('The creature falls to your mighty magic.')
                    MHP.remove(MHP[0])
                    MText.remove(MText[0])
                    MSkill.remove(MSkill[0])
                    MName.remove(MName[0])
                else:
                    over.append(0) #failed commands or something.
                    over.remove(over[0])
                    bossBattle(CHP[0], MHP, plot_num, d, dec, TempString, 0, 0)
            elif line.endswith("**DEATH**"):
                death()
            elif line.endswith('**THE END?**'):
                end('bad')
            elif line.endswith('**THE END.**'):
                end('normal')
            elif line.endswith('¤¤THE END...?¤¤'):
                end('evil')
            elif line.endswith('¤¤FINIT.¤¤'):
                end('good')
            while True:
                printStory(HP, MHP,plot_num, d, dec, TempString) #Works now. Maybe. TEST FOR LAG. #basically all that is edited, so yeah.
            #return(plot_num)
    
#prints the story. Fixed for now.    
def printStory(HP, MHP,plot_num, d, dec, TempString):
    #print(plot_num)
    Para.append(plot_num)
    Para.remove(Para[0])
    f = open('save' + str(state[0]) + '.txt', 'w') #Autosave
    f.write(str(Para[0])+ '\n'+ str(CSkill[0])+'/'+str(ISkill[0])+ '\n'+ str(CHP[0])+'/'+str(IHP[0])+ '\n'+ str(CLuck[0])+'/'+str(ILuck[0]) + '\n' + str(over[0]))
    TempString = ''
    for i in noRepeat:
        TempString += i + '/'
    #print(TempString)
    f.write('\n' + TempString.rstrip('/'))
    f.write('\n-INVENTORY-\n')
    for i in Inventory:
        f.write(i)
        f.write('\n')
    f.close() #Autosave end
    with open('decisions.txt','r') as decide:
        for line in decide:
            line=line.rstrip()
            if line == str(int(plot_num)+1):#breaks loop when number is one more than the para number. Put in an extra just in case.
                dec = 0
                break
            elif dec == 1:
                line = line.split('/')
                d[line[0]] = line[1] #adds the decision to dictionary
            elif line == plot_num:
                dec = 1 #begins to record the dictionary.
    #print(Para)
    #print(d) 
    plot_c = plotChoice() #plot_c is a choice in the text document thing. Sorry to editors.
    #d= {}
    #dec = 0
    #with open('decisions.txt','r') as decide:
        #for line in decide:
            #line=line.rstrip()
            #if line == str(int(plot_num)+1):#breaks loop when number is one more than the para number. Put in an extra just in case.
                #dec = 0
                #break
            #elif dec == 1:
                #line = line.split('/')
                #d[line[0]] = line[1] #adds the decision to dictionary
            #elif line == plot_num:
                #dec = 1 #begins to record the dictionary.
    #print(d)
    #print(Para)
    if plot_c.isdigit():
        if plot_c in d: #if the number that is typed corresponds with option
            plot_num = story(HP, MHP,plot_num, d, dec, plot_c, TempString) #'plot_num = story': This part is so the Paragraph number still auto updates after edits.
            return(plot_num)
        else:
            if 'p' in d:
                plot_num = story(HP, MHP,plot_num, d, dec, 'u', TempString) 
                return(plot_num)
            else:
                print('This value cannot be found. Enter a valid number, or follow instructions.')
                return(plot_num)
    else:
        plot_c = plot_c.upper()
        if plot_c == 'INVENTORY':
            print('These items are currently in your inventory: ')
            for i in Inventory:
                print(i)
        elif plot_c == 'STATS':
            print('These are your current stats:')
            print('SKILL: ' + str(CSkill[0])+'/'+str(ISkill[0]))
            print('HEALTH: '+str(CHP[0]) + '/' +str(IHP[0]))
            print('LUCK: '+str(CLuck[0])+'/'+str(ILuck[0]))
        elif plot_c == 'BOOZE': 
            if 'Booze' in Inventory:
                if 'Ring of Healing' in Inventory:
                    if CHP[0] + 5 > IHP[0]:
                        CHP.append(IHP[0])
                        CHP.remove(CHP[0])
                    else:
                        CHP.append(CHP[0]+5)
                        CHP.remove(CHP[0])
                else:
                    if CHP[0] + 4 > IHP[0]:
                        CHP.append(IHP[0])
                        CHP.remove(CHP[0])
                    else:
                        CHP.append(CHP[0] + 4)
                        CHP.remove(CHP[0])
                Inventory.remove('Booze')
                print('You drink the booze, and regain health.')
                print('Current HEALTH: ' + str(CHP[0]))
            else:
                print("You don't have any booze to drink, you fool!")
        elif plot_c == 'EAT': 
            if 'Provision' in Inventory:
                if 'Ring of Healing' in Inventory:
                    if CHP[0] + 5 > IHP[0]:
                        CHP.append(IHP[0])
                        CHP.remove(CHP[0])
                    else:
                        CHP.append(CHP[0]+5)
                        CHP.remove(CHP[0])
                else:
                    if CHP[0] + 4 > IHP[0]:
                        CHP.append(IHP[0])
                        CHP.remove(CHP[0])
                    else:
                        CHP.append(CHP[0] + 4)
                        CHP.remove(CHP[0])
                Inventory.remove('Provision')
                print('You eat the food, and feel stronger.')
                print('Current HEALTH: ' + str(CHP[0]))
            else:
                print("Your stomach rumbles in hunger. You don't have any food!")
        elif plot_c == 'ALD':
            if 'Liquid' in Inventory:
                ILuck.append(ILuck[0] + 1)
                ILuck.remove(ILuck[0])
                CLuck.append(ILuck[0])
                CLuck.remove(CLuck[0])
                print('You drink the mysterious liquid, and feel a surge of luck. Your INITIAL LUCK is')
                print("increased by 1, and your current LUCK is increased to this value!")
                Inventory.remove('Liquid')
            else:
                print('Lol, what is ALD?')
        elif plot_c == 'GATORADE':
            if 'Gatorade' in Inventory:
                CHP.append(IHP[0])
                CHP.remove(CHP[0])
                print('The Gatorade grants you the will to fight on!')
                Inventory.remove('Gatorade')
            else:
                print("Despair! Play the hidden minigame, 'Where's my Gatorade?' to get more.")
        elif plot_c == 'STAMINADE':
            if 'Staminade' in Inventory:
                CHP.append(IHP[0])
                CHP.remove(CHP[0])
                print('The Staminade regenerates health and beauty!')
                Inventory.remove('Staminade')
            else:
                print("Nope. All empty.")    
        elif plot_c == '':
            #print(d)
            if 'l' in d: #LUCK test
                #print('Yep, luck testing!')
                roll = rollDice(d1,d2)
                #print(roll) #checking 123
                if CLuck[0] == 1:
                    plot_num = story(HP, MHP,plot_num, d, dec, 'u', TempString)
                    return(plot_num)
                else:
                    CLuck.append(CLuck[0] -1)
                    CLuck.remove(CLuck[0])
                    if roll > (CLuck[0]+1): #ensures that it is current luck testing against, not current luck + 1
                        plot_num = story(HP, MHP,plot_num, d, dec, 'u', TempString)
                        return(plot_num)
                    else:
                        plot_num = story(HP, MHP,plot_num, d, dec, 'l', TempString)
                        return(plot_num)
            elif 's' in d: #SKILL test
                roll = rollDice(d1,d2)
                #print(roll)
                #print(CSkill[0])
                if '?' in d: #this is used ONCE in the god damn story. ONCE.
                    if roll == 12:
                        plot_num = story(HP, MHP,plot_num, d, dec, '?', TempString)
                        return(plot_num)
                    elif roll > (CSkill[0]):
                        plot_num = story(HP, MHP,plot_num, d, dec, 'u', TempString)
                        return(plot_num)
                    else:
                        plot_num = story(HP, MHP,plot_num, d, dec, 's', TempString)
                        return(plot_num)
                elif '¤' in d:
                    if '¤Callandor¤' in Inventory:
                        plot_num = story(HP, MHP,plot_num, d, dec, '¤', TempString)
                        return(plot_num)
                    else:
                        if roll > (CSkill[0]):
                            plot_num = story(HP, MHP,plot_num, d, dec, 'u', TempString)
                            return(plot_num)
                        else:
                            plot_num = story(HP, MHP,plot_num, d, dec, 's', TempString)
                            return(plot_num)
                else:
                    if roll > (CSkill[0]):
                        plot_num = story(HP, MHP,plot_num, d, dec, 'u', TempString)
                        return(plot_num)
                    else:
                        plot_num = story(HP, MHP,plot_num, d, dec, 's', TempString)
                        return(plot_num)
            elif '`' in d:
                if Para[0] in noRepeat:
                    plot_num = story(HP, MHP,plot_num, d, dec, '`', TempString)
                    return(plot_num)
                else:
                    plot_num = story(HP, MHP,plot_num, d, dec, 'u', TempString)
                    return(plot_num)
            elif '|' in d:
                if '¤Excaliber¤' in Inventory and 'Magic' in Inventory and 'Death Note' in Inventory:
                    plot_num = story(HP, MHP,plot_num, d, dec, '|', TempString)
                    return(plot_num)
                else:
                    plot_num = story(HP, MHP,plot_num, d, dec, 'u', TempString)
                    return(plot_num)
            elif 'D' in d:
                if 'Death Note' in Inventory and 'Pen' in Inventory:
                    plot_num = story(HP, MHP,plot_num, d, dec, 'D', TempString)
                    return(plot_num)
                else:
                    plot_num = story(HP, MHP,plot_num, d, dec, 'u', TempString)
                    return(plot_num)
            elif 'O' in d:
                if 'Osiris Sight' in Inventory:
                    plot_num = story(HP, MHP,plot_num, d, dec, 'O', TempString)
                    return(plot_num)
                else:
                    plot_num = story(HP, MHP,plot_num, d, dec, 'u', TempString)
                    return(plot_num)
            elif 'v' in d:
                if "Mariner's Crossbow" in Inventory:
                    plot_num = story(HP, MHP,plot_num, d, dec, 'v', TempString) #the 'x' is shifting plot_c to the 'story' function. SO COMPLICATED.
                    return(plot_num)
                else:
                    plot_num = story(HP, MHP,plot_num, d, dec, 'u', TempString)
                    return(plot_num)
            elif 'C' in d:
                if '¤Callandor¤' in Inventory:
                    plot_num = story(HP, MHP,plot_num, d, dec, 'C', TempString) #the 'x' is shifting plot_c to the 'story' function. SO COMPLICATED.
                    return(plot_num)
                else:
                    plot_num = story(HP, MHP,plot_num, d, dec, 'u', TempString)
                    return(plot_num)
            elif 'x' in d: #meant to be the continue by pressing space option. SUDDENLY WORKS!
                plot_num = story(HP, MHP,plot_num, d, dec, 'x', TempString) #the 'x' is shifting plot_c to the 'story' function. SO COMPLICATED.
                return(plot_num)   
            else:
                print("Spamming Enter here doesn't get you anywhere, you know.")
        else:
            if 'p' in d: #password part
                if plot_c == 'ALOHA SNACKBAR':
                    plot_num = story(HP, MHP,plot_num, d, dec, 'p', TempString)
                    return(plot_num)
                else:
                    plot_num = story(HP, MHP,plot_num, d, dec, 'u', TempString)
                    return(plot_num)
            else:
                print('That command is unknown.')
            
        return(plot_num)

# plotChoice is a function called by printStory, which simply asks, "what do you do?" and passes the value of the input back to printStory,
#A NORMAL TRANSITION TO THE NEXT SCENE
def plotChoice():
    plot_c = input("Command: ")
    print('****************************************************') #NEW
    return plot_c

# Starts the game's first scene, prints first scene text, then goes to printStory
def initPlot(l, d, TempString): #sorry about the meaningful names HMMHMM 'l'
    print("¤¤ DORAU ¤¤") #THE TITLE. op.
    print('****************************************************') # this is all hard coded intro here. Change it if you want for a different game.
    print('Story stolen from many sources by Wesley Yu.')
    print('The original parts also by the same guy.')
    print('Program by Sean Zhang and Wesley Yu.')
    print('Additional help of varying degree by: John Tian, William Weber,')
    print('various internet users and Wikipedia.')
    print('Special mentions to Ram and Rex, for lots of hacking stuff.')
    print('Thanks, you two. For making it Mac compat.')
    print("Inspired by the 'Fighting Fantasy' game books by Steve Jackson")
    print('and Ian Livingstone.')
    print('NOTE: This game is designed for fun. It is not to be marketed.')
    print('Who would buy this garbage anyways?')
    print('****************************************************')
    print('NOTE: THIS GAME IS IN ALPHA 1.0')
    print("THERE IS THE POSSIBILITY OF SEVERE LAG.")
    print('IF LAGGING, CLOSE THE GAME AND OPEN IT AGAIN.')
    print('IF THERE ARE PROBLEMS WHILE PLAYING THE GAME, PLEASE NOTIFY THE DEVELOPERS.')
    print('****************************************************')
    warn()
    stuck = 0
    while stuck == 0:
        print('Before we begin the game, will you be starting from Scratch or')
        choice = input('loading an existing game? (1 to Start New Game, 2 to Load.) ')
        if choice == '2':
            print('What existing state do you wish to load? (only type the part')
            statE = input('after state.) ')
            state.append(statE)
            state.remove(state[0])
            counter = 1
            with open('save' + str(statE) + '.txt') as f:
                for line in f:
                    line = line.rstrip()
                    if line == 'You have died.':
                        print('You have unfortunately died already.')
                        print('Please load an unfinished game or create a new one.') #seriously, don't screw with the save file guys. Really.
                        stuck = 0
                    elif line == "You have achieved the 'end.'":
                        print('This adventure has ended, but...')
                        print('This time, go for the path of a hero!')
                        stuck = 0
                    elif line == "You have achieved the end.":
                        print('This adventure has ended, but...')
                        print("Don't you wish that Shayla could have lived?")
                        stuck = 0
                    elif line == 'This may be the end.':
                        print('Taking over the world is great, but...')
                        print('Is this really what you wanted?')
                        stuck = 0
                    elif line == "This is the end.":
                        print('Congragulations for completion!')
                        print('But do you want to relive the adventure again?')
                        stuck = 0
                    else:
                        if counter == 1:
                            Para.append(int(line))
                            Para.remove(Para[0])
                        if counter == 2:
                            line = line.split('/')
            
                            CSkill.append(int(line[0]))
                            ISkill.append(int(line[1]))
                            #CSkill.remove(CSkill[0]) these are no longer needed
                            #ISkill.remove(ISkill[0])
               
                        if counter == 3:
                            line = line.split('/')
                            CHP.append(int(line[0]))
                            IHP.append(int(line[1]))
                            #CHP.remove(CHP[0])
                            #IHP.remove(IHP[0])
              
                        if counter == 4:
                            line = line.split('/')
                            CLuck.append(int(line[0]))
                            ILuck.append(int(line[1]))
                            #CLuck.remove(CLuck[0])
                            #ILuck.remove(ILuck[0])

                        if counter == 5:
                            over.append(int(line))
                            over.remove(over[0])
                            del Inventory[:] #cheating a little bit here, but meh.

                        if counter == 6: #to add this just for the spaceship...
                            line = line.split('/')
                            for i in line:
                                noRepeat.append(i)
                            for i in noRepeat:
                                if i =='':
                                    noRepeat.remove(noRepeat[noRepeat.index('')])
                            
                        if counter > 7:
                            Inventory.append(line)
                #counter += 1
                        counter += 1
                        stuck = 1
            if stuck == 1:  
                print('The state has been loaded.')
                print('The current stats are:')
                print('SKILL: ' + str(CSkill[0])+'/'+str(ISkill[0]))
                print('HEALTH: '+str(CHP[0]) + '/' +str(IHP[0]))
                print('LUCK: '+str(CLuck[0])+'/'+str(ILuck[0]))
                print('****************************************************')

        elif choice == '1':
            print('NOTE: You are beginning a NEW GAME and EXISTING DATA WILL BE WIPED.')
            print('Before we begin the game, what save state will you save this on? ')
            statE = input('(Please choose from a viable state slot of 1, 2 or 3.) ')
            #print(statE)
            if statE == '1' or statE == '2' or statE == '3':
                state.append(statE)
                state.remove(state[0])
                print('Your adventure is now autosaving on state ' + state[0] + '.')
                print('All previous saves on that state will be removed.')
                with open('save' + str(statE) + '.txt') as f:
                    for line in f:
                        line = line.rstrip()
                        if line == "You have achieved the 'end.'":
                            print('****************************************************')
                            print('Trying again?')
                            print('This time, go for the path of a hero!')
                        elif line == "You have achieved the end.":
                            print('****************************************************')
                            print("Changing history?")
                            print("Is it because of a certain individual?")
                        elif line == "This may be the end.":
                            print('****************************************************')
                            print("So that wasn't what you wanted.")
                            print('Maybe... this time?')
                        elif line == "This is the end.":
                            print('****************************************************')
                            print('You have achieved happily ever after.')
                            print('Yet you will continue to change it?')
                print('****************************************************')
                sr = rollD3(d1)
                hr = rollDice(d1, d2)
                lr = rollDie(d1)
                ISkill.append(9+ sr) #random generation of stat points.
                IHP.append(12+ hr)
                ILuck.append(6+ lr)
                CSkill.append(ISkill[0])
                CHP.append(IHP[0])
                CLuck.append(ILuck[0]) #This is all randomly generated stats.
                stuck = 1
            else:
                print()
                print('That is not a valid state. Please choose from 1, 2 or 3.')
                print()
                stuck = 0
        else:
            print()
            print('Choice is not valid. Seriously, we could be here all day.')
            print()
            stuck = 0
    plot_num = str(Para[0])
    if plot_num.isdigit():
        with open('decisions.txt','r') as decide:
            for line in decide:
                line=line.rstrip()
                if line == str(int(plot_num)+1):#breaks loop when number is one more than the para number. Put in an extra just in case.
                    l = 0
                    break
                elif l == 1:
                    line = line.split('/')
                    d[line[0]] = line[1] #adds the decision to dictionary
                elif line == plot_num:
                    l = 1 #begins to record the dictionary.
        with open("story" + plot_num + ".txt", "r") as story:
            for line in story:
                if line.startswith('+'):
                    pass
                elif line.startswith('-'):
                    pass
                elif line.startswith('@'):
                    require = (line.rstrip())[1:line.index('&')]
                    if require == 'Deathnote':
                        if 'Death Note' in Inventory and 'Pen' in Inventory:
                            print((line.strip())[line.index('&') + 2:])
                        else:
                            pass
                    else:
                        if require in Inventory:
                            print((line.strip())[line.index('&') + 2:])
                        else:
                            pass
                    #else:
                        #pass
                elif line.startswith('>'):
                    pass
                elif line.startswith('<'):
                    pass
                elif line.startswith('`'):
                    pass
                elif line.startswith('~'):
                    pass
                elif line.startswith('^'):
                    pass
                elif line.startswith('%'):
                    pass
                else:
                    if '}' in line:
                        line = line.replace('}',str(int(CSkill[0] - 2)))
                    elif ']' in line:
                        line = line.replace(']','『　　』')
                    elif '[' in line:
                        line = line.replace('[',str(CHP[0]))
                    elif '{' in line:
                        line = line.replace('{',str(int(CSkill[0] + 2)))
                    elif '†' in line:
                        line = line.replace('†', str(int(CSkill[0])))
                    elif '‡' in line:
                        line = line.replace('‡', str(int(CSkill[0] + 6)))
                    elif 'Š' in line:
                        line = line.replace('Š', str(int(CSkill[0] - 4)))
                    print(line.strip())
        if over[0] == 0:
            if line.endswith("**BATTLE**"): 
                battle(CHP[0], MHP, plot_num, d, l, TempString, 1)
            elif line.endswith('**CONTINUE**'):
                battle(CHP[0], MHP, plot_num, d, l, TempString, 1)
            elif line.endswith('¤¤ BOSS BATTLE ¤¤'):
                bossBattle(CHP[0], MHP, plot_num, d, l, TempString, 1, 0)
            elif line.endswith('¤¤ CONTINUE ¤¤'):
                bossBattle(CHP[0], MHP, plot_num, d, l, TempString, 1, 0)
            elif line.endswith('**THE END?**'):
                end('bad')
        elif over[0] == 1:
            if line.endswith ('**BATTLE**'):
                print('The threat has been neutralised. Continue on your mission!')
            elif line.endswith('**CONTINUE**'):
                print('The threat has been neutralised. Continue on your mission!')
            elif line.endswith('¤¤ BOSS BATTLE ¤¤'):
                print('The threat has been neutralised. Continue on your mission!')
            elif line.endswith('¤¤ CONTINUE ¤¤'):
                print('The threat has been neutralised. Continue on your mission!')
            elif line.endswith('**THE END?**'):
                end('bad')
            elif line.endswith('**THE END.**'):
                end('normal')
            elif line.endswith('¤¤THE END...?¤¤'):
                end('evil')
            elif line.endswith('¤¤FINIT.¤¤'):
                end('good')
    #printStory(HP, MP, '0')
    #else:
        #if plot_num == 'BOOZE':
                #print('So far so good!')

    while True:
            plot_num = printStory(CHP[0], MHP, plot_num, {}, 0, TempString)
        #else:
            #if plot_num == 'BOOZE':
               # print('So far so good!')
            
            

# STARTS THE GAME!!!!!!
initPlot(0, {}, '')
