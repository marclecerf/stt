# stt

Speech To Text (STT) sandbox

## Dependencies

* Tkinter
* PyAudio
* PocketSphinx

For Ubuntu folks, apt-get:

```
sudo apt-get install \
    python-tk \
    python-pyaudio \
    python-pocketsphinx
```

Or for pip:

```
pip install --upgrade \
    tk \
    pyaudio \
    pocketsphinx \

```

## tkstt.py

A simple Tkinter-based text window for printing the output
of the Pocket Sphinx speech-to-text converter applied to
audio input from the microphone.

