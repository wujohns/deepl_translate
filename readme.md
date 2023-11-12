# Readme
deepl translate plugin for text-generation-webui，reference:  
1. deepl website: https://www.deepl.com/translator  
1. text-generation-webui: https://github.com/oobabooga/text-generation-webui  

## Usage
1. clone this repo to the extensions folder of text-generation-webui  
1. cd this repo folder and run `pip install -r requirements.txt` to install the deepl package  

## Arguments
when start the text-generation-webui, using following to enable this plugin:  
`--extension deepl_translate` - active this plugin  

## Env
`DEEPL_USER_LANG_CODE` - user input language code(only support `EN-US`, `JA`, `ZH`, default is `ZH`)  
`DEEPL_BOT_LANG_CODE` - the model's language code(only support `EN-US`, `JA`, `ZH`, default is `EN-US`)  
`DEEPL_AUTH_KEY` - the deepl auth key  

this plugin will:  
1. translate the model response to `DEEPL_USER_LANG_CODE`  
1. translate you input and prompt to `DEEPL_BOT_LANG_CODE`  

## example
```bash
export DEEPL_AUTH_KEY=xxx && \
export DEEPL_USER_LANG_CODE=ZH && \
export DEEPL_BOT_LANG_CODE=EN-US && \
python server.py
```
