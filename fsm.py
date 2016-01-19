
class Message():
    def __init__(self, to="", content=""):
        self.to=to
        self.content=content

class ModuleBase():
    def __init__(self, parent=0):
        self.moduleName=type(self).__name__
        self.moduleNodes={}
        self.parent=parent

    def isMessageToMe(self, message):
        return message.to == self.moduleName

    def isModuleLoaded(self, moduleName):
        return moduleName in self.moduleNodes.keys()

    def doesHaveParent(self):
        return self.parent != 0
    def processMessage(self, message):
        if self.isMessageToMe(message):
            self.handleMessage(message)
        elif self.isModuleLoaded(message.to):
            self.moduleNodes[message.to].processMessage(message)
        elif self.doesHaveParent():
            self.emitMessage(message)
        pass

    def addModule(self, module):
        if not self.isModuleLoaded(module.moduleName):
            module.parent=self
            self.moduleNodes[module.moduleName]= module

    def deleteModule(self, moduleName):
        if self.isModuleLoaded(moduleName):
           del self.moduleNodes[moduleName]

    def handleMessage(self,message):
        pass
    def emitMessage(self, message):
        if self.doesHaveParent():
            self.parent.processMessage(message)


class WriterModule(ModuleBase):
    def __init__(self):
        super(type(self),self).__init__()
    def handleMessage(self, message):
        print("ModuleName: %s Message Header | To: %s Content: %s " % (self.moduleName, message.to, message.content))

class MasterModule(ModuleBase):
    def __init__(self):
        super(type(self),self).__init__()
    def handleMessage(self,message):
        print("Master!!!!")

mm=MasterModule()
wm=WriterModule()
mm.addModule(wm)
msg=Message("WriterModule","DEEDBEEF")
msg2=Message("MasterModule","NVM")
mm.moduleNodes["WriterModule"].processMessage(msg2)
mm.processMessage(msg)
mm.processMessage(msg2)

