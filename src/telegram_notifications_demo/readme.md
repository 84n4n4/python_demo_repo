1. create new bot using botfather https://core.telegram.org/bots/tutorial
2. create a new group on your cellphone, invite the botfather
3. check `https://api.telegram.org/bot<YourBOTToken>/getUpdates`
4. check for the ```"chat": {
            "id": <group_ID>,
            "title": "<Group name>"
        },``` field and copy the chat_id.
5. put chat_id and bot_id in your some .env or python config file
6. now simply calling the url ```'https://api.telegram.org/' + bot_id + '/sendMessage?chat_id=' + chat_id + '&text=someurlencodedmessage'``` will send a message to that chat and you will get notifications on your cellphone.
7. this of course can be done from behind any firewall since it only sends data to the internets, and doesnt need anything back.
8. also, this way does not require any libraries beyond urllib that is already in python
9. same thing could be done from a bashscript with curl or any other programming language capable of performing an http-get