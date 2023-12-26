import datetime
#定数
GG_NAME=0
ST_DATE=1
ED_DATE=2

STR_GANNEN='元'

#変数
era = [
    ['明治',18680125,19120729]
    ,['大正',19120730,19261224]
    ,['昭和',19261225,19890107]
    ,['平成',19890108,20190430]
    ,['令和',20190501,99999999]
    ]
def get_nowdate():
#本日の日付取得
    now = datetime.datetime.now()
    return now
def get_gengo(strDt):
#出力データ作成
    idate = int(strDt.replace('/', '')) #日付の「/」削除
    
    reslt=''
    for list1 in era:
        if (idate>=list1[ST_DATE]) and \
        idate<=list1[ED_DATE] :
            date_dd=str(list1[ST_DATE])
            date_nen = int(strDt[0:4]) - int(date_dd[0:4]) + 1
            #元号+年
            if(date_nen==1):
                reslt =list1[GG_NAME] + STR_GANNEN
            else:
                reslt = list1[GG_NAME] + f"{date_nen:02}"
            #出力日付の生成
            reslt = reslt + "年" + strDt[5:7] + "月" + strDt[8:10] + "日"
            break
    return reslt