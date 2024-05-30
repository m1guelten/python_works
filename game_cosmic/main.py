
def game():
    arr = field_start()
    arr_step = func_next_step(arr)
    game_end_data(arr_step)


def game_start_data():
    with open("input.txt", "rb") as file:
        start_data = file.read().decode().replace("\r\n", " ").split(" ")
        [step, width, height, *field] = start_data
        return step, width, height, field


def game_end_data(arr):
    arr_end = field_end(arr)
    # print(arr_end)
    end_text = ""
    for i in range(len(arr_end)):
        end_text += "".join(arr_end[i]) + "\n"
    with open("output.txt", "w+") as file:
        file.write(end_text)


def field_end(arr):
    width, height = len(arr), len(arr[0])
    arr_end = [['.'] * width for i in range(height)]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                arr_end[i][j] = "x"
    return arr_end


def field_start():
    step, width, height, field = game_start_data()
    step, width, height = int(step), int(width), int(height)
    arr_game = [[0] * width for i in range(height)]
    for i in range(len(arr_game)):
        for j in range(len(arr_game[i])):
            if field[i][j] == "x":
                arr_game[i][j] = 1
    return arr_game


def calc_arr(arr, i, j):
    k_up = (i - 1 + len(arr)) % len(arr)
    k_down = (i + 1 + len(arr)) % len(arr)
    k_left = (j - 1 + len(arr[i])) % len(arr[i])
    k_right = (j + 1 + len(arr[i])) % len(arr[i])

    return (
            arr[k_up][k_left]
            + arr[k_up][j]
            + arr[k_up][k_right]
            + arr[i][k_left]
            + arr[i][k_right]
            + arr[k_down][k_left]
            + arr[k_down][j]
            + arr[k_down][k_right]
    )


def func_next_step(arr):
    arr_new = [[0] * len(arr[0]) for i in range(len(arr))]

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            res = calc_arr(arr, i, j)

            if arr[i][j] == 0:
                if res == 3:
                    arr_new[i][j] = 1
            else:
                arr_new[i][j] = 0 if res < 2 or res > 3 else 1

    return arr_new


game()
