import random


def attackroll(bskill, nshots, strength, toughness):
    hitnum = 0
    hitcount = 0
    woundnum = 0
    shots = []
    wounds = []
    for shot in range(nshots):
        myroll = random.randint(1, 6)
        shots.append(myroll)
        if myroll >= bskill:
            hitnum += 1
            hitcount = hitnum
    while hitcount > 0:
        hitcount -= 1
        woundsuccess = False
        mywound = random.randint(1, 6)
        wounds.append(mywound)
        if strength <= toughness/2 and mywound > 5:
            woundsuccess = True
        elif (strength > toughness / 2) and mywound > 4:
            woundsuccess = True
        elif strength == toughness and mywound > 3:
            woundsuccess = True
        elif (strength > toughness) and (strength < toughness * 2) and mywound > 2:
            woundsuccess = True
        elif strength >= toughness*2 and mywound > 1:
            woundsuccess = True
        if woundsuccess:
            woundnum += 1
    print('Hit rolls: ', shots)
    print('Number of hits: ', hitnum)
    print('Wound rolls: ', wounds)
    print('Number of wounds: ', woundnum)


attackroll(bskill=int(input('What is your Weapon/Ballistic Skill? ')), nshots=int(input('How many shots? ')),
           strength=int(input('What is your strength? ')), toughness=int(input('What is the target toughness? ')))
