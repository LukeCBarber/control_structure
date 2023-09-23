
#intro
print("SURVIVE DRACULA'S CASTLE")
print()
print("""Lightning cracks the sky. Rain splashes the earth. Ascending a hillside, you look down a cobblestone road. Before you, a castle stands perched on the adjacent hillside. The Romanian countryside is scarcely inhabited, and you must find shelter from the storm. You follow the road. It leads to a wooden door, 15 feet in height.""")
print()
dec1 = input("""Would you like to knock on the door or walk around the perimeter of the castle? (knock, go around,):""")
if dec1 == 'knock':
    print()
    print("""You approach the door, but as you are about to knock, it swings open abruptly. A gust of cold air pours out of the castle. You are unnerved, but in need of shelter for the night.You enter the castle. Dim and silent, the entrance feels eerie, but you continue on to a spiral staircase. It winds through the back of the entrance hall up through the house, and to a lower level as well.""")
    print()
    doordec = input("""Would you like to go up or down? (up/down):""")
    print()
    if doordec == 'up':
        print("""You ascend the spiral staircase to the second floor. As you turn to look down a long corridor lined on either side with candles. A shadow at the end of the hall. “HELLO” you yell out. There is no response. The shadow vanishes.""")
        print()
        doorupdec = input("""Would you like to investigate the shadow or turn around? (investigate/turn around): """)
        print()
        if doorupdec == 'investigate':
            print("""You creep slowly towards the spot where the shadow was. Around a corner, you notice a single doorway slightly ajar and a low glow of light. Peeking through the door, you see what looks to be a bedroom with no bed. A single coffin sits in the middle of the room, wide open. As you push on the door to enter, you feel a cold hand on your shoulder. Everything goes black.""")
            print()
            print('YOU DIED')
            #ending1
        elif doorupdec == 'turn around':
            print("""Something feels wrong. You turn to run, but something stops you. Behind you stands a man, 6 feet tall. He has the paleness of a dead man. Not moving, not breathing, he stands for a moment in front of you. Lifting his head, he begins to smile revealing a set of large fangs. You try to scream, but before the noise can leave your vocal chords, he pounces on you.""")
            print()
            print('YOU DIED')
            #ending2
    elif doordec == 'down':
        print("""Descending the stairs, the little light that leaked into the entrance hall fades. The stairs seem to wind lower and lower with no doors or entrances to a basement floor. Finally, you reach the bottom of the stone spiral staircase. Suddenly, fire flares up from two wall mounted torches as if lit by some invisible force. They illuminate a small door. Before you can wonder how, you hear a large thud echo from above.""")
        print()
        doordowndec = input("""Would you like to go through the mysterious door or investigate the sound upstairs? (door/investigate): """)
        print()
        if doordowndec == 'door':
            print("""You approach the door apprehensively. Slowly pushing the door open, you enter a small room. A small torch mounted on the opposing wall. Below it a closed casket sits empty, save for a mounted crest above it. A small bat, a large D, surrounded by four small crowns. Suddenly, the door slams shut behind you. You are trapped.""")
            print()
            print('YOU DIED')
            #ending3
        elif doordowndec == 'investigate':
            print("""You turn back and run up the stairs. It's a lot easier to see the stairs in the dim lighting of the torches. You keep running and running. Was the staircase this long on the way down? Suddenly you feel a push. Slipping off of the stairs you begin to fall faster and faster. You hit the bottom of the staircase with a loud thud.""")
            print()
            print('YOU DIED')
            #ending4
