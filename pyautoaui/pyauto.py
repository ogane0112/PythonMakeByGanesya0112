import pyautogui
import schedule
import time
#このコードを実行する際はマイクラを全画面表示に変えてください
def op_gui():
    #Escキーを入力する
    # (100, 200)の位置にマウスカーソルを移動
    pyautogui.moveTo(1000,850)
    # クリック
    pyautogui.click()
    #初期位置に戻す
    pyautogui.moveTo(500,500)
schedule.every(10).seconds.do(op_gui)
#無限ループさせる！
while True:
    #puautoguiの例外が発生したら取得するようにしてある
    try:
        #ここに宣言したコードが格納されて実行される
        schedule.run_pending()
        #CPUをやすませる
        time.sleep(1)
    except pyautogui.FailSafeException:
        print("PyAutoGUI fail-safe triggered. Please check your code.")