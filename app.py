import PySimpleGUI as sg
from canvas import main, DRAWN_IMAGE_NAME, OUTPUT_IMAGE_SIZE
from predict import predict, visualization, BAR_NAME

IMAGE_ADDED = False

layout = [
    [sg.Column([
        [sg.Button(button_text="Draw", key="-DRAW-")],
        [sg.Image(source="icons/image.png", subsample=15, background_color="white", size=OUTPUT_IMAGE_SIZE, key="-IMAGE-")]]),
        sg.Image(source="icons/rightarrow.png", subsample=10),
        sg.Column([
            [sg.Button(button_text="Predict", key="-PREDICT-", disabled=True),
             sg.Checkbox(text="Normalized results", key="-MODE-")],
            [sg.Image(source="icons/bar_icon.png", subsample=3, background_color="white", size=OUTPUT_IMAGE_SIZE,
                      key="-RESULTS-")]])]]
window = sg.Window('🐸 Draw a number -> see the results 🐸', layout, finalize=True, font="Helvetica")
while True:
    event, values = window.read()
    if event == "-DRAW-":
        if main():
            window["-IMAGE-"].update(source=DRAWN_IMAGE_NAME, size=OUTPUT_IMAGE_SIZE)
            if not IMAGE_ADDED:
                IMAGE_ADDED = True
                window["-PREDICT-"].update(disabled=False)
            predictions = predict()
            visualization(predictions, window["-MODE-"].get())
            window["-RESULTS-"].update(source=BAR_NAME, size=OUTPUT_IMAGE_SIZE)
    if event == "-PREDICT-" and IMAGE_ADDED:
        predictions = predict()
        visualization(predictions, window["-MODE-"].get())
        window["-RESULTS-"].update(source=BAR_NAME, size=OUTPUT_IMAGE_SIZE)
    print(event, values)
    if event in (None, 'Exit', 'Cancel'):
        break