elif dec1 == 'go around':
    print()
    print("""The door looks too heavy to open and something feels off about this place. You decide to pace alongside the castle wall. The stone wall is high and climbing over is not an option. You continue to pace. Just as you are about to give up and head to the main entrance, you spot a light. A second floor window, and it's open. You could try to climb in.""")
    print()
    arounddec = input("""Would you like to climb to the window or head back to the main entrance? (climb/go back): """)
    if arounddec == 'climb':
        print("""You begin climbing the wall. The stone is slippery and the wind makes it hard to see. You are only a few feet from the window when you begin to slip. A fall from this height won’t kill you, but it will definitely hurt.""")
        print()
        aroundclimb = input("""Would you like to continue climbing or try to make your way down? (up/down): """)
        print()
        if aroundclimb == 'up':
            print("""Recovering your grip, you finally make it to the window. Pulling you face up you peer into an empty bedroom. Suddenly, a figure opens the door. You lock eyes with a horrifying creature. A walking corpse, his face looks like it has died a long time ago. Frightened you try to let go of the ledge, but he grabs your arms. With superhuman strength he pulls you into the castle. The lights go out.""")
            print()
            print('YOU DIED')
            #ending5
        elif aroundclimb == 'down':
            print("""You climb down and decide to make your way back. The storm is draining your energy and you begin to tire of walking. Finally, you stumble to the entrance of the castle only to find that the door is now open. A gust of frigid air rushes out of the castle and with it a whisper. “Rrruunn saavee yyyouuurrsseellfff. Tthhheerreee isss nooo ssshhheellttteerrr heeerrreee”. You turn and run into the forest.""")
            print()
            print('YOU LIVE!')
            #ending6
    elif arounddec == 'go back':
        print("""You approach the door, but as you are about to knock, it swings open abruptly. A gust of cold air pours out of the castle. You are unnerved, but in need of shelter for the night.You enter the castle. Dim and silent, the entrance feels eerie. You hear the sound of soft music echoing through the halls. It sounds pleasant, like a lullaby. You can follow the source of the sound or look elsewhere for somewhere to sleep.""")
        print()
        gobackdec = input("""Would you like to follow the music or keep looking for somewhere to sleep? (music/keep looking): """)
        if gobackdec == 'music':
            print("""Following the music, you are led to the end of the hall. It seems to be coming from upstairs. You climb a large spiral staircase and arrive at a long hallway. As you enter the hallway, the music suddenly stops. You hear another noise. Crying, like the cries of an infant. You spot a door at the end of the hall. This must be where the sound is coming from. As you are about to open the door you feel a cold breath over your shoulder. “You woke the baby” a lower muted voice says behind you. You feel a large thud on the back of your head and everything goes black.""")
            print()
            print('YOU DIED')
            #ending7
        elif gobackdec == 'keep looking':
            print()
            print("""You decide to ignore the lullaby. Whoever lives here wouldn’t want you to bother them at this hour. It’s probably best to  stay quiet and try to find an empty room to sleep in. While you are at it you might as well look around for anything valuable. Silently, you begin to move around the castle. Score! A dining room filled with polished gold and silver.""")
            print()
            keeplookingdec = input("""Would you like to steal some of the silverware? (yes/no): """)
            if keeplookingdec == 'no':
                print()
                print("""Picking up a silver fork admires its quality. Under normal circumstances, this would be ripe for the picking, but you do not want to alert anyone that you are here. You put it down heading through the dining hall and into the kitchen. A large iron potbelly furnace stands in the center of the room. Suddenly, a fire bursts into life beneath it. Behind you the voice of an old woman laughs, “We’ve been waiting all night for you, the table is all set, and YOU’RE THE MAIN COURSE!”. """)
                print()
                print('YOU DIED')
                #ending8
            elif keeplookingdec == 'yes':
                print()
                print("""All this gold and silver, but you have no bag to carry it in. You decide to grab as much silverware as you can carry and stuff it into your pockets. Picking up the last silver fork, you place it in your back pocket. Turning around, you decide to look for an empty room in the basement. Heading towards the stairs. A man approaches you, keeping his distance. “You have stolen from me” he declares in a monotone almost inhuman voice. “No I haven't,” you reply. “What did you take from the dining room?”. He moves out of the shadows and into plain view. Tall and pale, his fangs glisten as he hissed out. “WHAT DID YOU TAKE?”. Enraged he rushes towards you with inhuman speed, but not before you reach into your back pocket revealing a silver fork. As he tackles you to the floor you feel a sharp pain in your neck. Not before you stab him in the chest with the fork. You both fall to the ground. Suddenly, the vampire bursts into flames. You are alive, but at what cost. You have been cursed to live a half-life. Untouched by the warmth of sunlight, you must live out the rest of your days as the new Dracula.""")
                print()
                print('YOU LIVE, AMONG THE DEAD')
                #ending9


