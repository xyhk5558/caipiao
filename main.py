import requests
import time, datetime
import json
def get_week_day(date): #获取星期几
    week_day_dict = {
        0 : '星期一',
        1 : '星期二',
        2 : '星期三',
        3 : '星期四',
        4 : '星期五',
        5 : '星期六',
        6 : '星期天',
    }
    day = date.weekday()
    return week_day_dict[day]
def sc_send(desp,text='双色球开奖',key = "填写你的key"): #发送消息GET方法
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    url ="https://sc.ftqq.com/"+ key +".send?text="+text+"&desp="+ desp
    result = requests.get(url=url,headers=headers)
def query_api(): #查询开奖记录
    url = "https://bird.ioliu.cn/v2?url=http://cp.zgzcw.com/lottery/hisnumber.action?lotteryId=001&issueLen=1"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    req = requests.get(url=url,headers=headers)
    comments = dict(json.loads(req.text)[0])
    number = comments['lotteryNumber']
    kjtime = comments['ernieDate']
    kjnumber = comments['lotteryExpect']
    # 转换时间戳
    time_local = time.localtime(kjtime/1000)
    # 转换成新的时间格式(忽略时分秒)
    kjtime = time.strftime("%Y-%m-%d", time_local)
    desp = kjtime + "，第{0}期，最新开奖结果是：\n".format(kjnumber) + number
    return desp
if __name__ == '__main__':
    today = get_week_day(datetime.datetime.now())
    days = ['星期二','星期四','星期六']
    i  = 1
    while True:
        #判断开奖时间日期和时间
        if int(time.localtime()[3])  == 21 and today in days and int(time.localtime()[4]) == 30:
            sc_send(query_api())
            print("发送%s次" %i)
            i = i + 1
            #防止多次发送
            time.sleep(60)