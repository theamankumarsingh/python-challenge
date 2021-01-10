import requests as rq, sys
def check(res):
    try:
        res.raise_for_status()
    except Exception as exc:
        print('Error: '+exc)
        sys.exit(1)
def ability(pokemon):
    res=rq.get('https://pokeapi.co/api/v2/pokemon/'+pokemon)
    check(res)
    lst=res.json()['abilities']
    return [lst[i]['ability']['name'] for i in range(len(lst))]
