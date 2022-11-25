def image(list_me):
    deity = '![Alt text](../../../../../S:/GB/Python/Probnik4/DZ_12.11.22/image/deity.jpg)'
    dvarf = '![Alt text](../../../../../S:/GB/Python/Probnik4/DZ_12.11.22/image/dvarf.jpg)'
    elf = '![Alt text](../../../../../S:/GB/Python/Probnik4/DZ_12.11.22/image/elf.jpg)'
    essence = '![Alt text](../../../../../S:/GB/Python/Probnik4/DZ_12.11.22/image/essence.jpg)'
    goblin = '![Alt text](../../../../../S:/GB/Python/Probnik4/DZ_12.11.22/image/goblin.jpg)'
    human = '![Alt text](../../../../../S:/GB/Python/Probnik4/DZ_12.11.22/image/human.jpg)'
    orc = '![Alt text](../../../../../S:/GB/Python/Probnik4/DZ_12.11.22/image/orc.jpg)'
    pangolin = '![Alt text](../../../../../S:/GB/Python/Probnik4/DZ_12.11.22/image/pangolin.jpg)'
    slime = '![Alt text](../../../../../S:/GB/Python/Probnik4/DZ_12.11.22/image/slime.png'
    spirit = '![Alt text](../../../../../S:/GB/Python/Probnik4/DZ_12.11.22/image/spirit.jpg)'
    technocrat = '![Alt text](../../../../../S:/GB/Python/Probnik4/DZ_12.11.22/image/technocrat.jpg)'
    werewolf = '![Alt text](../../../../../S:/GB/Python/Probnik4/DZ_12.11.22/image/werewolf.jpg)'

    image_list = [deity, dvarf, elf, essence, goblin, human,
                  orc, pangolin, slime, spirit, technocrat, werewolf]
    if list_me[2] == 'deity':
        image_identifier = image_list[0]
    elif list_me[2] == 'dvarf':
        image_identifier = image_list[1]
    elif list_me[2] == 'elf':
        image_identifier = image_list[2]
    elif list_me[2] == 'essence':
        image_identifier = image_list[3]
    elif list_me[2] == 'goblin':
        image_identifier = image_list[4]
    elif list_me[2] == 'human':
        image_identifier = image_list[5]
    elif list_me[2] == 'orc':
        image_identifier = image_list[6]
    elif list_me[2] == 'pangolin':
        image_identifier = image_list[7]
    elif list_me[2] == 'slime':
        image_identifier = image_list[8]
    elif list_me[2] == 'spirit':
        image_identifier = image_list[9]
    elif list_me[2] == 'technocrat':
        image_identifier = image_list[10]
    elif list_me[2] == 'werewolf':
        image_identifier = image_list[11]
    print(image_identifier)
    with open('Persona.md', 'a') as data:
        data.write('image: ' + '**' + image_identifier + '**' + '\n\n')
