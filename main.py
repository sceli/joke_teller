import requests
import tkinter

BLACK = "#000000"
YELLOW = "#F7DB6A"
DARK_YELLOW = "#EBB02D"


def get_joke():
    response = requests.get("https://v2.jokeapi.dev/joke/Any?type=single")
    response.raise_for_status()
    joke = response.json()["joke"]
    canvas.itemconfig(joke_text, text=joke, font=("Comic Sans MS", 15, "bold"))


window = tkinter.Tk()
window.title("Joke teller")
window.config(padx=25, pady=25, background=BLACK)

canvas = tkinter.Canvas(width=500, height=500, background=BLACK, highlightthickness=5, highlightbackground=YELLOW)
joke_text = canvas.create_text(250, 250, text="Wanna hear a joke?", width=450, font=("Comic Sans MS", 30, "bold"),
                               fill=YELLOW)
canvas.grid(row=0, column=0)

button = tkinter.Button(text="Tell me a joke", font=("Comic Sans MS", 25, "bold"), bg=YELLOW,
                        activebackground=DARK_YELLOW, command=get_joke)
button.grid(row=1, column=0)

window.mainloop()
