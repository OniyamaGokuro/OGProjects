#diceRoller
import flet as ft
import random
def main(page: ft.Page):

    def rollDice(e):
        valor = random.randint(1,6)
        rollNumber.value = str(valor)
        match(valor):
            case 1:
                diceImage.src = "https://storage.needpix.com/rsynced_images/dice-147665_1280.png"
            case 2:
                diceImage.src = "https://cdn.pixabay.com/photo/2013/07/12/13/57/dice-147666_1280.png"
            case 3:
                diceImage.src = "https://storage.needpix.com/thumbs/dice-147667_1280.png"
            case 4:
                diceImage.src = "https://cdn.pixabay.com/photo/2013/07/12/13/58/dice-147668_1280.png"
            case 5:
                diceImage.src = "https://cdn.pixabay.com/photo/2013/07/12/13/58/dice-147669_960_720.png"
            case 6:
                diceImage.src = "https://cdn.pixabay.com/photo/2013/07/12/13/58/dice-147670_1280.png"
        rollNumber.update()
        diceImage.update()


    page.horizontal_alignment = "CENTER"
    page.vertical_alignment = "CENTER"

    diceImage = ft.Image(src="https://w0.peakpx.com/wallpaper/77/41/HD-wallpaper-red-dice-cool-graphy-fun-abstract.jpg", height=400, width=400)
    rollNumber = ft.Text(value="No roll yet", size=40)
    rollButton = ft.ElevatedButton(text="Roll Dice", height=40, width=200, on_click=rollDice)
    page.add(diceImage, rollNumber, rollButton)

ft.app(target=main)


