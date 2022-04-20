from tkinter import Tk, Canvas, Button, ROUND
from PIL import Image


POSTSCRIPT_NAME = "media/temp_data.ps"
DRAWN_IMAGE_NAME = "media/drawn_image.png"
OUTPUT_IMAGE_SIZE = (320, 320)


def save_as_image():
    try:
        img = Image.open(POSTSCRIPT_NAME)
    except FileNotFoundError:
        return False
    img = img.resize(OUTPUT_IMAGE_SIZE, Image.ANTIALIAS)
    img.save(DRAWN_IMAGE_NAME, "png")
    return True


class CanvasWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title('Canvas')
        self.lasx = None
        self.lasy = None
        self.canvas = Canvas(self.root, bg='white', height=OUTPUT_IMAGE_SIZE[0], width=OUTPUT_IMAGE_SIZE[1])
        self.canvas.pack()
        self.exit_button = Button(self.root, text="Save and exit", command=self.exit_button_command)
        self.exit_button.pack()

    def get_coords(self, event):
        self.lasx, self.lasy = event.x, event.y

    def draw_line(self, event):
        self.canvas.create_line((self.lasx, self.lasy, event.x, event.y),
                                fill='black',
                                capstyle=ROUND,
                                width=25)
        self.canvas.postscript(file=POSTSCRIPT_NAME)
        self.lasx, self.lasy = event.x, event.y

    def exit_button_command(self):
        self.root.quit()
        self.root.destroy()


def main():
    app = CanvasWindow()
    app.canvas.bind("<Button-1>", lambda x: app.get_coords(x))
    app.canvas.bind("<B1-Motion>", lambda x: app.draw_line(x))
    app.root.mainloop()
    return save_as_image()
