from time import sleep


def win(arr, combinations, window, writer):
    sleepTime = 10

    # Win Player 1
    if any(redWinCheck == 1 for redWinCheck in combinations):
        window.clear()
        writer.write("Red Win!", font=("Arial", 50, "bold"))
        sleep(sleepTime)
        writer.clear()
        return True
    # Win Player 2
    if any(blueWinCheck == 8 for blueWinCheck in combinations):
        window.clear()
        writer.write("Blue Win!", font=("Arial", 50, "bold"))
        sleep(sleepTime)
        writer.clear()
        return True
    # Draw
    elif 0 not in arr:
        window.clear()
        writer.forward(100)
        writer.write("GG", font=("Arial", 50, "bold"))
        writer.backward(100)
        sleep(sleepTime)
        writer.clear()
        return True
    return False
