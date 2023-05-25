#!/usr/bin/env python3

class MyString:

  def __init__(self, value= ''):
    self.value = value

  def get_value(self):
    return self._value

  def set_value(self, string_value):
    if isinstance(string_value, str):
      self._value = string_value
    else:
      print('The value must be a string.')

  value = property(get_value, set_value)

  def is_sentence(self):
    return self._value.endswith(".")
    
  def is_question(self):
    return self._value.endswith("?")
    
  def is_exclamation(self):
    return self._value.endswith("!")
    
  def count_sentences(self):
    v = self.value
    for punctuation in ['!', '?']:
      v = v.replace(punctuation, ".")

    result = [s for s in v.split(".") if s]

    return len(result)
  