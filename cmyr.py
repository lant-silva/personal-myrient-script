import os
import requests
from bs4 import BeautifulSoup
def game_handle(url, nameplat):
    response = requests.get(url)
    gamename : str

    if response.status_code == 200:
        os.system('cls')
        print(f'Plataforma selecionada: {nameplat}\nDigite o nome do jogo (ou parecido)')
        gamename = input()

        soup = BeautifulSoup(response.content, 'html.parser')
        titles = [title.get_text() for title in soup.find_all('td', class_='link')]
        lower_titles = [title.lower() for title in titles]

        match = [title for title in titles if gamename in title.lower()]
        # se achar
        if match:
            print(len(match), f'jogos encontrados, escolha o jogo para ser baixado')
            for indice, valor in enumerate(match):
                print(f'({indice}) {valor}')
            escolha = int(input())

            # construir o endereço final pra usar o curl
            finalurl = url + match[escolha]

            # construir o diretorio q eu vou inserir o jogo
            direct = f"D:\\Jogos\\Emuladores\\ROMs\\{nameplat}"
            if not os.path.exists(direct):
                os.makedirs(direct)
                print(f'Diretório {nameplat} criado.')

            # baixar o jogo
            cmd = f'wget -P "{direct}" {finalurl.replace(" ", "%20")}'
            os.system(cmd)

            # ver se baixou
            dfile = os.path.join(direct, os.path.basename(finalurl))
            if os.path.isfile(dfile):
                # extrair o jogo
                cmd = f'unzip "{dfile}" -d "{direct}"'
                os.system(cmd)

                # e por fim, deletar o .zip
                os.remove(dfile)
                os.system('cls')
                print('Jogo baixado, agora é só abrir o emulador e se divertir :D')
                print('Baixar outro jogo? (S/n)')
                again = input()

                if again == "" or again == "S" or again == "s":
                    os.system('cls')
                    print('''
                          

            Escolha uma plataforma
            [Sony]
            1 - PS1 | 2 - PS2 | 3 - PS3 | 4 - PSP
   
            [Nintendo]
            5 - GBA | 6 - NES | 7 - SNES | 8 - GBC | 9 - GB 
            10 - N64 | 11 - NDS | 12 - GameCube | 13 - Wii | 14 - WiiU
            
            [Sega]
            15 - Master System | 16 - Mega Drive | 17 - 32X | 18 - GameGear
            19 - Sega CD | 20 - Dreamcast | 21 - Saturn


                    ''')
                    plat = input()
                    platform_handle(plat)

            else:
                print('Ocorreu um erro, o jogo não foi baixado')
        else:
            print('Nenhum jogo encontrado\nProcurar por outro jogo? (S/n)')
            again = input()
            if again == "" or again == "S" or again == "s":
                os.system('cls')
                print('''
                          

            Escolha uma plataforma
            [Sony]
            1 - PS1 | 2 - PS2 | 3 - PS3 | 4 - PSP
   
            [Nintendo]
            5 - GBA | 6 - NES | 7 - SNES | 8 - GBC | 9 - GB 
            10 - N64 | 11 - NDS | 12 - GameCube | 13 - Wii | 14 - WiiU
            
            [Sega]
            15 - Master System | 16 - Mega Drive | 17 - 32X | 18 - GameGear
            19 - Sega CD | 20 - Dreamcast | 21 - Saturn


                ''')
                plat = input()
                platform_handle(plat)
            if again == "n" or again == "N":
                os.system('cls')
    else:
        print('Erro', response.status_code)
    pass

def platform_handle(escolha):
    platform = {
        '1': 'Redump/Sony - PlayStation/',
        '2': 'Redump/Sony - PlayStation 2/',
        '3': 'Redump/Sony - PlayStation 3/',
        '4': 'Redump/Sony - PlayStation Portable/',
        '5': 'No-Intro/Nintendo - Game Boy Advance/',
        '6': 'No-Intro/Nintendo - Nintendo Entertainment System (Headered)/',
        '7': 'No-Intro/Nintendo - Super Nintendo Entertainment System/',
        '8': 'No-Intro/Nintendo - Game Boy Color/',
        '9': 'No-Intro/Nintendo - Game Boy/',
        '10': 'No-Intro/Nintendo - Nintendo 64 (BigEndian)/',
        '11': 'No-Intro/Nintendo - Nintendo DS',
        '12': 'Redump/Nintendo - GameCube - NKit RVZ [zstd-19-128k]/',
        '13': 'Redump/Nintendo - Wii - NKit RVZ [zstd-19-128k]/',
        '14': 'Redump/Nintendo - Wii U - WUX/',
        '15': 'No-Intro/Sega - Master System - Mark III/',
        '16': 'No-Intro/Sega - Mega Drive - Genesis/',
        '17': 'No-Intro/Sega - 32X/',
        '18': 'No-Intro/Sega - Game Gear/',
        '19': 'Redump/Sega - Mega CD & Sega CD/',
        '20': 'Redump/Sega - Dreamcast/',
        '21': 'Redump/Sega - Saturn/'
    }
    plat = platform.get(escolha, '0')
    plats = plat.split("/")
    nameplat = plats[1]
    # construir o endereço final
    url = f'https://myrient.erista.me/files/{plat}'
    game_handle(url, nameplat)

os.system('cls')
print('''
        ______  ___              _____            _____ 
        ___   |/  /____  ___________(_)_____________  /_
        __  /|_/ /__  / / /_  ___/_  /_  _ \_  __ \  __/
        _  /  / / _  /_/ /_  /   _  / /  __/  / / / /_  
        /_/  /_/  _\__, / /_/    /_/  \___//_/ /_/\__/  
                  /____/                                

            Script de download - Myrient
            Eu não tenho relações com os donos do projeto
      
            Escolha uma plataforma
            [Sony]
            1 - PS1 | 2 - PS2 | 3 - PS3 | 4 - PSP
   
            [Nintendo]
            5 - GBA | 6 - NES | 7 - SNES | 8 - GBC | 9 - GB 
            10 - N64 | 11 - NDS | 12 - GameCube | 13 - Wii | 14 - WiiU
      
            [Sega]
            15 - Master System | 16 - Mega Drive | 17 - 32X | 18 - GameGear
            19 - Sega CD | 20 - Dreamcast | 21 - Saturn
      
''')
plat = input()
platform_handle(plat)