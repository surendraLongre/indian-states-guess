import pandas
import turtle

#initialize initial variables
screen=turtle.Screen()
tim=turtle.Turtle()
tim.penup()
tim.hideturtle()
image="states.gif"
screen.addshape(image)
turtle.shape(image)
screen.title("Indian States")

#start the main code

#read states name and get in a list
csv_file=pandas.read_csv("coor_data.txt")
states=(csv_file["states"].to_list())
longitude=(csv_file["longitude"].to_list())
latitude=(csv_file["latitude"].to_list())

guessed_num=0
states_num=len(states)

while guessed_num!=states_num:
    answer_data=screen.textinput(title=f"Guessed {guessed_num}/{states_num}", prompt="What's another state's name? ").lower()
    for i in range(states_num):
        if answer_data==states[i].lower():
            guessed_num+=1
            tim.goto(latitude[i], longitude[i])
            tim.write(states[i], align="center", font="Courier")


turtle.mainloop()
