import tkinter as tk
import tkinter.ttk as ttk
import openai

openai.api_key = "あなたのopen aiのapiキー"

# 初期設定#############
root = tk.Tk()
root.title("guiで関数名教えて!")
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
window_w = screen_w // 2  # 2で割って少数以下切り捨てでintで返す
window_h = screen_h
root.geometry(f"{window_h}x{window_h}+0+0")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

frame2 = ttk.Frame(root)  # frame2をつかい各flameを作る
frame2.rowconfigure(0, weight=1)
frame2.columnconfigure(0, weight=1)
frame2.grid(row=0, column=0, sticky="nsew")
main_frame = tk.Frame(frame2, background="aquamarine1")  # 最初に出る画面
main_frame.grid(row=0, column=0, sticky="nsew")
#####################


def generat_answer():
    # print("a")
    char1 = entryBox1.get()

    str3 = "関数もしくは変数"
    str0 = (
        "ルール0 : 回答は日本語で行ってください,\nルール1 : 私の質問にはトークン数が260以下になるように答えてください,\nルール2 : 「以下のようなものが考えられます」のような前置きは省略してください,\nルール3 : あなたの考えた名前について説明もしてください,\n命令 : 私はプログラムを書いています。以下の"
        + str3
        + "につける名前を３つほど考えてください,\n"
        + str3
        + ":"
    )

    str1 = str0 + char1 + ","
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": str1},
        ],
        max_tokens=300,  # トークンを使える数には限りがあるので
        # temperature=0.7,
    )
    result = str(response["choices"][0]["message"]["content"])
    textBox1.configure(state=tk.NORMAL)  # 編集できる
    textBox1.insert(tk.END, result)
    textBox1.configure(state=tk.DISABLED)  # 編集禁止


# <オブジェクトの定義>
entryBox1 = tk.Entry(font=("Arial", 20), width=50)  # テキストボックスの横幅を設定,入力できる文字数？
entryBox1.place(relx=0.1, rely=0.05, relwidth=0.7, height=100)


label_textBox1 = tk.Label(
    main_frame,
    text="ここに質問",
)
label_textBox1.place(in_=main_frame, relx=0.0, rely=0.02, width=100, height=60)

textBox1 = tk.Text(main_frame, background="black", fg="white", font=("Arial", 20), state=tk.DISABLED)
textBox1.place(relx=0.1, rely=0.4, relwidth=0.7, relheight=0.45)

generat_button = tk.Button(main_frame, text="回答生成", font=18, command=generat_answer)
generat_button.place(in_=main_frame, relx=0.4, rely=0.3, width=150, height=80, anchor=tk.W)

# </オブジェクトの定義>
root.mainloop()  # 最終行
