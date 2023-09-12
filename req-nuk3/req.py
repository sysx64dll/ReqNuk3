from PySide6.QtWidgets import QTextEdit , QProgressBar
import requests
import colorama
import threading
import time


def send_json_request(url :str,json_data :str,responseEB :QTextEdit,progress_bar :QProgressBar,howMany :int):
    res_t = []
    responseEB.clear()
    for i in range(howMany):
        res = requests.post(url,data=json_data)
        res_t.append(res)
        print(res)
        print(url)
        print(json_data)
    for r in res_t:
        responseEB.append(str(r))
    loadProgressBar(progress_bar,howMany)
    """
    thread = threading.Thread(target=loadProgressBar,args=((progress_bar,)))
    thread.start()
    thread.join()
    """

def loadProgressBar(progress_bar :QProgressBar,howMany :int):
    c = 0
    for c in range(int(progress_bar.maximum())):
        progress_bar.setValue(c)
        time.sleep(0.01 * howMany)
        c+=1
    progress_bar.setValue(0)
    print("[+]request status is ok")
