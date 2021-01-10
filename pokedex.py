import pokemon as pk, os
import PySimpleGUI as sg
import pyttsx3 as tts

#code
layout = [  [sg.Text('Enter Pokemon:'), sg.Input(key='-INPUT-'),sg.Button('GO!')],
            [sg.Text(size=(50,25), key='-OUTPUT-',background_color='RED')],
            [sg.Button('About'),sg.Button('Quit')]]
sg.theme('Reds')
window = sg.Window('Pokedex', layout)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    message=''''''; color='WHITE'
    if event=='GO!':
        pokemon=values['-INPUT-'].strip()
        if pokemon=='':
            continue
        message="This is "+pokemon+". It is a "+pk.pokemonType(pokemon)+" type pokemon. It's abilities are "
        for x in pk.pokemonAbilities(pokemon):
            message+=x+' '
        message+='. It takes double damage from '
        for x in pk.doubleDamageType(pokemon):
            message+=x+' '
        message+=' type pokemons. Some of such pokemons to watch out for are  '
        for x in pk.doubleDamageFrom(pokemon):
            message+=x+' '
        color='WHITE'  
    if event=='About':
        message='''I'm Dexter, a Pokédex programmed by Professor Oak for Pokémon Trainer Aman Singh of the town of Pallet. My function is to provide Aman with information and advice regarding Pokémon and their training. If lost or stolen, I cannot be replaced. '''
        color='GREEN'
    window['-OUTPUT-'].update(message,text_color=color)
window.close()