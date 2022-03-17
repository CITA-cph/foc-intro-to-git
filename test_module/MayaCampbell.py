class testOSCClass():
    def __int__(self):
        self.ip = "192.168.0.1"
        self.port = 2788
        self.clientName = "OSC1"
        self.msgContents = "'/test/me', None, ['text', 672, 8.871]"
        
        def function(self):
            osc_send(self.msgContents, self.cilentName)
        
        if __name__=="__main__":
            print("hello")
            pass