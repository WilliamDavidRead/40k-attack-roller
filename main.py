import random


def attackroll(bskill, nshots, strength, toughness, reroll):
    hitnum = 0
    hitcount = 0
    woundnum = 0
    shots = []
    wounds = []
    rerollbool = False
    if reroll == 'yes' or reroll == 'y' or reroll == 'Yes':
        rerollbool = True
        reroll = int(input('What numbers do you reroll? '))
    for shot in range(nshots):
        myroll = random.randint(1, 6)
        shots.append(myroll)
        if myroll < bskill and int(myroll) <= reroll and rerollbool:
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
        if (strength <= toughness / 2 and mywound > 5) or ((strength > toughness / 2) and mywound > 4) \
                or (strength == toughness and mywound > 3) or \
                ((strength > toughness) and (strength < toughness * 2) and mywound > 2):
            woundsuccess = True
        if woundsuccess:
            woundnum += 1
    print('Hit rolls: ', shots)
    print('Number of hits: ', hitnum)
    print('Wound rolls: ', wounds)
    print('Number of successful wound rolls: ', woundnum)
    return woundnum


attackroll(bskill=int(input('What is your Weapon/Ballistic Skill? ')), nshots=int(input('How many shots? ')),
           strength=int(input('What is your strength? ')), toughness=int(input('What is the target toughness? ')),
           reroll=input('Do you have any rerolls? '))


def savingthrow(savenum, ap, save, fnp):
    fnptest = False
    if fnp == 'yes' or fnp == 'y' or fnp == 'Yes':
        fnp = int(input('What is your feel no pain save? '))
        fnptest = True
    saves = []
    fnprolls = []
    failedsaves = 0
    finalfails = 0
    while savenum > 0:
        savenum -= 1
        savesuccess = False
        mysave = random.randint(1, 6)
        saves.append(mysave)
        if (mysave - ap) >= save:
            savesuccess = True
        if not savesuccess:
            finalfails += 1
    if fnptest:
        failedsaves = finalfails
        for i in range(finalfails):
            myfnp = random.randint(1, 6)
            fnprolls.append(myfnp)
            if myfnp >= fnp:
                finalfails -= 1
    if fnptest:
        print('Saving throw rolls: ', saves)
        print('Number of failed saves: ', failedsaves)
        print('Feel no pain rolls: ', fnprolls)
        print('Number of failed feel no pain rolls: ', finalfails)
    else:
        print('Saving throw rolls: ', saves)
        print('Number of failed saves: ', finalfails)


savingthrow(savenum=int(input('How many saving throws? ')), ap=int(input('What is the ap of the attacker? ')),
            save=int(input('What is your saving throw? ')), fnp=input('Do you have feel no pain? '))
