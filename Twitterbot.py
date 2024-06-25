import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains

class TwitterBot:
    def __init__(self, username, password):
        # Initialize the ChromeDriver and open Twitter login page
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 30)  # Increased timeout to 30 seconds
        self.login(username, password)

    def login(self, username, password):
        try:
            self.driver.get("https://twitter.com/login")
            username_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='username']")))
            username_input.send_keys(username)
            username_input.send_keys(Keys.RETURN)
            print("Entered username")

            password_input = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
            password_input.send_keys(password)
            password_input.send_keys(Keys.RETURN)
            print("Entered password")

            home_indicator = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/home']")))
            print("Logged in successfully!")
        except TimeoutException as e:
            print(f"Login failed due to timeout: {e}")
        except NoSuchElementException as e:
            print(f"An error occurred during login: {e}")

    def post_tweet(self, tweet_text):
        try:
            autotw1 = WebDriverWait(self.driver, 3600).until(EC.element_to_be_clickable((By.CLASS_NAME, 'DraftEditor-root')))
            autotw1.click()

            element = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'public-DraftEditorPlaceholder-root')))
            ActionChains(self.driver).move_to_element(element).send_keys(tweet_text).perform()
            print("Entered tweet text")

            send_tw = WebDriverWait(self.driver, 3600).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='tweetButtonInline']")))
            send_tw.click()
            print("Tweet posted successfully!")
        except TimeoutException as e:
            print(f"Posting tweet failed due to timeout: {e}")
        except NoSuchElementException as e:
            print(f"An error occurred while posting the tweet: {e}")

    def post_img(self, tweet_text, image_path):
        try:
            self.driver.get("https://twitter.com/compose/tweet")
            upload_button = WebDriverWait(self.driver, 3600).until(EC.presence_of_element_located((By.XPATH, "//input[@accept='image/jpeg,image/png,image/webp,image/gif,video/mp4,video/quicktime']")))
            upload_button.send_keys(image_path)

            autotw1 = WebDriverWait(self.driver, 3600).until(EC.element_to_be_clickable((By.CLASS_NAME, 'DraftEditor-root')))
            autotw1.click()

            element = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'public-DraftEditorPlaceholder-root')))
            ActionChains(self.driver).move_to_element(element).send_keys(tweet_text).perform()
            print("Entered tweet text")

            send_tw = WebDriverWait(self.driver, 3600).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='tweetButton']")))
            send_tw.click()
            print("Tweet with image posted successfully!")
        except TimeoutException as e:
            print(f"Posting tweet with image failed due to timeout: {e}")
        except NoSuchElementException as e:
            print(f"An error occurred while posting the tweet with image: {e}")

    def like_tweet(self, tweet_url):
        try:
            self.driver.get(tweet_url)
            like_button = WebDriverWait(self.driver, 3600).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='like']")))
            like_button.click()
            print("Tweet liked successfully!")
        except TimeoutException as e:
            print(f"Liking tweet failed due to timeout: {e}")
        except NoSuchElementException as e:
            print(f"An error occurred while liking the tweet: {e}")

    def retweet(self, tweet_url):
        try:
            self.driver.get(tweet_url)
            retweet_button = WebDriverWait(self.driver, 3600).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='retweet']")))
            retweet_button.click()
            confirm_button = WebDriverWait(self.driver, 3600).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='retweetConfirm']")))
            confirm_button.click()
            print("Tweet retweeted successfully!")
        except TimeoutException as e:
            print(f"Retweeting failed due to timeout: {e}")
        except NoSuchElementException as e:
            print(f"An error occurred while retweeting: {e}")

    def follow_user(self, username):
        try:
            self.driver.get(f"https://twitter.com/{username}")
            follow_button = WebDriverWait(self.driver, 3600).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='placementTracking']")))
            follow_button.click()
            print(f"Followed user {username} successfully!")
        except TimeoutException as e:
            print(f"Following user {username} failed due to timeout: {e}")
        except NoSuchElementException as e:
            print(f"An error occurred while following the user: {e}")

    def unfollow_user(self, username):
        try:
            self.driver.get(f"https://twitter.com/{username}")
            unfollow_button = WebDriverWait(self.driver, 3600).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='unfollow']")))
            unfollow_button.click()
            print(f"Unfollowed user {username} successfully!")
        except TimeoutException as e:
            print(f"Unfollowing user {username} failed due to timeout: {e}")
        except NoSuchElementException as e:
            print(f"An error occurred while unfollowing the user: {e}")

class TwitterBotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Twitter Bot Login")
        
        self.root.configure(bg='lightblue')  # Set background color

        tk.Label(root, text="Username", bg='lightblue').grid(row=0, column=0)
        tk.Label(root, text="Password", bg='lightblue').grid(row=1, column=0)

        self.username_entry = tk.Entry(root)
        self.password_entry = tk.Entry(root, show="*")

        self.username_entry.grid(row=0, column=1)
        self.password_entry.grid(row=1, column=1)

        self.login_button = tk.Button(root, text="Login", command=self.login, bg='lightgreen', activebackground='green')
        self.login_button.grid(row=2, column=1, pady=5)

        self.bot = None

    def on_enter(self, e):
        e.widget['background'] = 'green'

    def on_leave(self, e):
        e.widget['background'] = 'lightgreen'

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        try:
            self.bot = TwitterBot(username, password)
            self.open_main_window()
        except Exception as e:
            messagebox.showerror("Login Error", str(e))

    def open_main_window(self):
        self.root.destroy()
        main_window = tk.Tk()
        main_window.title("Twitter Bot Actions")
        main_window.configure(bg='lightblue')  # Set background color

        tk.Label(main_window, text="Tweet Text", bg='lightblue').grid(row=0, column=0)
        tk.Label(main_window, text="Image Path", bg='lightblue').grid(row=1, column=0)
        tk.Label(main_window, text="Tweet URL", bg='lightblue').grid(row=2, column=0)
        tk.Label(main_window, text="Retweet URL", bg='lightblue').grid(row=3, column=0)
        tk.Label(main_window, text="Follow Username", bg='lightblue').grid(row=4, column=0)
        tk.Label(main_window, text="Unfollow Username", bg='lightblue').grid(row=5, column=0)

        self.tweet_entry = tk.Entry(main_window)
        self.image_path_entry = tk.Entry(main_window)
        self.like_url_entry = tk.Entry(main_window)
        self.retweet_url_entry = tk.Entry(main_window)
        self.follow_username_entry = tk.Entry(main_window)
        self.unfollow_username_entry = tk.Entry(main_window)
        
        self.tweet_entry.grid(row=0, column=1)
        self.image_path_entry.grid(row=1, column=1)
        self.like_url_entry.grid(row=2, column=1)
        self.retweet_url_entry.grid(row=3, column=1)
        self.follow_username_entry.grid(row=4, column=1)
        self.unfollow_username_entry.grid(row=5, column=1)

        self.post_tweet_button = tk.Button(main_window, text="Post Tweet", command=self.post_tweet, bg='lightgreen', activebackground='green')
        self.post_img_button = tk.Button(main_window, text="Post Image", command=self.post_img, bg='lightgreen', activebackground='green')
        self.like_tweet_button = tk.Button(main_window, text="Like Tweet", command=self.like_tweet, bg='lightgreen', activebackground='green')
        self.retweet_button = tk.Button(main_window, text="Retweet", command=self.retweet, bg='lightgreen', activebackground='green')
        self.follow_button = tk.Button(main_window, text="Follow", command=self.follow_user, bg='lightgreen', activebackground='green')
        self.unfollow_button = tk.Button(main_window, text="Unfollow", command=self.unfollow_user, bg='lightgreen', activebackground='green')

        self.post_tweet_button.grid(row=6, column=0, pady=5)
        self.post_img_button.grid(row=6, column=1, pady=5)
        self.like_tweet_button.grid(row=7, column=0, pady=5)
        self.retweet_button.grid(row=7, column=1, pady=5)
        self.follow_button.grid(row=8, column=0, pady=5)
        self.unfollow_button.grid(row=8, column=1, pady=5)

        # Bind hover events for buttons
        self.bind_button_events(self.post_tweet_button)
        self.bind_button_events(self.post_img_button)
        self.bind_button_events(self.like_tweet_button)
        self.bind_button_events(self.retweet_button)
        self.bind_button_events(self.follow_button)
        self.bind_button_events(self.unfollow_button)

        main_window.mainloop()

    def bind_button_events(self, button):
        button.bind("<Enter>", self.on_enter)
        button.bind("<Leave>", self.on_leave)

    def post_tweet(self):
        tweet_text = self.tweet_entry.get()
        if self.bot:
            self.bot.post_tweet(tweet_text)
        else:
            messagebox.showerror("Error", "Please login first")

    def post_img(self):
        tweet_text = self.tweet_entry.get()
        image_path = self.image_path_entry.get()
        if self.bot:
            self.bot.post_img(tweet_text, image_path)
        else:
            messagebox.showerror("Error", "Please login first")

    def like_tweet(self):
        tweet_url = self.like_url_entry.get()
        if self.bot:
            self.bot.like_tweet(tweet_url)
        else:
            messagebox.showerror("Error", "Please login first")

    def retweet(self):
        tweet_url = self.retweet_url_entry.get()
        if self.bot:
            self.bot.retweet(tweet_url)
        else:
            messagebox.showerror("Error", "Please login first")

    def follow_user(self):
        username = self.follow_username_entry.get()
        if self.bot:
            self.bot.follow_user(username)
        else:
            messagebox.showerror("Error", "Please login first")

    def unfollow_user(self):
        username = self.unfollow_username_entry.get()
        if self.bot:
            self.bot.unfollow_user(username)
        else:
            messagebox.showerror("Error", "Please login first")

if __name__ == "__main__":
    root = tk.Tk()
    app = TwitterBotApp(root)
    root.mainloop()
