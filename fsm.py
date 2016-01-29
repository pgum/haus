class Message():
    def __init__(self, to="", content=""):
        self.recipient=to
        self.content=content

class ModuleBase():
    def __init__(self, parent=0):
        self.name=type(self).__name__
        self.moduleNodes={}
        self.parent=parent

    def isMessageToMe(self, message):
        return self.name[:len(message.recipient)]==message.recipient

    def haveSubmodule(self, name):
        return name in self.moduleNodes.keys()

    def haveParent(self):
        return self.parent != 0

    def processMessage(self, message):
        if self.isMessageToMe(message):
            self.handleMessage(message)
        elif self.haveSubmodule(message.recipient):
            self.moduleNodes[message.recipient].processMessage(message)
        elif self.haveParent():
            self.emitMessage(message)
        pass

    def addModule(self, module):
        if not self.haveSubmodule(module.name):
            module.parent=self
            self.moduleNodes[module.name]= module

    def addModuleByType(self, moduleName):
        try:
            self.addModule(globals()[moduleName]())
        except KeyError as e:
            pass

    def deleteModule(self, name):
        if self.haveSubmodule(name):
           del self.moduleNodes[name]

    def deleteAllModules(self):
        for module in self.moduleNodes.keys():
            self.deleteModule(module)

    def handleMessage(self,message):
        pass
    def parseMessage(self,message):
        pass

    def emitMessage(self, message):
        if self.haveParent():
            self.parent.processMessage(message)
        else:
            self.processMessage(message)

    def forwardMessage(self, message, recipient):
        message.recipient=recipient
        self.emitMessage(message)

    def writeToDebug(self, message):
        self.forwardMessage(message, "WriterModule")

class WriterModule(ModuleBase):
    def __init__(self):
        super(WriterModule,self).__init__()
    def handleMessage(self, message):
        print("ModuleName: %s Message Header | To: %s Content: %s " % (self.name, message.recipient, message.content))

import simplejson as json

class MasterModule(ModuleBase):
    def __init__(self):
        super(MasterModule,self).__init__()

    def parseMessage(self, message):
        try:
            msg=json.loads(message.content)
            if msg["action"] == "add":
                self.addModuleByType(msg["mName"])
            elif msg["action"] == "delete":
                self.deleteModule(msg["mName"])
            else:
                print("wtf?!")
        except json.JSONDecodeError as e:
            print("bez akcji: %s" %(message.content))

    def handleMessage(self,message):
        self.writeToDebug(message)
        self.parseMessage(message)
