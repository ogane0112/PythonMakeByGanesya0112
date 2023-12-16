import tkinter as tk
#ui画面を表示させるためのコード
root = tk.Tk()
frame =tk.Frame(root)

#Hello worldと出力する関数
def hello():
    label_1.config(text="Hello world")
#表示した文字列を削除する関数
def delete_labal_01():
    label_1.config(text ="")
#ラベルを作成するコード
label = tk.Label(root, text ="一回押すごとにHello worldとターミナル上に出力されます！")
label.pack()
label_1 = tk.Label(root,text ="")
label_1.pack()


#Hello worldと出力させるためのボタンを作成する
button = tk.Button(frame,text="please click me",command=hello)
button.pack(side="left")
#文字列を削除するためのボタンを削除するためのコード
delete_labal_01_button = tk.Button(frame,text="消去",command=delete_labal_01)
delete_labal_01_button.pack(side="right")

frame.pack()
#このコードの前に他の処理を書くこと！
root.mainloop()