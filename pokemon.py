import requests as rq, sys
def check(res): #check for errors
    try:
        res.raise_for_status()
    except Exception as exc:
        print('Error: '+exc)
        sys.exit(1)
def pokemonType(pokemon):
    res=rq.get('https://pokeapi.co/api/v2/pokemon/'+pokemon)
    check(res)
    return res.json()['types'][0]['type']['name']
def pokemonAbilities(pokemon):
    res=rq.get('https://pokeapi.co/api/v2/pokemon/'+pokemon)
    check(res)
    lst=res.json()['abilities']
    return [lst[i]['ability']['name'] for i in range(len(lst))]
def doubleDamageFrom(pokemon,count=5,random=True):
    lst=doubleDamageType(pokemon)
    l=[]
    if random:
        i=0
        while True:
            for pos in range(len(lst)):
                r=rq.get('https://pokeapi.co/api/v2/type/'+lst[pos]).json()['pokemon']
                if i>=len(r):
                    continue
                if not count:
                    return l
                l.append(r[i]['pokemon']['name'])
                count-=1
            i+=1                           
    else:
        for pos in range(len(lst)):
            r=rq.get('https://pokeapi.co/api/v2/type/'+lst[pos]).json()['pokemon']
            for i in range(len(r)):
                if not count:
                    return l
                l.append(r[i]['pokemon']['name'])
                count-=1
def doubleDamageType(pokemon):
    res=rq.get('https://pokeapi.co/api/v2/pokemon/'+pokemon)
    check(res)
    res=rq.get(res.json()['types'][0]['type']['url'])
    check(res)
    lst=res.json()['damage_relations']['double_damage_from']
    l=[]
    for pos in range(len(lst)):
        l.append(lst[pos]['name'])
    return l