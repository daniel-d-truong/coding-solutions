
def anon_note_checker(mag_text, message):
  mag_text_lower = mag_text.lower()
  message_lower = message.lower()
  mag_text_list = mag_text_lower.split(" ")
  message_list = message_lower.split(" ")
  texts = {

  }
  for s in mag_text_list:
      if s in texts.keys():
          texts[s]+=1;
      else:
          texts[s] = 1;

  for s in message_list:
      if s not in texts.keys():
          return False
      else:
          texts[s]-=1;
          if texts[s] < 0:
              return False

  return True
