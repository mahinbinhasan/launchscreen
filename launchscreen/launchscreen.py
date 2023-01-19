"""
This module implements the main functionality of MahinLaunchScreen.
Author: MAHIN BIN HASAN
YouTube: https://www.youtube.com/c/AlMahin
Github: https://github.com/mahinbinhasan
Facebook: https://facebook.com/root.mahin
"""

__author__ = "Mahin Bin Hasan"
__email__ = "allmahin149@gmail.com"
__status__ = "planning"
class screen:
    def screen(image,deltime):
        from tkinter import PhotoImage,Tk,Canvas
        import time


        wel =Tk()
        bgr = PhotoImage(file=image)
        wel.configure(bg='black')
        wel.wm_overrideredirect(True) 
        wel.wm_attributes("-transparentcolor",'black')
        w =bgr.width() # width for the Tk wel
        h = bgr.height() # height for the Tk wel
        ws = wel.winfo_screenwidth() # width of the screen
        hs = wel.winfo_screenheight() # height of the screen

        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        wel.geometry('%dx%d+%d+%d' % (w, h, x, y))

        maincan = Canvas(wel,width=800,height=378,bd=0,highlightthickness=0,bg='black')
        maincan.pack(fill="both",expand=True)
        maincan.create_image(0,0,image=bgr,anchor="nw")
        wel.after(deltime,lambda:wel.destroy())

        wel.mainloop()
class help:
    def commands():
        p="""
        Usage: 
        from launchscreen import screen
        screen.screen('download.png')
        """
        return p