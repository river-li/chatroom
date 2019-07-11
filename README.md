A Simple Chatroom with Python and PyQt5, for Computer Network 's project.

## Usage

```bash
pip install -r requirements.txt
python src/server/server.py
python src/client/client.py
```

## Instruction
client.py是client的主程序

main_window是client.py的图形界面文件

backen_thread.py里面是后台侦听的类，主要是更新客户端的窗口文字

dialog和startup是刚运行时的弹窗

```
.
├── img
│   └── icon.svg
├── LICENSE
└── src
    ├── client
    │   ├── backen_thread.py
    │   ├── client.py
    │   ├── dialog.py
    │   ├── main_window.py
    │   ├── main_window.ui
    │   ├── startup.py
    │   └── startup.ui
    └── server
        ├── multi_task.py
        └── server.py

```

急着交作业，功能简陋，又丑，有空再改
