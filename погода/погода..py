# погода
from tkinter import *
import requests
from PIL import Image, ImageTk, ImageFilter


def get_weather():
    city = entry.get()
    api_key = "a29f1b242da1a5fc7268c8e3090f95ad"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    temperature = round(data["main"]["temp"])
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    country = data["sys"]["country"]

    weather_info = f"Погода в городе {city}:\nТемпература: {temperature}°C\nВлажность: {humidity}%\nСкорость ветра: {wind_speed} м/с\nСтрана: {country}"
    canvas.delete("weather_info")
    canvas.create_text(350, 450, text=weather_info, fill="black", tags="weather_info")

    image2 = Image.open("C:\\КАРТИНКИ\\показ погоды.png")
    image2 = image2.resize((70, 50))
    global background_image1
    background_image1 = ImageTk.PhotoImage(image2)
    background_label1 = canvas.create_image(310, 360, anchor=NW, image=background_image1)


# создаю окно
root = Tk()
root.geometry("700x550")
root.title("Погода today?")
root.iconbitmap("C:\\КАРТИНКИ\\погода.ico")
root.resizable(False, False)

# фон приложения
canvas = Canvas(root, width=700, height=550)
canvas.pack()

image = Image.open("C:\\КАРТИНКИ\\фон погоды.jpg")
image = image.resize((700, 550), )
image = image.filter(ImageFilter.GaussianBlur(radius=3))
background_image = ImageTk.PhotoImage(image)
background_label = canvas.create_image(0, 0, anchor=NW, image=background_image)

image3 = Image.open("C:\\КАРТИНКИ\\облако пнг.png")
image3 = image3.resize((220, 200))
background_image3 = ImageTk.PhotoImage(image3)
background_label3 = canvas.create_image(235, -55, anchor=NW, image=background_image3)
# поля ввода
city_label = canvas.create_text(350, 50, text="Введите название города:", font=("Arial", 8, "bold"), fill="black")
entry_var = StringVar()
entry = Entry(root, textvariable=entry_var)
canvas.create_window(350, 100, window=entry)

get_weather_button = Button(root, text="Получить погоду", command=get_weather)
canvas.create_window(350, 150, window=get_weather_button)

root.mainloop()
