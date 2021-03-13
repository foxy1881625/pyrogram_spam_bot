from pyrogram import Client

app = Client("my_account")

userchat =	"T_F_E_L_CHATIK"
chat_members = []

with app:
	for members in app.iter_chat_members(userchat):
		memebers_user = members.user.username
		if  members.user.is_bot == True:
			print("Bot")
		elif memebers_user == 'None' or memebers_user == "none":
			print("none username")
		else:
			app.send_message(memebers_user,"Привет друг,набираю аудиторию опытных программистов,можешь подписаться на блог - @oempsm")
print(chat_members)


app.run()