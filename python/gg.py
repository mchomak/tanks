import shelve

def save():
    global moneys2,kills2,file_moneyss,file_kilss,collect_freeztank_skin,collect_firetank_skin,collect_duotank_skin
    global file_collect_freeztank_skin,file_collect_firetank_skin,file_collect_duotank_skin
    moneys2=1000
    kills2=0
    collect_freeztank_skin = 1
    collect_firetank_skin = 0
    collect_duotank_skin = 0
    file_moneyss = "moneyss2"
    file_kilss="kilss2"
    file_collect_freeztank_skin='freeztank_skin'
    file_collect_firetank_skin='firetank_skin'
    file_collect_duotank_skin='duotank_skin'

    with shelve.open(file_moneyss) as states:
        states['moneys2'] = moneys2
        print(moneys2)

    with shelve.open(file_kilss) as states:
        states['kills2'] = kills2
        print(kills2)

    with shelve.open(file_collect_freeztank_skin) as states:
        states['freeztank_skin'] = collect_freeztank_skin
        print(collect_freeztank_skin)

def get_save():
    with shelve.open(file_moneyss) as states:
        moneys2 = (states['moneys2'])
        print(moneys2)

    with shelve.open(file_kilss) as states:
        kills2 = (states['kills2'])
        print(kills2)

    with shelve.open(file_collect_freeztank_skin) as states:
        collect_freeztank_skin = (states['freeztank_skin'])
        print(kills2)
save()
get_save()
