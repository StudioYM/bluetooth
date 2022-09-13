bluetooth.onBluetoothConnected(function () {
    music.playMelody("C5 C C5 C C5 C C5 C ", 600)
})
input.onButtonPressed(Button.AB, function () {
    music.startMelody(music.builtInMelody(Melodies.Nyan), MelodyOptions.Once)
})
