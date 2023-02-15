import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guess_state = []

while len(guess_state) < 50:
    answer_state = screen.textinput(title=f"{len(guess_state)}/50 states correct", prompt="What's Another State's Name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guess_state]
        data_frame = pandas.DataFrame(missing_states)
        df = data_frame.to_csv("missing_states.csv")
        break
    if answer_state in all_states:
        guess_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.pendown()
        t.write(answer_state)



