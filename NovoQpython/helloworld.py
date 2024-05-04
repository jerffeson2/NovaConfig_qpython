#-*-coding:utf8;-*-
#qpy:console
#qpy:2
"""
Este é um arquivo de exemplo que mostra como usar QPython para desenvolver aplicativos Android.
Ele usa o recurso SL4A

@Author: Jerffeson
@Date: 2024-05-03
"""
import androidhelper

# Inicializa o objeto Android
droid = androidhelper.Android()

# Obtém a entrada do diálogo
line = droid.dialogGetInput().result

# Verifica se o usuário inseriu alguma entrada
if line is not None:
    s = "Hello, %s" % (line,)
    # Exibe uma mensagem de toast com o texto formatado
    droid.makeToast(s)
else:
    # Exibe uma mensagem de toast informando que não houve entrada
    droid.makeToast("No input provided")
