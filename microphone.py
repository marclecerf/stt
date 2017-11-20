import os
import pyaudio
import pocketsphinx as sphinx

DEFAULT_MODEL_PATH = sphinx.get_model_path()
DEFAULT_HMM_PATH = os.path.join(DEFAULT_MODEL_PATH, 'en-us')
DEFAULT_LM_PATH = os.path.join(DEFAULT_MODEL_PATH, 'en-us.lm.bin')
DEFAULT_DICT_PATH = os.path.join(DEFAULT_MODEL_PATH, 'cmudict-en-us.dict')

DEFAULT_DECODER_CONFIG = sphinx.Decoder.default_config()
DEFAULT_DECODER_CONFIG.set_string('-hmm', DEFAULT_HMM_PATH)
DEFAULT_DECODER_CONFIG.set_string('-lm', DEFAULT_LM_PATH)
DEFAULT_DECODER_CONFIG.set_string('-dict', DEFAULT_DICT_PATH)
DEFAULT_DECODER_CONFIG.set_int('-pl_window', 0)
DEFAULT_DECODER_CONFIG.set_int('-maxhmmpf', 3000)
DEFAULT_DECODER_CONFIG.set_int('-ds', 2)

class SpeechToText(object):
    """Poll a microphone and perform speech-to-text"""

    def __init__(self, config=DEFAULT_DECODER_CONFIG):
        self.stream = pyaudio.PyAudio().open(
            format=pyaudio.paInt16, channels=1,
            rate=16000, input=True,
            frames_per_buffer=1024)
        self.stream.start_stream()
        self.decoder = sphinx.Decoder(config)
        self.decoder.start_utt()

    def poll(self):
        in_speech_bf = False
        while True:
            buf = self.stream.read(1024)
            if buf:
                self.decoder.process_raw(buf, False, False)
                if self.decoder.get_in_speech() != in_speech_bf:
                    in_speech_bf = self.decoder.get_in_speech()
                    if not in_speech_bf:
                        self.decoder.end_utt()
                        res = self.decoder.hyp().hypstr
                        self.decoder.start_utt()
                        return res
        else:
            decoder.end_utt()
            return None

if __name__ == "__main__":
    stt = SpeechToText()
    while True:
        res = stt.poll()
        if res is None:
            break
        print('STT RESULT: %s' % res)


