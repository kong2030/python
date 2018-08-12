#coding=utf-8
import os
import sys
import ConfigParser

class TomcatOps(object):

    def __init__(self,conf_file):
        self.conf_file = conf_file

    ##set tomcat env
    def __setEnv(self):
        config = ConfigParser.ConfigParser()
        config.read(self.conf_file)

        self.JAVA_HOME = config.get("tomcat", "JAVA_HOME")
        self.CATALINA_HOME = config.get("tomcat", "CATALINA_HOME")
        self.CATALINA_BASE = config.get("tomcat", "CATALINA_BASE")
        self.CATALINA_TMPDIR = config.get("tomcat", "CATALINA_TMPDIR")
        self.CATALINA_PID = config.get("tomcat", "CATALINA_PID")
        self.JAVA_OPTS = config.get("tomcat", "JAVA_OPTS")

        self.env_cmd = '''export JAVA_HOME=%s;export CATALINA_HOME=%s;export CATALINA_BASE=%s;export CATALINA_TMPDIR=%s;export CATALINA_PID=%s;export JAVA_OPTS=%s;
                ''' % (self.JAVA_HOME, self.CATALINA_HOME, self.CATALINA_BASE, self.CATALINA_TMPDIR, self.CATALINA_PID, self.JAVA_OPTS)

    ## start the server
    def start(self):
        self.__setEnv()
        start_sh = self.CATALINA_HOME + os.sep + "bin" + os.sep + "startup.sh"
        cmd = self.env_cmd + start_sh
        os.system(cmd)

    ##stop the server
    def stop(self):
        self.__setEnv()
        stop_sh = self.CATALINA_HOME + os.sep + "bin" + os.sep + "shutdown.sh"
        cmd = self.env_cmd + stop_sh
        os.system(cmd)