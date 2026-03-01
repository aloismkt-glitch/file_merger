import os
import tkinter as tk
from tkinter import messagebox
import webbrowser


def merge_files():
    try:
        blank_lines = int(blank_entry.get())
    except ValueError:
        messagebox.showerror('오류', '공백 칸 수는 숫자로 입력하십시오.')
        return

    insert_name = name_var.get()
    sort_order = sort_var.get()
    current_dir = os.getcwd()
    output_filename = 'merged_output.txt'

    txt_files = [f for f in os.listdir(current_dir) if f.endswith('.txt') and f != output_filename]

    if not txt_files:
        messagebox.showinfo('알림', '현재 폴더에 병합할 txt 파일이 없습니다.')
        return

    # 정렬 옵션 적용
    txt_files.sort(reverse=(sort_order == 'desc'))

    try:
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            for i, file in enumerate(txt_files):
                if insert_name:
                    outfile.write(f'--- {file} ---\n')

                with open(file, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())

                if i < len(txt_files) - 1:
                    if blank_lines > 0:
                        outfile.write('\n' * blank_lines)
                    else:
                        outfile.write('\n')

        messagebox.showinfo('완료', f'총 {len(txt_files)}개의 파일을 {output_filename}로 합쳤습니다.')
    except Exception as e:
        messagebox.showerror('오류', f'파일 병합 중 오류가 발생했습니다: {e}')


def open_link(url):
    webbrowser.open(url)


# GUI 설정
root = tk.Tk()
root.title('TXT 파일 병합 프로그램')
root.geometry('450x500')
root.resizable(False, False)

# 사용 방법 안내
guide_frame = tk.Frame(root, pady=15)
guide_frame.pack()
tk.Label(guide_frame, text='[사용 방법]', font=('맑은 고딕', 12, 'bold')).pack()
tk.Label(guide_frame, text='합치려는 txt 파일이 있는 폴더 안에\n본 프로그램을 넣고 실행하십시오.').pack()

# 설정 영역
setting_frame = tk.Frame(root, pady=10)
setting_frame.pack()

tk.Label(setting_frame, text='합치는 파일 간 공백 칸 수:').grid(row=0, column=0, padx=5, pady=5, sticky='e')
blank_entry = tk.Entry(setting_frame, width=5)
blank_entry.insert(0, '1')
blank_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

name_var = tk.BooleanVar()
name_var.set(True)
tk.Checkbutton(setting_frame, text='합칠 때 사이사이에 파일명 넣기', variable=name_var).grid(row=1, column=0, columnspan=2, pady=5)

# 정렬 순서 라디오 버튼 추가
sort_var = tk.StringVar()
sort_var.set('asc')
sort_frame = tk.Frame(setting_frame)
sort_frame.grid(row=2, column=0, columnspan=2, pady=5)
tk.Label(sort_frame, text='파일 병합 순서:').pack(side='left', padx=5)
tk.Radiobutton(sort_frame, text='오름차순 (A-Z)', variable=sort_var, value='asc').pack(side='left')
tk.Radiobutton(sort_frame, text='내림차순 (Z-A)', variable=sort_var, value='desc').pack(side='left')

# 실행 버튼
tk.Button(root, text='파일 합치기 실행', command=merge_files, width=20, height=2, bg='#4CAF50', fg='white').pack(pady=10)

# 구분선
tk.Frame(root, height=2, bd=1, relief='sunken').pack(fill='x', padx=20, pady=15)

# 링크 영역
links_frame = tk.Frame(root)
links_frame.pack()

LINKS = [
    ("\u25b6 AI NEXT: 한눈에 읽는 AI 진화 계보", "https://play.google.com/store/books/details?id=2i7BEQAAQBAJ"),
    ("\u25b6 약사가 알려주는 화장품 성분", "https://www.yes24.com/Product/Goods/179601623"),
    ("\u25b6 을의 협상력: 중소기업 대표를 위한 거래 테이블 생존 전략", "https://play.google.com/store/books/details?id=K_e0EQAAQBAJ"),
    ("\u25b6 고객의 속마음을 여는 대화법", "https://play.google.com/store/books/details?id=Vfe0EQAAQBAJ"),
]

for text, url in LINKS:
    btn = tk.Button(links_frame, text=text, command=lambda u=url: open_link(u), anchor='w', width=45, relief='flat',
                    fg='blue', cursor='hand2')
    btn.pack(pady=2)

root.mainloop()