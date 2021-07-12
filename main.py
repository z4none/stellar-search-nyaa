import os
import sys
import StellarPlayer
import threading
import time

from .simple import Simple

class Plugin(StellarPlayer.IStellarPlayerPlugin):
    def __init__(self, player:StellarPlayer.IStellarPlayer):
        super().__init__(player)
        self.simple = Simple(player)    

    def handleRequest(self, method, args):
        if hasattr(self.simple, f"on_{method}"):
            getattr(self.simple, f"on_{method}")(args)

    def start(self):
        print("plugin start")
        if hasattr(self.simple, 'start'):
            print("simple start")
            self.simple.start()

    def stop(self):
        super().stop()
        if hasattr(self.simple, 'stop'):
            self.simple.stop()
        print("plugin stop")

def newPlugin(player:StellarPlayer.IStellarPlayer,*arg):
    return Plugin(player)

def destroyPlugin(plugin:StellarPlayer.IStellarPlayerPlugin):
    plugin.stop()

