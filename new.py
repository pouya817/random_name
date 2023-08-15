import tkinter as tk
from tkinter import PhotoImage
import requests
from PIL import Image, ImageTk
import io
def show_person_details():
    want_age = int(age_entry.get())
    while True:
        global personal_info
        response = requests.get('https://randomuser.me/api/')
        personal_info = response.json()
        age = personal_info['results'][0]['dob']['age']
        if age < want_age:
            city = personal_info['results'][0]['location']['city']
            street = personal_info['results'][0]['location']['street']['name']
            number = personal_info['results'][0]['cell']
            email = personal_info['results'][0]['email']
            accepted_age = f'Hey, now I have found a {age} years old person from {city}, living on {street}, number is {number}, email is {email}. Maybe you want to chat with.\nIf you want more details, push "again".'
            result_label.config(text=accepted_age)

            # باز کردن و نمایش تصویر
            image_url = personal_info['results'][0]['picture']['large']
            image_response = requests.get(image_url)
            img_data = image_response.content
            img = Image.open(io.BytesIO(img_data))
            img = img.resize((150, 150), Image.LANCZOS)  # تغییر در این خط
            img = ImageTk.PhotoImage(img)
            image_label.config(image=img)
            image_label.image = img  # تاثیرگذاری بر روی تصویر در GUI
    
    
            break
    return personal_info
        
def show_more():
    root1=tk.Tk()
    root1.geometry("400x400")
    root1.title('more info')
    show_more= tk.Label(root1 , justify="center", text=personal_info)
    show_more.pack()

def send_sms(person):
    # sms_response = requests.post('https://api.kavenegar.com/v1/7065344F526B327A6359512B5A4E314A347332364355616A646D495A61364D39755047592B4E76343463773D/sms/send.json?receptor=09104346645&sender=10008663&message=%s' % personal_info)
    # sms_response_json = sms_response.json()
    # sms_status = sms_response_json['return']['status']
    print(person)
    print('ok all right enjoy your chat')
    return #sms_status
# ایجاد پنجره
root = tk.Tk()
root.title('Person Finder')

# ایجاد ویجت‌ها
age_label = tk.Label(root, text='Enter your age:')
age_label.pack()

age_entry = tk.Entry(root)
age_entry.pack()
print(age_entry)
show_button = tk.Button(root, text='Show Person Details', command=lambda:show_person_details(),activebackground='black',activeforeground='yellow',cursor="clock")
show_button.pack()

result_label = tk.Label(root, text='', wraplength=250)
result_label.pack()

image_label = tk.Label(root)
image_label.pack()

sms_label = tk.Label(root , text='if you want save intere sms button')
sms_label.pack()

sms_button = tk.Button(root, text='sms', command=lambda: send_sms(personal_info),activebackground='black', activeforeground='red')
sms_button.pack()



more_button = tk.Button(root, text='more info', command=lambda: show_more(),activebackground='black' , activeforeground='red',cursor="heart")
more_button.pack()

root.mainloop()