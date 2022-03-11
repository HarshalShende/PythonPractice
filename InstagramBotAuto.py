from instabot import Bot
bot=Bot()
#login to account
bot.login(username="",password="")
#follow user
bot.follow("username")
#upload picture
bot.upload_photo("c:/user/picture/abc.jpg",caption="hello world" )
#unfollow user
bot.unfollow("username")
#send message
bot.send_message("I love python ", ["user1","user2"])
#get followers details
followers=bot.get_user_followers("username_our")
for follower in followers:
    print(bot.get_user_info(followers))

#get following list
followings=bot.get_user_following("username")
for following in followings:
    print(bot.get_user_info(following))