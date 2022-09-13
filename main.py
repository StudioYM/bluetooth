def on_bluetooth_connected():
    music.play_melody("C5 C C5 C C5 C C5 C ", 600)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_button_pressed_ab():
    music.start_melody(music.built_in_melody(Melodies.NYAN), MelodyOptions.ONCE)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

bluetooth.start_button_service()