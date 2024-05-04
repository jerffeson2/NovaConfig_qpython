#-*-coding:utf8;-*-
#qpy:2
#qpy:kivy
"""
Este é um arquivo de exemplo que mostra como usar QPython para desenvolver aplicativos Android.
Obtenha um endereço de link de vídeo de uma página da Web remota e reproduza-o com o A8 Player
para reproduzir. (Precisa da rede)

@Author: Jerffeson
@Date: 2024-05-03
"""
from jnius import cast
from jnius import autoclass
from jnius import JavaException
from android import AndroidBrowser
from urllib.request import urlopen  # Importa urlopen do módulo urllib.request

# Adiciona parênteses ao redor da mensagem de print
print("[A8 Player with qpython example]")

# get and parse video link
response = urlopen('http://qpython.com/samples/script_data.txt')
if response:
    # Decodifica o conteúdo da resposta para string usando UTF-8
    content = response.read().decode('utf-8')
    import json
    data = json.loads(content)
    link = data['link']

    # get android object
    PythonActivity = autoclass('org.renpy.android.PythonActivity')
    Intent = autoclass('android.content.Intent')
    Uri = autoclass('android.net.Uri')
    Toast = autoclass('android.widget.Toast')

    # play the url
    intent = Intent()
    intent.setAction(Intent.ACTION_VIEW)
    intent.setClassName('com.hipipal.mna8', 'com.hipipal.mna8.PLAPlayerAct')
    intent.setDataAndType(Uri.parse(link), 'video/*')
    currentActivity = cast('android.app.Activity', PythonActivity.mActivity)

    try:
        s = "Play Video: %s..." % link
        print(s)

        currentActivity.startActivity(intent)
    except JavaException:
        s = "Need install A8 Player App first"
        print(s)

        browser = AndroidBrowser()
        browser.open("http://play.tubebook.net/a8-video-player.html")

    print("[A8 Player with qpython END]")

else:
    print("Maybe network error, could not get the parameters for play")
