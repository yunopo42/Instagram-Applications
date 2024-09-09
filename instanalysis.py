import instaloader
import tkinter as tk
from tkinter import ttk, messagebox


# Kullanıcı bilgilerini al
def get_user_info(username):
    bot = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(bot.context, username)
    except instaloader.exceptions.ProfileNotExistsException:
        return "Kullanıcı bulunamadı"

    # Bir sözlük oluştur
    user_info = {
        "username": profile.username,
        "followers": profile.followers,
        "followees": profile.followees,
        "post count": profile.mediacount,
        "Last post date": get_last_post_date(profile)
    }
    return user_info


# Kullanıcıya ait son gönderi tarihi çekme
def get_last_post_date(profile):
    last_post = None
    for post in profile.get_posts():
        if not last_post or post.date_utc > last_post.date_utc:
            last_post = post
    if last_post:
        return last_post.date_utc.strftime("%Y-%m-%d %H:%M:%S")
    return "No posts"


# Kullanıcı bilgilerini görüntüleme
def show_user():
    username = entry_username.get()
    if not username:
        messagebox.showerror("Hata", "Lütfen bir kullanıcı adı girin.")
        return
    user_info = get_user_info(username)
    if isinstance(user_info, dict):
        for widget in tree.get_children():
            tree.delete(widget)
        tree.insert('', 'end', values=(
            user_info['username'],
            user_info['followers'],
            user_info['followees'],
            user_info['post count'],
            user_info['Last post date']
        ))
    else:
        # Hata mesajı gönder
        messagebox.showerror("Hata", user_info)


# Tkinter arayüzü
window = tk.Tk()
window.title("Instagram Kullanıcı Bilgisi Görüntüleyici")

frame = tk.Frame(window)
frame.pack(padx=20, pady=20)

# Kullanıcı adı etiket
label = tk.Label(frame, text="Kullanıcı Adı: ")
label.grid(row=0, column=0, padx=5, pady=5)

# Kullanıcı adı giriş kutusu
entry_username = tk.Entry(frame)
entry_username.grid(row=0, column=1, padx=5, pady=5)

# Bilgi görüntüleme butonu
search_button = tk.Button(frame, text="Bilgileri Görüntüle", command=show_user)
search_button.grid(row=0, column=2, padx=5, pady=5)

# Bilgi tablosu
tree = ttk.Treeview(window, columns=("username", "followers", "followees", "post count", "Last post date"),
                    show='headings')
tree.heading("username", text="Username")
tree.heading("followers", text="Followers")
tree.heading("followees", text="Followees")
tree.heading("post count", text="Post Count")
tree.heading("Last post date", text="Last Post Date")
tree.pack(padx=20, pady=20)

window.mainloop()
