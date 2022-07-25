def create_youtube_video(title,description):
	
	vidDic = {"Title":title,"Description":description,"Likes":0,"Dislikes":0,"comments":{}}
	return create_youtube_video



def like(vidDic):
	if Likes in vidDic:
		vidDic["Likes"] =+1
		return vidDic

def dislike(vidDic):
	if Dislikes in vidDic:
		vidDic["Disikes"]=+1
		return vidDic

def add_comment(vidDic,username,comment):
	if "comments" in vidDic:

		vidDic["commments"][username]=comment
		return

title = input("Enter a title for your video!")
description = input("Enter a description for your video!")
username = input("Please enter your username!")
comment = input("Add a comment!")

youtubevideo = create_youtube_video (title,description)
