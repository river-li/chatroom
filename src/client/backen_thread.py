import threading
import json

class ListenThread(threading.Thread):
    def __init__(self, socket, father):
        threading.Thread.__init__(self)
        self.father = father
        self.socket = socket

    def get_list(self, data):
        list_box = self.father.listWidget
        list_box.clear()
        list_box.addItems(data["list"])

    def chat(self, data):
        text_box = self.father.textBrowser
        if data["type"] == "chat" :
            text = "Group:" + data["from"] + ":" + data["msg"] + '\n'
        text_box.append(text)

    def run(self):
        while True:
            try:
                json_data = self.socket.recv(1024)
                data = json.loads(json_data)
            except Exception as e:
                print(e)
                break
            print("RECV: "+str(json_data))

            methods = {
                "list": self.get_list,
                "chat": self.chat
            }
            methods[data["type"]](data)
        print("Thread Exit")

