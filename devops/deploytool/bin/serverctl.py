#!/usr/bin/python
#coding=utf-8
import sys
import os
import ConfigParser

sys.path.append("..")
from lib.TomcatOps import *





if __name__=='__main__':
    if len(sys.argv) != 3 :
        print "the args should like (appname action): tm_omm start"
    else :
        appname = sys.argv[1]
        action = sys.argv[2]
        ##the server conf file
        conf_file = os.path.abspath('..') + os.sep + "conf" + os.sep + appname + ".conf"
        if not os.path.exists(conf_file):
            print "can not find install conf file,please check:"
            print "conf_file:",conf_file
        else :
            config = ConfigParser.ConfigParser()
            config.read(conf_file)
            server_type = config.sections()[0]
            if server_type == "tomcat" :
                ops = TomcatOps(conf_file)
                if action == "start" :
                    print action
                    ops.start()
                elif action == "stop" :
                    print action
                    ops.stop()
                else:
                    print "can not find this action, please check...."

            if server_type == "nginx" :
                print "nginx"