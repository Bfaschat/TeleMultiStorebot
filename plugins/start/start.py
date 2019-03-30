from utils.typing import *
import random
import time, datetime, os, re, sys, sqlite3, json, io 
import requests
from pyrogram import Client, Filters, ReplyKeyboardRemove
from utils.broadcast import *
db = DBHelper()
sms = "Hello! [{}](tg://user?id={})! I can or may be able to download any downloadable file link you send to me and upload for you if and only if its a valid link. \n\n Send /faq to learn more about the usage and other useful tips"
@Client.on_message(Filters.command("start")) 
def start(bot, m):
    user=m.from_user.first_name
    
    id = ""
    if m.chat.type == 'private':
       smsg = sms
       id=m.from_user.id
    else:
      smsg = "start_msg"
      id=m.chat.id
    cc = db.checkifexist(id)
    
    if cc:
      sent = m.reply(smsg.format(user, id), quote=True)
    else:
      db.add_tlgrm_user(0, id)
      sent = m.reply(smsg.format(user, id), quote=True)
    if m.chat.type == 'supergroup':
      bot.send_message(id, "hello mother faker i am testing ")  