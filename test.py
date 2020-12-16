from leaguepkg import Client_interface
from pprint import pprint
import time
import json
from ultimate_bravery import UltimateBravery
client = Client_interface.Client()
UB = UltimateBravery(client)
def summoners_rift():
    while True:
        try:
            summoner_data = client.get_player_champ_select()
        except KeyError:
            break
        for cell in summoner_data:
            if(cell['type'] == 'ban' and cell['completed'] == False and cell['isInProgress'] == True):
                client.select_champ(UB.ban.champ_id)
            elif cell['type'] == 'pick' and cell['completed'] == False and cell['isInProgress'] == True:
                client.select_champ(UB.champion.champ_id)
                runes = []
                for rune in UB.runes[1]:
                    runes.append(rune.rune_id)
                print(UB.runes[0].rune_id)
                print(runes)
                print(UB.runes[2].rune_id)
                print(client.change_current_page('ub-new', UB.runes[0].rune_id, runes, UB.runes[2].rune_id))

        time.sleep(3)
summoners_rift()
#print(client.change_current_page('dat new shit', 8200,[8229, 8275, 8233, 8236, 8463, 8429, 5007, 5003, 5001], 8400))
