import os

print("""
\033[1;32m
PAQUETES NECESARIOS:
\033[1;39m
pkg install nano -y
\033[1;33m

\033[1;35mCOLORES:\033[1;39m
""")
os.system("cat source/menu/menu_13/.colores")
print("""
\033[1;33mFUNCIONES:\033[1;39m
""")
os.system("cat source/menu/menu_13/.funk")
print("""
\033[1;32mPROCEDIMIENTO:
\033[1;36m
Primero entraremos a la carpeta etc para modificar el archivo bash.bashrc:
\033[1;39m
cd /data/data/com.termux/files/usr/etc
\033[1;36m
Aqui eliminaremos el archivo motd:
\033[1;39m
rm motd
\033[1;36m
Abrimos el archivo bash.bashrc:
\033[1;39m
nano bash.bashrc
\033[1;36m
Aqui buscaremos una variable llamada PS1
\033[1;39m
La tendremos que modificar por defecto te viene un $ le puedes añadir colores, funciones etc, Puedes agregar cualquier palabra que quieras, color o función:

\033[1;33mEjemplo:
\033[1;39m
PS1='\n \e[1;36m>>\e[1;32mTunombre\e[1;35m@\e[1;33mtermux\e[1;36m<<\e[1;32m [\e[1;33m \d\e[1;32m]\e[1;32m [\e[1;33m\t \e[1;32m] 
|\e[1;31m[\e[1;33m \s \h \e[1;31m]
|__\e[1;31m[\e[1;33m \w \e[1;31m]
|
\e[1;31m|__\e[1;31m[\e[1;36m # \e[1;31m]\e[1;39m '
\033[1;32m""")
os.system("cat source/menu/menu_13/.func")
print("""
\033[1;39mCuando terminemos presionamos CTRL+x y posteriormente damos a y

Abrimos nueva ventana y ya tendriamos modificado nuestra entrada de comandos.
""")

