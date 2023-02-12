from translate import Translator

translator = Translator(to_lang='it')

try:
    with open('./text.txt', mode='r') as myFile:
        text = myFile.read()
        translation = translator.translate(text)
        with open('./translated.txt', mode='w') as myfile2:
            myfile2.write(translation)
except FileNotFoundError as e:
    print(e)