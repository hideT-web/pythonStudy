###################################
#西暦を和暦に変換するデスクトップアプリ
###################################
import PySimpleGUI as sg
from config import *

#画面配色パターンセット
sg.theme('LightBrown6')
#システム日付取得
now = "{0:%Y/%m/%d}".format(get_nowdate())

#画面レイアウト
layout = [[sg.Text("西暦"),           
           sg.Input(now,size=(12,1),
           text_color='#222',readonly=True, enable_events=True,key="-IN1-"),
           sg.CalendarButton('日付選択',
                format='%Y/%m/%d',                
                locale='ja_JP', 
                month_names=[ "{:>2d}月".format(m) for m in range(1, 13) ], 
                key='-BTN_CALENDER-',
                target='-IN1-')],
         [sg.Button("実行",key="-BTN_EXEC-"),sg.Button("閉じる",key="-BTN_CLOSE-")],
         [sg.Text(key="-TXT1-")]]
window = sg.Window("西暦を和暦に変換",layout,font=(None,16),size=(320,150))

#関数
def execute():
    txt = get_gengo(values["-IN1-"])
    window["-TXT1-"].update(txt)
def cal_change():
    now=values["-IN1-"]
    window['-BTN_CALENDER-'].calendar_default_date_M_D_Y =(int(now[5:7]), int(now[8:10]), int(now[0:4]))

##画面処理
while True:
    event, values = window.read()
    if event == '-IN1-':
        cal_change()
    if event == "-BTN_EXEC-":
        execute()    
    if event == None or event == "-BTN_CLOSE-":
        break
window.close()
