import os
message = input("変更を入力してください\n")
os.system("git add .")
print("git addが実行されました")
os.system("git status")
os.system(f"git commit -m {message}")