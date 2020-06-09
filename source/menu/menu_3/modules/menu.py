import os
import subprocess
import json
from time import sleep
from .ban import *
from .sys import *

class main:
  def install_tools(self):
    while True:
      tool=tools()
      num=1
      total=len(tool.names)
      print("\007")
      for tool_name in tool.names:
        print (f" \033[01;31m[ \033[01;39m{num} \033[01;31m] \033[01;39m{tool_name}\033[00m")

        num+=1
      print("")
      logo.back()
      cmd=input("\033[1;31mWIKI\033[1;39m-HERRAMIENTAS > \033[00m")
      if cmd=="99" or cmd=="exit":
        self.menu()
        break
      else:
        try:
          if int(cmd)>=1 and int(cmd)<=int(total):
            print("\033[01;33mINSTALANDO...\033[00m")
            tool.install(tool.names[int(cmd)-1])
          else:

            print(f"\007\033\033[1;31m[!]\033[1;39m Opción invalida > \033[00m",cmd)
            sleep(1)
        except ValueError:

          print(f"\033[1;31m[!]\033[1;39m Opción invalida > \033[00m",cmd)
          sleep(1)

  def mss():
    a = input("PRESIONA ENTER PARA CONTINUAR...")

  def category(self):
    while True:
      tool=tools()
      total=len(tool.category)
      num=1
      print("")
      for cat in tool.category:
        print (f"  \033[01;31m[ \033[01;39m{num} \033[01;31m] \033[01;39m{tool.category_data[cat]}\033[00m")

        num+=1
      print("")
      logo.back()
      cmd=input("\033[1;31mHERRAMIENTAS\033[1;39m-CATEGORIAS > \033[00m")
      if cmd=="99" or cmd=="exit":
        self.menu()
        break
      else:
        try:
          if int(cmd) in range(1,int(total)+1):
            while True:
              print(int(cmd)-1)
              print(tool.category[int(cmd)-1])
              cnt=1
              print("")
              tmp_cat_tool=[]
              for i in tool.names:
                if tool.category[int(cmd)-1] in tool.data[i]["category"]:
                  tmp_cat_tool.append(tool.data[i]['name'])
                  print(f" \033[01;31m[ \033[1;39m{cnt} \033[01;31m] \033[01;39m{tool.data[i]['name']}\033[00m")

                  cnt+=1
              print("")
              logo.back()

              tcmd=input("\033[1;31mHERRAMIENTAS\033[1;39m-CATEGORIAS > \033[00m")
              if tcmd=="99" or tcmd=="exit":
                break
              else:
                try:
                  cat_total=len(tmp_cat_tool)
                  if int(tcmd) in range(1,int(cat_total)+1):
                    print("\033[01;32mInstalando....\033[00m")
                    tool.install(tmp_cat_tool[int(tcmd)-1])
                  else:
                    print(f"\007\033[1;31m[!]\033[1;39m Opción invalida > \033[00m",cmd)
                    sleep(1)
                except ValueError:

                  print(f"\007\033[1;31m[!]\033[1;39m Opción invalida > \033[00m",cmd)
                  sleep(1)
          else:

            print(f"\007\033[1;31m[!]\033[1;39m Opción invalida > \033[00m",cmd)
            sleep(1)
        except ValueError:

          print(f"\007\033[1;31m[!]\033[1;39m Opción invalida > \033[00m",cmd)
          sleep(1)

  @classmethod
  def menu(self):
    while True:
      tool=tools()
      system=sys()
      total=len(tool.names)
      logo.menu(total)

      cmd=input("\033[1;31m		   WIKI\033[1;39m-HERRAMIENTAS > \033[00m")
      if cmd == "1":
        self.install_tools(self)
        break
      elif cmd == "2":
        self.category(self)
        break
      elif cmd=="99" or cmd=="exit":
        logo.exit()
        os.system("bash wiki")
        break
      else:

        print(f"\007\033[1;31m		   [!]\033[1;39m Opción invalida > \033[00m",cmd)
        sleep(0.2)
        os.system("clear")
