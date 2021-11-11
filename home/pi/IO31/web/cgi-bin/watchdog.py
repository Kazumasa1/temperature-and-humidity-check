#!/usr/bin/python3
#
import datetime
#----------------------------------- センサーから値を取得する
# IN  - なし
# OUT - temp : string
#       humi : string
#
def getTempHumi():
    # この例では、エラー処理は考慮していないが、
    # センサーエラーを考慮するなら、エラーコードを
    # 上位ルーチンに返す必要あり
    #
    # temp : 温度
    # humi : 湿度
    # 温度、湿度を取得して、string型で変数に代入する
    temp = str(23)
    humi = str(65)

    return temp,humi
#----------------------------------- 現在日時を取得する
# IN  - なし
# OUT - dtm : string
#
def getDateTime():
    # dtm : 'yyyy-mm-dd hh:mm:ss'
    # 現在日時を取得して、string型で変数に代入する
    # 日時フォーマットは任意（以下の例はSQLの日時フォーマット）
    dtm = '2021-09-01 10:25:47'

    return dtm
#----------------------------------- CSVファイルに１件分のデータ出力
# IN  - dtm  : string
#       temp : string
#       humi : string
# OUT - なし
#
def putCSV(dtm,temp,humi):
    fileName = 'data.csv'   # CSVファイル名
    CRLF = '\x0d\x0a'       # 改行コード：CRLF
    LF   = '\x0a'           # 改行コード：LFのみ

    data = '"' + dtm + '", ' + temp + ', ' + humi
    with open(fileName, mode='a') as f:
        f.write(data)
        f.write(CRLF)

    return
#----------------------------------- main
if __name__ == '__main__':
    (temp, humi) = getTempHumi()
    dtm = getDateTime()
    putCSV(dtm,temp,humi)