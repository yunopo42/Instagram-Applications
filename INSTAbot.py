import instaloader
import tkinter as tk
from tkinter import messagebox


def download_post():
    # Get User Name
    user_name = entry_username.get()
    try:
        # Create an Instaloader object
        bot = instaloader.Instaloader()  # Use Instaloader with the correct capitalization

        # Create a profile object
        profile = instaloader.Profile.from_username(bot.context, user_name)

        # Get user's posts
        posts = profile.get_posts()

        for index, post in enumerate(posts, 1):
            bot.download_post(post, target=f"{profile.username}_{index}")

        # Success message
        messagebox.showinfo("Download Complete", "Download Complete")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# GUI
window = tk.Tk()
window.title("Instagram Downloader")
window.geometry("300x250")

# Username label
label = tk.Label(window, text="Kullanıcı Adı:")
label.pack(pady=10, padx=10)

# Username entry
entry_username = tk.Entry(window)
entry_username.pack(pady=10, padx=10)

# Download button
download_button = tk.Button(window, text="Download Post", command=download_post)
download_button.pack(pady=10, padx=10)

window.mainloop()