class tools:
  data=None
  names=None
  category=None
  category_data=None
  def __init__(self):
    system=sys()
    with open("source/menu/menu_3/dates/data.json") as data_file:
      self.data=json.load(data_file)
    with open("source/menu/menu_3/dates/cat.json") as cat_file:
      self.category_data=json.load(cat_file)
    self.names=list(self.data.keys())
    self.category=list(self.category_data.keys())

  def install(self,name):
    package_name=self.data[name]["package_name"]
    package_manager=self.data[name]["package_manager"]
    url=self.data[name]["url"]
    req=list(self.data[name]["dependency"])
    system=sys()

    if system.connection:
      if len(req)!=0 and req[0]!=None:
        for dep in req:
          if os.path.exists(system.bin+"/"+dep):
            pass
          else:
            if system.sudo != None:
              os.system(system.sudo+" "+system.pac+" install "+dep+" -y")
            else:
              os.system(system.pac+" install "+dep+" -y")
      if package_manager=="package_manager":
        if os.path.exists(system.bin+"/"+package_name):
          os.system("clear")
          logo.already_installed(name)
          tmp=input("\033[1;33mPRESIONA ENTER PARA CONTINUAR...: \033[00m")
          os.system("clear")
          logo.already_installed(name)
          tmp=input("\033[1;33mPRESIONA ENTER PARA CONTINUAR...: \033[00m")
        else:
          if system.sudo != None:
            os.system(system.sudo+" "+system.pac+" install "+package_name+" -y")
          else:
            os.system(system.pac+" install "+package_name+" -y")

          if os.path.exists(system.bin+"/"+package_name):
            os.system("clear")
            logo.installed(name)
            tmp=input("\033[1;33mPRESIONA ENTER PARA CONTINUAR...: \033[00m")
          else:
            os.system("clear")
            logo.not_installed(name)
            tmp=input("\033[1;33mPRESIONA ENTER PARA CONTINUAR...: \033[00m")

      elif package_manager=="git":
        if os.path.exists(system.home+"/"+package_name):
          os.system("clear")
          logo.not_installed(name)
          tmp=input("\033[1;33mPRESIONA ENTER PARA CONTINUAR...: \033[00m")
        else:
          if system.sudo != None:
            os.system(system.sudo+" git clone "+url+" "+system.home+"/"+package_name)
          else:
            os.system("git clone "+url+" "+system.home+"/"+package_name)
        
          if os.path.exists(system.home+"/"+package_name):
            logo.installed(name)
            tmp=input("\033[1;33mPRESIONA ENTER PARA CONTINUAR...: \033[00m")

          else:
            logo.not_installed(name)
            tmp=input("\033[1;33mPRESIONA ENTER PARA CONTINUAR...: \033[00m")

      elif package_manager=="wget":
        if os.path.exists(system.home+"/"+package_name):
          logo.already_installed(name)
          tmp=input("\033[1;33mPRESIONA ENTER PARA CONTINUAR...: \033[00m")
        else:
          if system.sudo != None:
            os.system(system.sudo+" wget "+url+" -o "+system.home+"/"+package_name)
          else:
            os.system("wget "+url+" -o "+system.home+"/"+package_name)
        
          if os.path.exists(system.home+"/"+package_name):
            logo.installed(name)
            tmp=input("\033[1;33mPRESIONA ENTER PARA CONTINUAR...: \033[00m")
          else:
            logo.not_installed(name)
            tmp=input("\033[1;33mPRESIONA ENTER PARA CONTINUAR...: \033[00m")

      elif package_manager=="curl":
        if os.path.exists(system.home+"/"+package_name):
          logo.already_installed(name)
          tmp=input("\033[1;33mPRESIONA ENTER PARA CONTINUAR...: \033[00m")

        else:
          if system.sudo != None:
            os.system(system.sudo+" curl "+url+" -o "+system.home+"/"+package_name)
          else:
            os.system("curl "+url+" -o "+system.home+"/"+package_name)

          if os.path.exists(system.home+"/"+package_name):
            logo.installed(name)
            tmp=input("\033[1;33mPRESIONA ENTER PARA CONTINUAR...: \033[00m")
          else:
            logo.not_installed(name)
            tmp=input("\033[1;33mPRESIONA ENTER PARA CONTINUAR...: \033[00m")
    else:
      logo.nonet()
      tmp=input("\033[1;33mPRESIONA ENTER PARA CONTINUAR...: \033[00m")

