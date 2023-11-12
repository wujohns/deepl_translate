import gradio as gr
import deepl
import os

params = {
  "activate": True,
  "user_lang_code": "ZH",
  "bot_lang_code": "EN-US",
  'auth_key': ''
}

# https://www.deepl.com/docs-api/translate-text/?utm_source=github&utm_medium=github-python-readme
language_codes = {
  'English': 'EN-US',
  'Japanese': 'JA',
  'Chinese': 'ZH'
}

def setup():
  if os.getenv('DEEPL_AUTH_KEY'):
    params.update({ 'auth_key': os.getenv('DEEPL_AUTH_KEY') })
  if os.getenv('DEEPL_USER_LANG_CODE'):
    params.update({ 'user_lang_code': os.getenv('DEEPL_USER_LANG_CODE') })
  if os.getenv('DEEPL_BOT_LANG_CODE'):
    params.update({ 'bot_lang_code': os.getenv('DEEPL_BOT_LANG_CODE') })

def input_modifier(string):
  """
  This function is applied to your text inputs before
  they are fed into the model.
  """
  if not params['activate'] or params['auth_key'] == '':
    return string
  
  translator = deepl.translator.Translator(params['auth_key'])
  result = translator.translate_text(string, target_lang=params['bot_lang_code'])
  return result.text

def output_modifier(string):
  """
  This function is applied to the model outputs.
  """
  if not params['activate'] or params['auth_key'] == '':
    return string
  
  translator = deepl.translator.Translator(params['auth_key'])
  result = translator.translate_text(string, target_lang=params['user_lang_code'])
  return result.text

def bot_prefix_modifier(string):
  """
  This function is only applied in chat mode. It modifies
  the prefix text for the Bot and can be used to bias its
  behavior.
  """

  return string

def ui():
  user_lang_name = list(language_codes.keys())[list(language_codes.values()).index(params['user_lang_code'])]
  bot_lang_name = list(language_codes.keys())[list(language_codes.values()).index(params['bot_lang_code'])]

  with gr.Row():
    activate = gr.Checkbox(value=params['activate'], label='开启翻译')
    user_lang = gr.Dropdown(value=user_lang_name, choices=[k for k in language_codes], label='用户使用语言')
    bot_lang = gr.Dropdown(value=bot_lang_name, choices=[k for k in language_codes], label='模型使用语言')
    auth_key = gr.Textbox(value=params['auth_key'], label="deepl api key")

  activate.change(lambda x: params.update({"activate": x}), activate, None)
  user_lang.change(lambda x: params.update({"user_lang_code": language_codes[x]}), user_lang, None)
  bot_lang.change(lambda x: params.update({"bot_lang_code": language_codes[x]}), bot_lang, None)
  auth_key.change(lambda x: params.update({"auth_key": x}), auth_key, None)
