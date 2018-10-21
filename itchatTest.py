import itchat


def loginSuccess():
    print("登录成功")


def exitSuccess():
    print("退出登录")

# def getAllFriends():
#     return
# def getAllFriends():


if __name__ == '__main__' :
    itchat.auto_login(hotReload=True, loginCallback=loginSuccess, exitCallback=exitSuccess)
    # print(itchat.get_friends())
    all_friends = itchat.get_friends()
    for chatroom in itchat.get_contact():
        print(chatroom)
    # itchat.send_file()
    for friend in all_friends:
    #     print(friend)
        print(friend['NickName'])
    # itchat.send("Hello,chenhao", toUserName='@e8daa7b353fc0b8f4ea6d2ed45501c1fdd9b0a17a8e37bf2bd0b9c90ad9ec62c')
    # itchat.send_file("itchat.pkl")