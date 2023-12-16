from moviepy.editor import VideoFileClip
import tkinter as tk
root = tk.TK()
#変数の宣言
clip_list=[]
#動画を読み取り結合するための関数
def movie_get(movie):
    clip =VideoFileClip(movie)
    clip_list.append(clip)
    return clip_list









root.mainloop()