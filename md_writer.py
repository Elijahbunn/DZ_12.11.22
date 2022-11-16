#import constructor as cons

list_me = ['Kich', 'Urusai', 'goblin', 21, 189, 'coat, boots, pants',
            'pointed nose, brown eyes, high forehead',
            'scar on left cheek', 3, 4, 2, 5, 32, 4]

def text_md(list1):
    list_txt = ['**', '\n\n', 'name: ', 'surname: ', 'race: ', 'age: ', 'growth: ',
                'clothes: ', 'facialfeatures: ', 'appearancefeatures: ',
                'strength: ', 'intelligence: ', 'skills: ', 'speed: ',
                'agikity: ', 'magic: ']

    with open('list.md', 'w') as data:
        for i in range(len(list_txt)):
            data.write(f"{list_txt[i+2]} {list_txt[0]}{list1[i]}{list_txt[0]} {list_txt[1]}")

        # data.write('name: ' + '**' + list1[0] + '**' + '\n\n')
        # data.write('surname: ' + '**' + list1[1] + '**' + '\n\n')
        # data.write('race: ' + '**' + list1[2] + '**' + '\n\n')

        # data.write('age: ' + '**' + str(list1[3]) + '**' + '\n\n')
        # data.write('growth: ' + '**' + str(list1[4]) + '**' + '\n\n')
        # data.write('clothes: ' + '**' + list1[5] + '**' + '\n\n')
        # data.write('facialfeatures: ' + '**' +
        #            list1[6] + '**' + '\n\n')
        # data.write('appearancefeatures: ' + '**' +
        #            list1[7] + '**' + '\n\n')

        # data.write('strength: ' + '**' + str(list1[8]) + '**' + '\n\n')
        # data.write('intelligence: ' + '**' + str(list1[9]) + '**' + '\n\n')
        # data.write('skills: ' + '**' + str(list1[10]) + '**' + '\n\n')
        # data.write('speed: ' + '**' + str(list1[11]) + '**' + '\n\n')
        # data.write('agikity: ' + '**' + str(list1[12]) + '**' + '\n\n')
        # data.write('magic: ' + '**' + str(list1[13]) + '**' + '\n\n')


text_md(list_me)
