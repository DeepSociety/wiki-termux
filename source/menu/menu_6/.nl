print("""
\033[1;39mBien si tienes el problema de que cuando inicias un phishing ngrok no te deja el link debes hacer lo siguiente:

Primero verificaremos si nuestro ngrok si conecta, sino conecta tenemos que instalar de otra forma(ve al menú Tutoriales/Instalación Ngrok)

Bien una ves ya con ngrok funcionando debemos verifica que puerto abre nuestro phishing\033[1;31m¿Cómo lo veo?\033[1;39m pues podemos ver el codigo fuente y verificar que puerto abre para eso:

\033[1;32mcat nombredelphishing.sh

\033[1;39mEso si solo nuestra herramienta no nos muestra el localhost, en herramientas como socialsploit,hiddeneye,phisherman etc si nos muestra el localhost que es algo asi:

\033[1;36mlocalhost:5626

\033[1;39mEn otras herramientas con ShellPhish o Zphisher no nos muestra el localhost, pero si revisamos el codigo fuente veremos que abre puerto 3333 en ambas ocaciones:

\033[1;36mshellphish.sh:\033[1;39mAbre puerto 3333
\033[1;36mzphisher.sh:\033[1;39mAbre puerto 3333
\033[1;36mAIOPhish/SocialSploit:\033[1;39mAbren puerto random, el script te dejara el puerto al costado del localhost:(puerto)

Bien una ves ya sabiendo el puerto y teniendo nuestro ngrok funcionando lo que debemos hacer es crear una nueva ventana, entrar a la carpeta de ngrok y abrir un servidor con el puerto que abre tu phishing\033[1;32m

Ejemplo:
							    
\033[1;36mQuiero hacer phishing con ShellPhish:\033[1;39mEntonces tengo que abrir puerto 3333:

\033[1;32m./ngrok http 3333

\033[1;36mQuiero hacer phishing con AIOPhish/SocialSploit:\033[1;39mEntonces tengo que abrir puerto que me deje el script, ya que en este caso es random:

\033[1;32m./ngrok http tupuerto

\033[1;39mAqui nuestro phising tiene que seguir funcionando es decir esperando los datos de la victima, bien ya abierto el puerto ngrok y una ves conectado nos dejara un link lo copiamos:

\033[1;36mhttp://284aqoks9.ngrok.io\033[1;33m(Ejemplo)

\033[1;39mSolo copiaremos el link no el ":" y el puerto que nos deja al costado.

Haciendo eso enviaremos el link a la victima y esperar los datos :)

\033[1;32mRepetir el proceso cada vez que inicias el phishing.

\033[1;36mNota:\033[1;39m No obstante puedes usar AIOPhish tiene esos errores solucionados, y la capacidad de colocar titulos, fotos, descripción y otras cosas al momento de enviar el link.

""")
