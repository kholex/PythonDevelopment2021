from tkinter.messagebox import showinfo
import tkinter as tk

def place_parse(a):
    t = a.split('+')
    wh = int(t[-1]) if len(t) > 1 else 0
    if len(t) > 1:
        a = '+'.join(t[:-1])
    t = a.split('.')
    w = int(t[-1]) if len(t) > 1 else 1
    a = int('.'.join(t[:-1])) if len(t) > 1 else int(a)
    return a, w, wh

class Application(tk.Frame):
    def __init__(self, master=None, title="<application>"):
        super().__init__(master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.title(title)
        self.widgets = {}
        self.grid(sticky = 'NEWS')
        self.createWidgets()

    def __getattr__(self, name):
        if name in self.widgets:
            return self.widgets[name]
        widgets = self.widgets

        def _builder(master = self, name = name):
            def builder(Type, a, **kwargs):
                t = a.split('/')
                a = t[0]
                gr = t[1] if(len(t) > 1) else 'NEWS'
                (r, rw, h),(c, cw, w) = \
                    place_parse(a.split(':')[0]), place_parse(a.split(':')[1])
                master.columnconfigure(c, weigh=cw)
                master.rowconfigure(r, weigh=rw)

                class Widget(Type):
                    def __getattr__(self,s_name):
                        s_name = name+'.'+s_name
                        if s_name in widgets:
                            return widgets[name]
                        return _builder(self,s_name)
                widgets[name] = Widget(master, **kwargs)
                widgets[name].grid(row = r, sticky = gr, rowspan = h+1, columnspan = w+1, column = c)
                return widgets[name]
            return builder
        return _builder(name = name)


class App(Application):
    def createWidgets(self):
        self.message = "Congratulations!\nYou've found a sercet level!"
        self.F1(tk.LabelFrame, "1:0", text="Frame 1")
        self.F1.B1(tk.Button, "0:0/NW", text="1")
        self.F1.B2(tk.Button, "0:1/NE", text="2")
        self.F1.B3(tk.Button, "1:0+1/SEW", text="3")
        self.F2(tk.LabelFrame, "1:1", text="Frame 2")
        self.F2.B1(tk.Button, "0:0/N", text="4")
        self.F2.B2(tk.Button, "0+1:1/SEN", text="5")
        self.F2.B3(tk.Button, "1:0/S", text="6")
        self.Q(tk.Button, "2.0:1.2/SE", text="Quit", command=self.quit)
        self.F1.B3.bind("<Any-Key>", lambda event: showinfo(self.message.split()[0], self.message))

app = App(title="Sample application")
app.mainloop()
