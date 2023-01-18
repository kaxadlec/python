# lol = [['Kai Havertz','29번'],['Mason Mount','19번'],['Reece James','24번']]
# print(dict(lol))
# lot = [('Kai Havertz','29번'),('Mason Mount','19번'),('Reece James','24번')]
# print(dict(lot))
#
# chelsea ={'Kai Havertz':'29번','Mason Mount':'19번','Reece James':'24번'}
# print(chelsea)
# print(len(chelsea))
#
# player_number = dict(Kai_Havertz = '29번', Mason_Mount = '19번', Reece_James = '24번')
# print(player_number)
# player_list = list(player_number)
# number_list = [player for player in player_number.values()]
# print(player_list,number_list)

# for i, player in enumerate(player_list):
#     print(player_number[1])
# for i in range(len(chelsea_player)):
#     print(chelsea_player[i])
# for chelsea in chelsea_player:
#     print(chelsea)

word ='letters'
letter_counts = {i:word.count(i) for i in word}
print(letter_counts)