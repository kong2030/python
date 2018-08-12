#coding=utf-8
import os
import sys
import shutil

##install dir
BASE_DIR = "/home/admin"   ##the base dir of installed software
##BASE_DIR = r"D:\Python"
APP_DIR = BASE_DIR + os.sep + "app"

SERVER_DIR = APP_DIR + os.sep + "servers"
TOMCAT_DIR = APP_DIR + os.sep + "tomcat"
NGINX_DIR = APP_DIR + os.sep + "nginx"
DEPLOYTOOL_DIR = APP_DIR + os.sep + "deploytool"

##software dir
now_dir = os.getcwd()     ##the dir now
deploytool_dir = now_dir + os.sep + "deploytool"
software_dir = now_dir + os.sep + "install"
tomcat_dir = software_dir + os.sep + "tomcat"
nginx_dir = software_dir + os.sep + "nginx"

##install the tomcat
def deployTomcat(appname="tomcat",port=8080,shutdown_port=8005):

    ##copy the software
    if not os.path.exists(TOMCAT_DIR) :
        shutil.copytree(tomcat_dir,TOMCAT_DIR)
        ##unzip the *.tar.gz files
        tar_cmd = "cd %s;ls *.tar.gz | xargs -n1 tar -zxvf" % TOMCAT_DIR
        os.system(tar_cmd)
    if not os.path.exists(DEPLOYTOOL_DIR):
        shutil.copytree(deploytool_dir,DEPLOYTOOL_DIR)

    tomcat_version_dir = ""
    jdk_version_dir = ""
    for dir in os.listdir(TOMCAT_DIR):
        if os.path.isdir(os.path.join(TOMCAT_DIR, dir)):
            if "jdk" in dir :
                jdk_version_dir = TOMCAT_DIR + os.sep + dir
            if "tomcat" in dir :
                tomcat_version_dir = TOMCAT_DIR + os.sep + dir
    if tomcat_version_dir == "" or jdk_version_dir == "" :
        print "can not find software tomcat or jdk"

    ##create instance dir
    instance_dir = SERVER_DIR + os.sep + appname
    if not os.path.exists(instance_dir+os.sep+"conf"):
        shutil.copytree(tomcat_version_dir+os.sep+"conf",instance_dir+os.sep+"conf")
    if not os.path.exists(instance_dir+os.sep+"logs"):
        os.makedirs(instance_dir+os.sep+"logs")
    app_temp = instance_dir+os.sep+"temp"
    if not os.path.exists(app_temp):
        os.makedirs(app_temp)
    if not os.path.exists(instance_dir+os.sep+"work"):
        os.makedirs(instance_dir+os.sep+"work")
    app_webapps = instance_dir+os.sep+"webapps"
    if not os.path.exists(app_webapps):
        os.makedirs(app_webapps)

    ##create server.xml
    config_file = software_dir + os.sep + "config" + os.sep + "tomcat-server.xml"
    tomcat_server_conf = instance_dir+os.sep+"conf" + os.sep + "server.xml"
    with open(config_file) as source:
        contens = source.read()
        contens = contens.replace("$shutdownport",str(shutdown_port)).replace("$port",str(port)).replace("$appBase",app_webapps)
        with open(tomcat_server_conf,"w") as des:
            des.write(contens)

    ##create deploy conf file
    deploy_file = software_dir + os.sep + "config" + os.sep + "tomcat-install.conf"
    instance_deploy_file = DEPLOYTOOL_DIR + os.sep + "conf" + os.sep + appname + ".conf"
    with open(deploy_file) as source:
        contens = source.read()
        contens = contens.replace("$appname",appname).replace("$approotdir",instance_dir).replace("$port",str(port)).replace("$shutdownport",str(shutdown_port))
        contens = contens.replace("$jdk_home",jdk_version_dir).replace("$catalina_home",tomcat_version_dir).replace("$catalina_base",instance_dir).replace("$catalina_temp",app_temp)
        with open(instance_deploy_file,"w") as des:
            des.write(contens)

    print "tomcat installed........"

##install the nginx
def deployNginx(appname="nginx",port=8000):
    print appname,port
    print "nginx installed........."



## main function
if __name__=='__main__':
    print "Please intput your choice(1 or 2): 1.tomcat  2.nginx"
    choice = input()
    if choice == 1 :
        print "installing tomcat ......."
        appname = raw_input("input the appname:")
        port = input("input the port:")
        shutdown_port = input("input the shutdonw port:")
        deployTomcat(appname,port,shutdown_port)
    elif choice == 2 :
        print "installing nginx ........"
        appname = raw_input("input the appname:")
        port = input("input the port:")
        deployNginx(appname,port)
    else :
        print "your choice is error......"
        sys.exit()