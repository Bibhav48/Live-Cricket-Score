import requests
import bs4
import pymsgbox as p
import os
from time import sleep
from termcolor import cprint
from pygame import mixer

#link = 'https://www.cricbuzz.com/live-cricket-scorecard/22760/ind-vs-aus-1st-odi-australia-tour-of-india-2020'
# link = "https://www.cricbuzz.com/live-cricket-scorecard/59986/ind-vs-nz-2nd-odi-new-zealand-tour-of-india-2023"
# link = "https://www.cricbuzz.com/live-cricket-scorecard/60016/ind-vs-aus-2nd-test-australia-tour-of-india-2023"
link = "https://www.cricbuzz.com/live-cricket-scorecard/66162/nep-vs-uae-6th-match-icc-cricket-world-cup-league-two-2019-23"

mixer.init()
mixer.music.load('notification')
blank =""
prev_runs = prev_wkts = float("inf")
runs = wkts = 0
# try:
error_count = 0
while error_count < 10:
    try:
        res = requests.get(link)
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        details = soup.select('.cb-scrd-hdr-rw span')
    except:
        error_count +=1
    sleep(1)
    os.system("clear")
    gap = max(len(detail.get_text()) for detail in details)+5

    for i,info in enumerate(details):
        text=info.getText()
        #print(f"{blank:<5}{text:<0}")
        if i == 1:
            runs,wkts = text.split("-")
            wkts = int(wkts[0])
            runs = int(runs)
            if wkts>prev_wkts:
                mixer.music.play()
                p.alert(text=f'{"WICKET":^60}\n{details[i-1].getText()}: {wkts} wickets gone!!', title='WICKET', button='OK',timeout=5000)
                print("W")
                mixer.music.pause()
            elif prev_runs+6 == runs:
                mixer.music.play()
                print(4)
                p.alert(text=f'{"SIXXXXXXXX":^60}\n{details[i-1].getText()}: {runs} runs scored!!', title='SIXXXXXXXX', button='OK',timeout=5000)
                mixer.music.pause()
            elif prev_runs+4 == runs:
                print(4)
                mixer.music.play()
                p.alert(text=f'{"FOURRRRRR":^60}\n{details[i-1].getText()}: {runs} runs scored!!', title='FOURRRRRR', button='OK',timeout=5000)
                mixer.music.pause()
            prev_runs = runs
            prev_wkts = wkts
        
            
        if text[0].isdigit(): 
            new_text = text.strip()+"\n"
            print(new_text,end='')#! Use only one or zero print
        else:
            new_text = text.strip()+":"
            print(f"{new_text:<{gap}}",end='')#! Use only one or zero print
            


            
# except KeyboardInterrupt:
#     cprint("\nExited: 0","green")
# except Exception as e:
#     cprint(f"\n{e} \nExited:1","red")
    
