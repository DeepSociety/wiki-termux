import os

class logo:
  @classmethod
  def tool_header(self):
    os.system("clear")
    os.system("python source/art/banner3")
    os.system("bash source/.core")
  @classmethod
  def nonet(self):
    print ("")
    print ("\033[1;35m Not_Found")
    print ("")
    print ('''
\033[1;31m  [*]  \033[1;31mNo tienes internet, CONECTATE!!\033[00m''')
    print ("")

  @classmethod
  def already_installed(self,name):
    print(f'''\033[1;32m'{name}'\033[1;32m Ya esta instalado''')

  @classmethod
  def installed(self,name):

    print(f'''\033[1;37m
░░░░░░░░░░▄▄▄▄▄▄▄░░░░░░░░░░
░░░░░░▄▄▀▀░░░░░░░▀▀▄▄░░░░░░
░░░░▄▀░░░░░░░░░░░░░░░▀▄░░░░
░░░▄▀░░░▄▄▄▄▄▄▄▄▄▄▄░░░░█░░░ \033[1;33m '{name}'\033[01;32m Instalado correctamente\033[1;37m
░░█░░▄███████████████▄░░█░░
░█░░▄██▀░▄▄▀███▀▄▄░▀███░░█░
░█░░▀█████████████████▀░░█░
░█░░░░▀▀████████████▀░░░░█░  No olvides leer el archivo README.md para
░░█░░░░░░░░▀▀▀▀▀░░░░░░░▄▀░░  que sepas la funcionalidad del script, y
░░░▀▀▄▄▄▄░░░░░░░░░▄▄▄▀▀░░░░  el proceso de uso.\033[1;37m
░░▄██▀▄▄▄█▀▀▀▀▀▀▀█▄▄▄▀██▄░░
░▄▀██░░░░░▀▀▀▀▀▀▀░░░░░██▀▄░\033[1;32m  cat README.md\033[1;37m
█░░██░░░░░░░░░░░░░░░░░██░░░
█░░██░░░░░░░░░░░░░░░░░██░░█
█░░██░░░░░░░░░░░░░░░░░██░░█
█░░██░░░░░░░░░░░░░░░░░██░░█
█░░██░░░░░░░░░░░░░░░░░██░░█
█░░██▄░░░░░░░░░░░░░░░▄██░░█
▀▀▄█░█▄▄▄▄░░░░░░░▄▄▄▄█░█▄▀▀
░░░░░░░░░█▄▄▄▄▄▄▄█░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░
''')

  @classmethod
  def not_installed(self,name):
    self.tool_header()
    print(f'''
\033[1;33mNo se pudo instalar,\033[1;39m Verifica que \033[1;33m'{name}' no este instalado
''')

  @classmethod
  def back(self):

    print ("\033[01;31m [\033[1;39m 99\033[1;31m ] \033[1;39m Volver al menú\n")

  @classmethod
  def menu(self,total):
    self.tool_header()
    print (f'''
\033[1;31m  		   [\033[1;39m 1\033[1;31m ] \033[1;39m Todas las herramientas.
\033[1;31m  		   [\033[1;39m 2\033[1;31m ] \033[1;39m Categorias.\n
\033[1;31m  		   [\033[1;39m 99\033[1;31m ] \033[1;39m Volver al menú.

''')
  @classmethod
  def exit(self):
    self.tool_header()
    print ('''\033[00m''')

