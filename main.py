from pynput.keyboard import Controller
import time

keyboard = Controller()

# text co chceš napsat
text = ("")

time.sleep(2)
for char in text:
  keyboard.type(char)
  # delay v sekundach
  # nezapomeň po každém pokusu tohle trochu poupravit
  time.sleep(0.280)