import urllib.request
import urllib.parse

def main():
    bot_id = '12345'
    chat_id = '12345'
    telegram_send_url = 'https://api.telegram.org/' + bot_id + '/sendMessage?chat_id=' + chat_id + '&text='
    message = urllib.parse.quote('some message to send')
    urllib.request.urlopen(telegram_send_url + message)

if __name__ == '__main__':
    main()