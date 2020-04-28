from urllib.request import urlopen
import random
import telebot
#from goto import goto, label 


bot = telebot.TeleBot("1113715967:AAEf5eBctEv0Oe2SNBMVLEur5-vOAF3r7hE")

while True:
    @bot.message_handler(content_types=['text'])
    def send_welcome(message):

        ganr = message.text
        html = urlopen("https://zaycev.net/genres/" + ganr + "/index.html").read().decode('utf-8')
        html_search = ""

        music = ["","","","","","","","","",""]
        e = 0


        while e < 10:
            rand_page = random.randint(1,5)
            if rand_page == 1:
                html = urlopen("https://zaycev.net/genres/" + ganr + "/index.html").read().decode('utf-8')
            else:
                html = urlopen("https://zaycev.net/genres/" + ganr + "/index_" + str(rand_page) + ".html").read().decode('utf-8')

            load_cnt = False
            music[e] = "https://zaycev.net"

            track_cnt = 0
            get_cnt = 0
            for i in html:
                rand_music = random.randint(1,20)
                if ("musicset-track__track-name" in html_search) and rand_music > 10:
                    track_cnt+=1
                    html_search = ""
                elif ("musicset-track__track-name" in html_search) and rand_music <= 10:
                    html_search = ""
                if ("href=\"" in html_search) and track_cnt > 0 and i != "\"":
                    music[e]+=i
                    get_cnt+=1
                if get_cnt > 0:
                    if i == "\"":
                        q = 0
                        dub_cnt = 0
                        while q < 10:
                            if music[e] == music[q]:
                                dub_cnt +=1
                                if dub_cnt == 2:
                                    music[e] = ""
                                    e-=1
                                    load_cnt = True
                            q+=1
                        break
                html_search += i
            e+=1
            if load_cnt == False:
                print(str(e) + "`s - music founded!")    

        for i in music:
            bot.send_message(message.chat.id, i)
    bot.polling( none_stop = True )
