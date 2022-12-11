from lcu_driver import Connector

connector = Connector()

@connector.ready
async def connect(connection):
    champ_left = []
    summoner = await connection.request('get', '/lol-summoner/v1/current-summoner')
    if summoner.status == 200 :
        summoner = await summoner.json()
        summoner = str(summoner['summonerId'])
        champions_get = await connection.request('get', '/lol-champions/v1/inventories/' + summoner + '/champions')
        champions = await champions_get.json()
        for x in range(1, len(champions)):
            champ_left.append(champions[x]["name"])
            nb_skins = len(champions[x]["skins"])
            for y in range(1, nb_skins):
                if(champions[x]["skins"][y]["ownership"]["owned"]==True):
                    champ_left.pop()
                    break
        champ_left.sort()
        for i in range(len(champ_left)):
            print(champ_left[i])
        print("Nombre de skin(s) manquant(s):", len(champ_left))





@connector.close
async def disconnect(connection):
    await connector.stop()

connector.start()