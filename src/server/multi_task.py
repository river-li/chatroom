import threading
import json

def log(msg):
    with open('server.log', 'a') as f:
        f.write(msg+'\n')

class User():
    def __init__(self, addr, client_sock):
        self.ADDR = addr
        self.clientSocket = client_sock

class ClientThread(threading.Thread):
    def __init__(self, user):
        threading.Thread.__init__(self)
        self.user = user

    def run(self):
        try:
            handle = Handle(self.user)
            while True:
                json_data = self.user.clientSocket.recv(1024)
                data = json.loads(json_data)
                log("RECV:  " + str(json_data)+ '\n')
                if data['type'] == 'logout':
                    break
                else:
                    handle.__main__(data)

        except Exception as e:
            print(e)
            log(str(e)+'\n')

        finally:
            name = Handle.usernames[self.user]
            log("用户" + str(name) + "登出\n")
            Handle.del_user(self.user)
            self.user.clientSocket.close()

    def stop(self):
        try:
            self.user.clientSocket.shutdown(2)
            self.user.clientSocket.close()
        except:
            pass


class Handle():
    usernames = {}

    def __init__(self, user):
       self.user = user

    @staticmethod
    def get_user(username):
        def getKey(list, value):
            return [k for k,v in d.items() if v == value][0]
        return getKey(Handle.usernames, username)

    @staticmethod
    def del_username(username):
        try:
            user = Handle.get_user(username)
            Handle.del_user(user)
        except:
            pass

    @staticmethod
    def del_user(user):
        try:
            Handle.usernames.pop(user)
        except Exception as e:
            print(e)
            log(str(e))

    @staticmethod
    def send_all(user_list, data):
        json_data = json.dumps(data)
        json_data = bytes(json_data, 'utf8')
        for user in user_list:
            user.clientSocket.send(json_data)
        log("__sendToAll__" + str(json_data))

    def send_me(self, data):
        """给本用户发送信息包"""
        json_data = json.dumps(data)
        json_data = bytes(json_data, 'utf8')
        self.user.clientSocket.send(json_data)
        log('__send__' + str(json_data))

    def login(self, data):
        """处理登录信息包"""
        # already login
        if self.user in Handle.usernames.keys():
            data['status'] = False
            data['info'] = "您已经登录了"
            # username in use
        elif data['username'] in Handle.usernames.values():
            data['status'] = False
            data['info'] = "用户名已被占用"
        else:
            data['status'] = True
            Handle.usernames[self.user] = data['username']
        self.send_me(data)

    def get_list(self, data):
        """获取在线用户列表"""
        name_list = Handle.usernames.values()
        name_list = list(name_list)
        data['list'] = name_list
        user_list = [user for user in Handle.usernames]
        self.send_all(user_list,data)

    def chat(self, data):
        """群聊(公共聊天)"""
        user_list = [user for user in Handle.usernames]
        self.send_all(user_list, data)

    def logout(self, data):
        """登出"""
        log("用户" + Handle.usernames[self.user] + "登出")
        Handle.del_user(self.user)

    def __main__(self, data):
        msg_type = data['type']
        methods = {
            "login": self.login,
            "list": self.get_list,
            "chat": self.chat,
            "logout": self.logout
        }

        try:
            return methods[msg_type](data)
        # 这里通过判断type的值，返回一个相应的函数
        # 用函数处理数据猴返回
        except Exception as e:
            print(e)
            log(str(e))
            data['status'] = False
            data['info'] = "Unknow Error"
            return data
