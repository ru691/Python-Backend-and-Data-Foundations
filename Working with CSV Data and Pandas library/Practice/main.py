import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. State Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
all_states = states_data.state.to_list()
correct_guesses = []

while len(correct_guesses) < 50 :
    answer_state = screen.textinput(title = f"{len(correct_guesses)}/50 States correct",
                                    prompt = "What is your guess?").title()
    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in correct_guesses:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("missing_states.csv")
        break

    if answer_state in all_states:
        correct_guesses.append(answer_state)
        state = states_data[states_data["state"] == answer_state]
        print(state)
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(state.x.item(), state.y.item())
        writer.write(answer_state)

