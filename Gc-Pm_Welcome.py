import amino
import time
client=amino.Client()

client.login(email="hotaku2323@gmail.com",password="adruin4242")

print("logged in.....")

cid="e5396610-2244-4d86-87a4-e212654b69ea"
cidy=cid

subclient=amino.SubClient(comId=cid,profile=client.profile)
print("inside community")
@client.event("on_group_member_join")
def on_group_member_join(data):
	if data.comId==cidy:
		try:
			x=data.message.author.icon
			response=requests.get(f"{x}")
			file=open("sample.png","wb")
			file.write(response.content)
			file.close()
			img=open("sample.png","rb")
			subclient.send_message(chatId=data.message.chatId,message=f"""[c]Welcome to the GC <${data.message.author.nickname}$>""",embedId=data.message.author.userId,embedTitle=data.message.author.nickname,embedLink=f"ndc://x{cid}/user-profile/{data.message.author.userId}",embedImage=img,mentionUserIds=[data.message.author.userId])
			print(f"\nwelcomed {data.message.author.nickname} to gc ")
		except Exception as e:
			print(e)
				
@client.event("on_group_member_leave")
def on_group_member_leave(data):
	if data.comId==cidy:
		try:
			subclient.send_message(chatId=data.message.chatId,message="""[c]Rip~""")
			print(f"Someone left the gc")
		except Exception as e:
			print(e)
def socketRoot():
	j=0
	while True:
		if j>=300:
			print("Updating socket.......")
			client.close()
			client.start()
			print("Socket updated")
			j=0
		j=j+1
		time.sleep(1)
socketRoot()

