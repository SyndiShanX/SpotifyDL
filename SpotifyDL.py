import subprocess
import json
import os

fileDir = os.getcwd()
fileDir = fileDir.replace('\\', '/')
fileDir = fileDir + '/'
print(fileDir)

Songs = open(fileDir + 'Songs.json')
SongsJson = json.load(Songs)

FilesList = os.listdir(fileDir + 'Downloaded-Songs')
DownloadedSongNames = [file for file in FilesList if file.endswith('.mp3')]
DownloadedSongNames = str(DownloadedSongNames).replace('é', 'e').replace('Ø', 'O').replace('AC/DC', 'ACDC').replace('Au/Ra', 'AuRa').replace('Axwell / Ingrosso', 'Axwell  Ingrosso').replace('Run–D.M.C.', 'Run D.M.C.').replace('ö', 'o').replace('ë', 'e').replace('å', 'a').replace('XXXTENTACION', 'XXXTentacion').replace('SABAI', 'Sabai').replace('Weird Al', "\'Weird Al\'").replace("\'Weird Al\' Yankovic - Foil", "\'Weird Al\' Yankovic - Foil").replace("Call of the Dead", "\'Call of the Dead\'").replace("Ridin\'", "\'Ridin\'\'").replace('Garrett Nash', 'gnash').replace('Ü', 'U').replace('á', 'a').replace('?', '').replace(' / ', '  ').replace('Wreck-It Ralph/Soundtrack', "\'Wreck-It Ralph\'Soundtrack").replace('’', "\'").replace('TROLLS', '\'TROLLS\'').replace('Friends', '\'Friends\'').replace('8 Mile', '\'8 Mile\'').replace('The Voice', '\'The Voice\'').replace('.../...', '......').replace('ñ', 'n').replace('*', '').replace('Man: Into', 'Man -  Into').replace('Parody of Party In The USA', "Parody of \'Party In The U.S.A.\'").replace('Armageddon', "\'Armageddon\'").replace('Alice Through The Looking Glass', "\'Alice Through The Looking Glass\'").replace('“', '').replace('”', '')

f = open(fileDir + 'Songs.bat', 'w')
f.write('')
f.close()

i = 0
SongNameReal = ''

