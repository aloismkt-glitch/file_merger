import os
import tkinter as tk
from tkinter import messagebox
import webbrowser


def open_link(url):
    webbrowser.open_new(url)


def merge_files():
    try:
        blanks = int(blank_entry.get())
    except ValueError:
        messagebox.showerror('오류', '공백 칸 수는 숫자로 입력해야 한다.')
        return

    include_filename = filename_var.get()
    sort_order = sort_var.get()

    files = [f for f in os.listdir('.') if f.endswith('.csv') and f != 'merged_output.csv']

    if not files:
        messagebox.showinfo('알림', '현재 폴더에 병합할 csv 파일이 없다.')
        return

    files.sort(reverse=(sort_order == 'desc'))

    try:
        with open('merged_output.csv', 'w', encoding='utf-8-sig') as outfile:
            for i, file in enumerate(files):
                if include_filename:
                    outfile.write(f'--- {file} ---\n')

                with open(file, 'r', encoding='utf-8-sig') as infile:
                    outfile.write(infile.read())

                if not outfile.tell() == 0:
                    outfile.write('\n')

                if i < len(files) - 1:
                    outfile.write('\n' * blanks)

        messagebox.showinfo('완료', '파일 병합이 완료되었다. (merged_output.csv)')
    except Exception as e:
        messagebox.showerror('오류', f'병합 중 오류가 발생했다: {e}')


root = tk.Tk()
root.title('CSV 병합 프로그램')
root.geometry('500x450')

tk.Label(root, text='사용방법: 합치려는 csv 폴더 안에 본 파일을 넣고 실행하세요.').pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text='1. 파일 간 공백(줄 수):').grid(row=0, column=0, sticky='w', pady=5)
blank_entry = tk.Entry(frame, width=5)
blank_entry.insert(0, '1')
blank_entry.grid(row=0, column=1, sticky='w')

filename_var = tk.BooleanVar(value=True)
tk.Checkbutton(frame, text='2. 사이사이에 파일명 넣기', variable=filename_var).grid(row=1, column=0, columnspan=2, sticky='w',
                                                                          pady=5)

tk.Label(frame, text='3. 정렬 방식:').grid(row=2, column=0, sticky='w', pady=5)
sort_var = tk.StringVar(value='asc')
tk.Radiobutton(frame, text='오름차순', variable=sort_var, value='asc').grid(row=2, column=1, sticky='w')
tk.Radiobutton(frame, text='내림차순', variable=sort_var, value='desc').grid(row=3, column=1, sticky='w')

tk.Button(root, text='병합 시작', command=merge_files, bg='lightblue', width=20).pack(pady=10)

rec_frame = tk.LabelFrame(root, text='추천 서적 (클릭 시 이동)')
rec_frame.pack(pady=10, fill='x', padx=20)

links = [
    ("\u25b6 AI NEXT: 한눈에 읽는 AI 진화 계보", "https://play.google.com/store/books/details?id=2i7BEQAAQBAJ"),
    ("\u25b6 약사가 알려주는 화장품 성분", "https://www.yes24.com/Product/Goods/179601623"),
    ("\u25b6 을의 협상력: 중소기업 대표를 위한 거래 테이블 생존 전략", "https://play.google.com/store/books/details?id=K_e0EQAAQBAJ"),
    ("\u25b6 고객의 속마음을 여는 대화법", "https://play.google.com/store/books/details?id=Vfe0EQAAQBAJ"),
]

for text, url in links:
    lbl = tk.Label(rec_frame, text=text, fg='blue', cursor='hand2', anchor='w')
    lbl.pack(fill='x', padx=10, pady=2)
    lbl.bind("<Button-1>", lambda e, u=url: open_link(u))

root.mainloop()
