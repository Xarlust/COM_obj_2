class HelloWorld:
    _reg_clsid_ = "{7CC9F362-486D-11D1-BB48-0000E838A65F}"
    _reg_desc_ = "Python Test COM Server"
    _reg_progid_ = "Python.TestServer"
    _public_methods_ = ['Hello']
    _public_attrs_ = ['softspace', 'noCalls']
    _readonly_attrs_ = ['noCalls']

    def __init__(self):
        self.softspace = 1
        self.noCalls = 0

    def Hello(self, who):
        self.noCalls = self.noCalls + 1
        return "Hello" + " " * self.softspace + who

if __name__=='__main__':
    import win32com.server.register
    print("Going to register...")
    win32com.server.register.UseCommandLine(HelloWorld)

# в excel процедуру для проверки
#Sub d()
#    Set obj = CreateObject("Python.TestServer")
#    MsgBox obj.Hello("joe")
#End Sub
