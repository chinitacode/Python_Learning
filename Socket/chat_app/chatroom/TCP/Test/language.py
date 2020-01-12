# language.py

from settings import language

if language == 'en':
    administrator = 'Administrator'
    txt_administrator_close_chatroom = 'Chatroom closed by Administrator.'
    txt_uesr_enter_chatroom = 'entered the chatroom.'
    txt_user_quit_chatroom = 'quited the chatroom.'
    txt_username = 'username> '
    txt_user_already_exists = 'Username already exists!'
    txt_connect_to = 'Connected to'
    txt_connect_from = 'Connected from'
elif language == 'cn':
    administrator = '管理员'
    txt_administrator_close_chatroom = '管理员关闭了聊天室。'
    txt_uesr_enter_chatroom = '进入了聊天室。'
    txt_user_quit_chatroom = '退出了聊天室。'
    txt_username = '用户名> '
    txt_user_already_exists = '用户名已存在。'
    txt_connect_to = '连接到'
    txt_connect_from = '连接从'