while i < len(SongsJson['Songs']):
    SongURL = str(SongsJson['Songs'][i]).split("'Song URL': '")[1].split("'")[0]

    if "'Song Name': '" in str(SongsJson['Songs'][i]):
        SongName = str(SongsJson['Songs'][i]).split("'Song Name': '")[1].split("',")[0]
    else:
        SongName = str(SongsJson['Songs'][i]).split("'Song Name': \"")[1].split('",')[0]

    if "'Artist': '" in str(SongsJson['Songs'][i]):
        SongArtists = str(SongsJson['Songs'][i]).split("'Artist': '")[1].split("',")[0]
    else:
        SongArtists = str(SongsJson['Songs'][i]).split("'Artist': \"")[1].split('",')[0]

    SongArtist = SongArtists.split(', ')

    if len(SongArtist) == 1:
        SongFileNameTest = SongArtists + ' - ' + SongName + '.mp3'
        SongArtistFinal = SongArtists
    elif len(SongArtist) == 2:
        if SongArtist[1].lower() in SongName.lower():
            SongFileNameTest = SongArtist[0] + ' - ' + SongName + '.mp3'
            SongArtistFinal = SongArtist[0]
        else:
            SongFileNameTest = SongArtists + ' - ' + SongName + '.mp3'
            SongArtistFinal = SongArtists
    elif len(SongArtist) == 3:
        if SongArtist[1].lower() in SongName.lower():
            if SongArtist[2].lower() in SongName.lower():
                SongFileNameTest = SongArtist[0] + ' - ' + SongName + '.mp3'
                SongArtistFinal = SongArtist[0]
            else:
                SongFileNameTest = SongArtist[0] + ', ' + SongArtist[2] + ' - ' + SongName + '.mp3'
                SongArtistFinal = SongArtist[0] + ', ' + SongArtist[2]
        elif SongArtist[2].lower() in SongName.lower():
            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[1] + ' - ' + SongName + '.mp3'
            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[1]
        else:
            SongFileNameTest = SongArtists + ' - ' + SongName + '.mp3'
            SongArtistFinal = SongArtists
    elif len(SongArtist) == 4:
        if SongArtist[1].lower() in SongName.lower():
            if SongArtist[2].lower() in SongName.lower():
                if SongArtist[3].lower() in SongName.lower():
                    SongFileNameTest = SongArtist[0] + ' - ' + SongName + '.mp3'
                    SongArtistFinal = SongArtist[0]
                else:
                    SongFileNameTest = SongArtist[0] + ', ' + SongArtist[3] + ' - ' + SongName + '.mp3'
                    SongArtistFinal = SongArtist[0] + ', ' + SongArtist[3]
            else:
                if SongArtist[3].lower() in SongName.lower():
                    SongFileNameTest = SongArtist[0] + ', ' + SongArtist[2] + ' - ' + SongName + '.mp3'
                    SongArtistFinal = SongArtist[0] + ', ' + SongArtist[2]
                else:
                    SongFileNameTest = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[3] + ' - ' + SongName + '.mp3'
                    SongArtistFinal = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[3]
        else:
            if SongArtist[2].lower() in SongName.lower():
                if SongArtist[3].lower() in SongName.lower():
                    SongFileNameTest = SongArtist[0] + ', ' + SongArtist[1] + ' - ' + SongName + '.mp3'
                    SongArtistFinal = SongArtist[0] + ', ' + SongArtist[1]
                else:
                    SongFileNameTest = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[3] + ' - ' + SongName + '.mp3'
                    SongArtistFinal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[3]
            else:
                if SongArtist[3].lower() in SongName.lower():
                    SongFileNameTest = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2] + ' - ' + SongName + '.mp3'
                    SongArtistFinal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2]
                else:
                    SongFileNameTest = SongArtists + ' - ' + SongName + '.mp3'
                    SongArtistFinal = SongArtists
    elif len(SongArtist) == 5:
        if SongArtist[1].lower() in SongName.lower():
            if SongArtist[2].lower() in SongName.lower():
                if SongArtist[3].lower() in SongName.lower():
                    if SongArtist[4].lower() in SongName.lower():
                        SongFileNameTest = SongArtist[0] + ' - ' + SongName + '.mp3'
                        SongArtistFinal = SongArtist[0]
                    else:
                        SongFileNameTest = SongArtist[0] + ', ' + SongArtist[4] + ' - ' + SongName + '.mp3'
                        SongArtistFinal = SongArtist[0] + ', ' + SongArtist[4]
                else:
                    if SongArtist[4].lower() in SongName.lower():
                        SongFileNameTest = SongArtist[0] + ', ' + SongArtist[3] + ' - ' + SongName + '.mp3'
                        SongArtistFinal = SongArtist[0] + ', ' + SongArtist[3]
                    else:
                        SongFileNameTest = SongArtist[0] + ', ' + SongArtist[3] + ', ' + SongArtist[4] + ' - ' + SongName + '.mp3'
                        SongArtistFinal = SongArtist[0] + ', ' + SongArtist[3] + ', ' + SongArtist[4]
            else:
                if SongArtist[3].lower() in SongName.lower():
                    if SongArtist[4].lower() in SongName.lower():
                        SongFileNameTest = SongArtist[0] + ', ' + SongArtist[2] + ' - ' + SongName + '.mp3'
                        SongArtistFinal = SongArtist[0] + ', ' + SongArtist[2]
                    else:
                        SongFileNameTest = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[4] + ' - ' + SongName + '.mp3'
                        SongArtistFinal = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[4]
                else:
                    if SongArtist[4].lower() in SongName.lower():
                        SongFileNameTest = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[3] + ' - ' + SongName + '.mp3'
                        SongArtistFinal = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[3]
                    else:
                        SongFileNameTest = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[3] + ', ' + SongArtist[4] + ' - ' + SongName + '.mp3'
                        SongArtistFinal = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[3] + ', ' + SongArtist[4]
        else:
            if SongArtist[2].lower() in SongName.lower():
                if SongArtist[3].lower() in SongName.lower():
                    if SongArtist[4].lower() in SongName.lower():
                        SongFileNameTest = SongArtist[0] + ', ' + SongArtist[1] + ' - ' + SongName + '.mp3'
                        SongArtistFinal = SongArtist[0] + ', ' + SongArtist[1]
                    else:
                        SongFileNameTest = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[4] + ' - ' + SongName + '.mp3'
                        SongArtistFinal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[4]
                else:
                    if SongArtist[4].lower() in SongName.lower():
                        SongFileNameTest = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[3] + ' - ' + SongName + '.mp3'
                        SongArtistFinal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[3]
                    else:
                        SongFileNameTest = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[3] + ', ' + SongArtist[4] + ' - ' + SongName + '.mp3'
                        SongArtistFinal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[3] + ', ' + SongArtist[4]
            else:
                if SongArtist[3].lower() in SongName.lower():
                    if SongArtist[4].lower() in SongName.lower():
                        SongFileNameTest = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2] + ' - ' + SongName + '.mp3'
                        SongArtistFinal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2]
                    else:
                        SongFileNameTest = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2] + ', ' + SongArtist[4] + ' - ' + SongName + '.mp3'
                        SongArtistFinal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2] + ', ' + SongArtist[4]
                else:
                    if SongArtist[4].lower() in SongName.lower():
                        SongFileNameTest = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2] + ', ' + SongArtist[3] + ' - ' + SongName + '.mp3'
                        SongArtistFinal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2] + ', ' + SongArtist[3]
                    else:
                        SongFileNameTest = SongArtists + ' - ' + SongName + '.mp3'
                        SongArtistFinal = SongArtists
    elif len(SongArtist) == 6:
        if SongArtist[1].lower() in SongName.lower():
            if SongArtist[2].lower() in SongName.lower():
                if SongArtist[3].lower() in SongName.lower():
                    if SongArtist[4].lower() in SongName.lower():
                        if SongArtist[5].lower() in SongName.lower():
                            SongFileNameTest = SongArtist[0] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0]
                        else:
                            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[5] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[5]
                    else:
                        if SongArtist[5].lower() in SongName.lower():
                            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[4] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[4]
                        else:
                            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[4] + ', ' + SongArtist[5] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[4] + ', ' + SongArtist[5]
                else:
                    if SongArtist[4].lower() in SongName.lower():
                        if SongArtist[5].lower() in SongName.lower():
                            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[3] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[3]
                        else:
                            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[3] + ', ' + SongArtist[5] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[3] + ', ' + SongArtist[5]
                    else:
                        if SongArtist[5].lower() in SongName.lower():
                            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[3] + ', ' + SongArtist[4] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[3] + ', ' + SongArtist[4]
                        else:
                            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[3] + ', ' + SongArtist[4] + ', ' + SongArtist[5] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[3] + ', ' + SongArtist[4] + ', ' + SongArtist[5]
            else:
                if SongArtist[3].lower() in SongName.lower():
                    if SongArtist[4].lower() in SongName.lower():
                        if SongArtist[5].lower() in SongName.lower():
                            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[2] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[2]
                        else:
                            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[5] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[5]
                    else:
                        if SongArtist[5].lower() in SongName.lower():
                            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[4] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[4]
                        else:
                            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[4] + ', ' + SongArtist[5] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[4] + ', ' + SongArtist[5]
                else:
                    if SongArtist[4].lower() in SongName.lower():
                        if SongArtist[5].lower() in SongName.lower():
                            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[3] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[3]
                        else:
                            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[3] + ', ' + SongArtist[5] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[3] + ', ' + SongArtist[5]
                    else:
                        if SongArtist[5].lower() in SongName.lower():
                            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[3] + ', ' + SongArtist[4] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[3] + ', ' + SongArtist[4]
                        else:
                            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[3] + ', ' + SongArtist[4] + ', ' + SongArtist[5] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[3] + ', ' + SongArtist[4] + ', ' + SongArtist[5]
        else:
            if SongArtist[2].lower() in SongName.lower():
                if SongArtist[3].lower() in SongName.lower():
                    if SongArtist[4].lower() in SongName.lower():
                        if SongArtist[5].lower() in SongName.lower():
                            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[1] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[1]
                        else:
                            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[5] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[5]
                    else:
                        if SongArtist[5].lower() in SongName.lower():
                            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[4] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[4]
                        else:
                            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[4] + ', ' + SongArtist[5] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[4] + ', ' + SongArtist[5]
                else:
                    if SongArtist[4].lower() in SongName.lower():
                        if SongArtist[5].lower() in SongName.lower():
                            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[3] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[3]
                        else:
                            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[3] + ', ' + SongArtist[5] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[3] + ', ' + SongArtist[5]
                    else:
                        if SongArtist[5].lower() in SongName.lower():
                            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[3] + ', ' + SongArtist[4] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[3] + ', ' + SongArtist[4]
                        else:
                            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[3] + ', ' + SongArtist[4] + ', ' + SongArtist[5] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[3] + ', ' + SongArtist[4] + ', ' + SongArtist[5]
            else:
                if SongArtist[3].lower() in SongName.lower():
                    if SongArtist[4].lower() in SongName.lower():
                        if SongArtist[5].lower() in SongName.lower():
                            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2]
                        else:
                            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2] + ', ' + SongArtist[5] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2] + ', ' + SongArtist[5]
                    else:
                        if SongArtist[5].lower() in SongName.lower():
                            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2] + ', ' + SongArtist[4] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2] + ', ' + SongArtist[4]
                        else:
                            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2] + ', ' + SongArtist[4] + ', ' + SongArtist[5] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2] + ', ' + SongArtist[4] + ', ' + SongArtist[5]
                else:
                    if SongArtist[4].lower() in SongName.lower():
                        if SongArtist[5].lower() in SongName.lower():
                            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2] + ', ' + SongArtist[3] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2] + ', ' + SongArtist[3]
                        else:
                            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2] + ', ' + SongArtist[3] + ', ' + SongArtist[5] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2] + ', ' + SongArtist[3] + ', ' + SongArtist[5]
                    else:
                        if SongArtist[5].lower() in SongName.lower():
                            SongFileNameTest = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2] + ', ' + SongArtist[3] + ', ' + SongArtist[4] + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2] + ', ' + SongArtist[3] + ', ' + SongArtist[4]
                        else:
                            SongFileNameTest = SongArtists + ' - ' + SongName + '.mp3'
                            SongArtistFinal = SongArtists
    else:
        SongFileNameTest = SongArtists + ' - ' + SongName + '.mp3'
        SongArtistFinal = SongArtists
    if str(DownloadedSongNames) != '[]' and len(DownloadedSongNames) > 500:
        if SongName.lower() in str(DownloadedSongNames).lower():
            z = 1
            while z < len(DownloadedSongNames.split(SongArtistFinal)):
                if SongName in DownloadedSongNames.split(SongArtistFinal)[z]:
                    if DownloadedSongNames.split(SongArtistFinal)[z]:
                        SongNameReal = DownloadedSongNames.split(SongArtistFinal)[z].split('.mp3')[0]
                        SongFileNameReal = SongArtistFinal + SongNameReal + '.mp3'
                z = z + 1
            else:
                if SongNameReal != '':
                    f = None
                elif z > len(DownloadedSongNames.split(SongArtistFinal)):
                    SongNameReal = DownloadedSongNames.split(SongArtistFinal)[1].split('.mp3')[0]
                    SongFileNameReal = SongArtistFinal + DownloadedSongNames.split(SongArtistFinal)[1].split('.mp3')[0] + '.mp3'
                elif len(DownloadedSongNames.split(SongArtistFinal)) == 1:
                    if SongArtistFinal == "'Weird Al' Yankovic":
                        SongArtistFinal = "''Weird Al'' Yankovic"
                        SongNameReal = DownloadedSongNames.split(SongArtistFinal)[1].split('.mp3')[0]
                        SongFileNameReal = SongArtistFinal + DownloadedSongNames.split(SongArtistFinal)[1].split('.mp3')[0] + '.mp3'
                    else:
                        if SongArtistFinal == "Jack U, Skrillex, Diplo, Clean Bandit":
                            SongArtistFinal = "Jack U, Skrillex, Diplo, AlunaGeorge, Clean Bandit"
                            SongNameReal = DownloadedSongNames.split(SongArtistFinal)[1].split('.mp3')[0]
                            SongFileNameReal = SongArtistFinal + DownloadedSongNames.split(SongArtistFinal)[1].split('.mp3')[0] + '.mp3'
                elif z == len(DownloadedSongNames.split(SongArtistFinal)):
                    SongNameReal = DownloadedSongNames.split(SongArtistFinal)[1].split('.mp3')[0]
                    SongFileNameReal = SongArtistFinal + DownloadedSongNames.split(SongArtistFinal)[1].split('.mp3')[0] + '.mp3'
                else:
                    print("Error!")
        else:
            if SongArtistFinal == "'Weird Al' Yankovic":
                SongArtistFinal = "''Weird Al'' Yankovic"
                SongNameReal = DownloadedSongNames.split(SongArtistFinal)[1].split('.mp3')[0]
                SongFileNameReal = SongArtistFinal + DownloadedSongNames.split(SongArtistFinal)[1].split('.mp3')[0] + '.mp3'
            elif len(DownloadedSongNames.split(SongArtistFinal)) == 1:
                f = None
            else:
                if SongName in DownloadedSongNames.replace("''", "'"):
                    SongNameReal = DownloadedSongNames.split(SongArtistFinal)[1].split('.mp3')[0]
                    SongFileNameReal = SongArtistFinal + DownloadedSongNames.split(SongArtistFinal)[1].split('.mp3')[0].replace("''", "'") + '.mp3'

        if len(SongArtist) == 1:
            SongFileNameReal = SongArtists + ' - ' + SongName + '.mp3'
        elif len(SongArtist) == 2:
            if SongArtist[1].lower() in SongName.lower():
                SongFileNameReal = SongArtist[0] + ' - ' + SongName + '.mp3'
            else:
                SongFileNameReal = SongArtists + ' - ' + SongName + '.mp3'
        elif len(SongArtist) == 3:
            if SongArtist[1].lower() in SongName.lower():
                if SongArtist[2].lower() in SongName.lower():
                    SongFileNameReal = SongArtist[0] + ' - ' + SongName + '.mp3'
                else:
                    SongFileNameReal = SongArtist[0] + ', ' + SongArtist[2] + ' - ' + SongName + '.mp3'
            elif SongArtist[2].lower() in SongName.lower():
                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[1] + ' - ' + SongName + '.mp3'
            else:
                SongFileNameReal = SongArtists + ' - ' + SongName + '.mp3'
        elif len(SongArtist) == 4:
            if SongArtist[1].lower() in SongName.lower():
                if SongArtist[2].lower() in SongName.lower():
                    if SongArtist[3].lower() in SongName.lower():
                        SongFileNameReal = SongArtist[0] + ' - ' + SongName + '.mp3'
                    else:
                        SongFileNameReal = SongArtist[0] + ', ' + SongArtist[3] + ' - ' + SongName + '.mp3'
                else:
                    if SongArtist[3].lower() in SongName.lower():
                        SongFileNameReal = SongArtist[0] + ', ' + SongArtist[2] + ' - ' + SongName + '.mp3'
                    else:
                        SongFileNameReal = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[3] + ' - ' + SongName + '.mp3'
            else:
                if SongArtist[2].lower() in SongName.lower():
                    if SongArtist[3].lower() in SongName.lower():
                        SongFileNameReal = SongArtist[0] + ', ' + SongArtist[1] + ' - ' + SongName + '.mp3'
                    else:
                        SongFileNameReal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[3] + ' - ' + SongName + '.mp3'
                else:
                    if SongArtist[3].lower() in SongName.lower():
                        SongFileNameReal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2] + ' - ' + SongName + '.mp3'
                    else:
                        SongFileNameReal = SongArtists + ' - ' + SongName + '.mp3'
        elif len(SongArtist) == 5:
            if SongArtist[1].lower() in SongName.lower():
                if SongArtist[2].lower() in SongName.lower():
                    if SongArtist[3].lower() in SongName.lower():
                        if SongArtist[4].lower() in SongName.lower():
                            SongFileNameReal = SongArtist[0] + ' - ' + SongName + '.mp3'
                        else:
                            SongFileNameReal = SongArtist[0] + ', ' + SongArtist[4] + ' - ' + SongName + '.mp3'
                    else:
                        if SongArtist[4].lower() in SongName.lower():
                            SongFileNameReal = SongArtist[0] + ', ' + SongArtist[3] + ' - ' + SongName + '.mp3'
                        else:
                            SongFileNameReal = SongArtist[0] + ', ' + SongArtist[3] + ', ' + SongArtist[4] + ' - ' + SongName + '.mp3'
                else:
                    if SongArtist[3].lower() in SongName.lower():
                        if SongArtist[4].lower() in SongName.lower():
                            SongFileNameReal = SongArtist[0] + ', ' + SongArtist[2] + ' - ' + SongName + '.mp3'
                        else:
                            SongFileNameReal = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[4] + ' - ' + SongName + '.mp3'
                    else:
                        if SongArtist[4].lower() in SongName.lower():
                            SongFileNameReal = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[3] + ' - ' + SongName + '.mp3'
                        else:
                            SongFileNameReal = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[3] + ', ' + SongArtist[4] + ' - ' + SongName + '.mp3'
            else:
                if SongArtist[2].lower() in SongName.lower():
                    if SongArtist[3].lower() in SongName.lower():
                        if SongArtist[4].lower() in SongName.lower():
                            SongFileNameReal = SongArtist[0] + ', ' + SongArtist[1] + ' - ' + SongName + '.mp3'
                        else:
                            SongFileNameReal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[4] + ' - ' + SongName + '.mp3'
                    else:
                        if SongArtist[4].lower() in SongName.lower():
                            SongFileNameReal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[3] + ' - ' + SongName + '.mp3'
                        else:
                            SongFileNameReal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[3] + ', ' + SongArtist[4] + ' - ' + SongName + '.mp3'
                else:
                    if SongArtist[3].lower() in SongName.lower():
                        if SongArtist[4].lower() in SongName.lower():
                            SongFileNameReal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2] + ' - ' + SongName + '.mp3'
                        else:
                            SongFileNameReal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2] + ', ' + SongArtist[4] + ' - ' + SongName + '.mp3'
                    else:
                        if SongArtist[4].lower() in SongName.lower():
                            SongFileNameReal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2] + ', ' + SongArtist[3] + ' - ' + SongName + '.mp3'
                        else:
                            SongFileNameReal = SongArtists + ' - ' + SongName + '.mp3'
        elif len(SongArtist) == 6:
            if SongArtist[1].lower() in SongName.lower():
                if SongArtist[2].lower() in SongName.lower():
                    if SongArtist[3].lower() in SongName.lower():
                        if SongArtist[4].lower() in SongName.lower():
                            if SongArtist[5].lower() in SongName.lower():
                                SongFileNameReal = SongArtist[0] + ' - ' + SongName + '.mp3'
                            else:
                                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[5] + ' - ' + SongName + '.mp3'
                        else:
                            if SongArtist[5].lower() in SongName.lower():
                                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[4] + ' - ' + SongName + '.mp3'
                            else:
                                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[4] + ', ' + SongArtist[5] + ' - ' + SongName + '.mp3'
                    else:
                        if SongArtist[4].lower() in SongName.lower():
                            if SongArtist[5].lower() in SongName.lower():
                                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[3] + ' - ' + SongName + '.mp3'
                            else:
                                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[3] + ', ' + SongArtist[5] + ' - ' + SongName + '.mp3'
                        else:
                            if SongArtist[5].lower() in SongName.lower():
                                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[3] + ', ' + SongArtist[4] + ' - ' + SongName + '.mp3'
                            else:
                                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[3] + ', ' + SongArtist[4] + ', ' + SongArtist[5] + ' - ' + SongName + '.mp3'
                else:
                    if SongArtist[3].lower() in SongName.lower():
                        if SongArtist[4].lower() in SongName.lower():
                            if SongArtist[5].lower() in SongName.lower():
                                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[2] + ' - ' + SongName + '.mp3'
                            else:
                                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[5] + ' - ' + SongName + '.mp3'
                        else:
                            if SongArtist[5].lower() in SongName.lower():
                                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[4] + ' - ' + SongName + '.mp3'
                            else:
                                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[4] + ', ' + SongArtist[5] + ' - ' + SongName + '.mp3'
                    else:
                        if SongArtist[4].lower() in SongName.lower():
                            if SongArtist[5].lower() in SongName.lower():
                                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[3] + ' - ' + SongName + '.mp3'
                            else:
                                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[3] + ', ' + SongArtist[5] + ' - ' + SongName + '.mp3'
                        else:
                            if SongArtist[5].lower() in SongName.lower():
                                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[3] + ', ' + SongArtist[4] + ' - ' + SongName + '.mp3'
                            else:
                                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[2] + ', ' + SongArtist[3] + ', ' + SongArtist[4] + ', ' + SongArtist[5] + ' - ' + SongName + '.mp3'
            else:
                if SongArtist[2].lower() in SongName.lower():
                    if SongArtist[3].lower() in SongName.lower():
                        if SongArtist[4].lower() in SongName.lower():
                            if SongArtist[5].lower() in SongName.lower():
                                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[1] + ' - ' + SongName + '.mp3'
                            else:
                                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[5] + ' - ' + SongName + '.mp3'
                        else:
                            if SongArtist[5].lower() in SongName.lower():
                                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[4] + ' - ' + SongName + '.mp3'
                            else:
                                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[4] + ', ' + SongArtist[5] + ' - ' + SongName + '.mp3'
                    else:
                        if SongArtist[4].lower() in SongName.lower():
                            if SongArtist[5].lower() in SongName.lower():
                                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[3] + ' - ' + SongName + '.mp3'
                            else:
                                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[3] + ', ' + SongArtist[5] + ' - ' + SongName + '.mp3'
                        else:
                            if SongArtist[5].lower() in SongName.lower():
                                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[3] + ', ' + SongArtist[4] + ' - ' + SongName + '.mp3'
                            else:
                                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[3] + ', ' + SongArtist[4] + ', ' + SongArtist[5] + ' - ' + SongName + '.mp3'
                else:
                    if SongArtist[3].lower() in SongName.lower():
                        if SongArtist[4].lower() in SongName.lower():
                            if SongArtist[5].lower() in SongName.lower():
                                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2] + ' - ' + SongName + '.mp3'
                            else:
                                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2] + ', ' + SongArtist[5] + ' - ' + SongName + '.mp3'
                        else:
                            if SongArtist[5].lower() in SongName.lower():
                                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2] + ', ' + SongArtist[4] + ' - ' + SongName + '.mp3'
                            else:
                                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2] + ', ' + SongArtist[4] + ', ' + SongArtist[5] + ' - ' + SongName + '.mp3'
                    else:
                        if SongArtist[4].lower() in SongName.lower():
                            if SongArtist[5].lower() in SongName.lower():
                                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2] + ', ' + SongArtist[3] + ' - ' + SongName + '.mp3'
                            else:
                                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2] + ', ' + SongArtist[3] + ', ' + SongArtist[5] + ' - ' + SongName + '.mp3'
                        else:
                            if SongArtist[5].lower() in SongName.lower():
                                SongFileNameReal = SongArtist[0] + ', ' + SongArtist[1] + ', ' + SongArtist[2] + ', ' + SongArtist[3] + ', ' + SongArtist[4] + ' - ' + SongName + '.mp3'
                            else:
                                SongFileNameReal = SongArtists + ' - ' + SongName + '.mp3'
        else:
            SongFileNameReal = ''
    else:
        SongNameReal = 'Skip'
        SongFileNameReal = 'Skip'

    if SongNameReal == 'Skip':
        f = open(fileDir + 'Songs.bat', 'a')
        f.write('spotdl ' + SongURL + ' -o "' + fileDir + 'Downloaded-Songs"\n')
        f.close()
        print('Song with filename: "' + SongFileNameTest + '" not found, and added to the Download List!')
    elif SongFileNameTest.lower() != SongFileNameReal.lower():
        f = open(fileDir + 'Songs.bat', 'a')
        f.write('spotdl ' + SongURL + ' -o "' + fileDir + 'Downloaded-Songs"\n')
        f.close()
        print('Song with filename: "' + SongFileNameReal + '" not found, and added to the Download List!')
    else:
        # noinspection PyUnboundLocalVariable
        if SongNameReal == '':
            f = open(fileDir + 'Songs.bat', 'a')
            f.write('spotdl ' + SongURL + ' -o "' + fileDir + 'Downloaded-Songs"\n')
            f.close()
            print('Song with filename: "' + SongFileNameReal + '" not found, and added to the Download List!')
        else:
            print('Song with filename: "' + SongFileNameReal + '" already exists, skipping!')
    i = i + 1
    SongNameReal = ''

SongsYT = open(fileDir + 'Songs.bat', 'r').read().replace('spotdl https://open.spotify.com/track/11empTcflLLXn41XHmitrW -o "' + fileDir + 'Downloaded-Songs"', 'spotdl https://www.youtube.com/watch?v=CojnI6ikXMg|https://open.spotify.com/track/11empTcflLLXn41XHmitrW -o "' + fileDir + 'Downloaded-Songs"')

f = open(fileDir + 'Songs.bat', 'w')
f.write(SongsYT)
f.close()

subprocess.call('wt ' + fileDir + 'Songs.bat')
