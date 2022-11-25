import image_list

def text_md(list1):
    list_txt = ['**', '\n\n', 'name: ', 'surname: ', 'race: ', 'age: ', 'growth: ',
                'clothes: ', 'facialfeatures: ', 'appearancefeatures: ',
                'strength: ', 'intelligence: ', 'skills: ', 'speed: ',
                'agikity: ', 'magic: ']

    with open('Persona.md', 'w') as data:
        for i in range(len(list1)):
            data.write(f"{list_txt[i+2]} {list_txt[0]}{list1[i]}{list_txt[0]} {list_txt[1]}")

    image_list.image(list1)