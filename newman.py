# ============================================
# Auther: C C Sreenidhin
# Company: Audrey Technologies
# Project: Music Analyser
# Date:01-09-2017
# ============================================

#import modules
#=============================================
import Tkinter, ttk, tkFileDialog
#=============================================
from links import *
from analy import *

#=============================================

#Create a class for the UI and its objects
class musicAnalyser(Frame):

  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.master = master
    master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth()-3, master.winfo_screenheight()-3))
    self.grid()
    master.title("Music Analyser")

    master.rowconfigure(0, pad=3)
    master.columnconfigure(0, pad=3)
    master.columnconfigure(1, weight=1)

    #Music player display frame
    frame1 = Frame(master, bd=2, bg="black")
    frame1.grid(row = 0, column = 0, sticky = "ns")

    #Analysis and result Frame
    frame2 = Frame(master, bd=2, relief=SUNKEN)
    frame2.grid(row = 0, column = 1, sticky = W+E+N+S)

    #row and column configure frame1
    frame1.columnconfigure(0, pad=3)
    frame1.columnconfigure(1, pad=3)
    frame1.columnconfigure(2, pad=3)
    frame1.columnconfigure(3, pad=3)
    frame1.columnconfigure(4, pad=3)

    frame1.rowconfigure(0, pad=3)
    frame1.rowconfigure(1, pad=3)
    frame1.rowconfigure(2, pad=3)
    frame1.rowconfigure(3, pad=3, weight = 1)

    #row and column configure
    frame2.columnconfigure(0, pad=3)
    frame2.columnconfigure(1, pad=3)
    frame2.columnconfigure(2, pad=3)
    frame2.columnconfigure(3, pad=3)
    frame2.columnconfigure(4, pad=3)

    frame2.rowconfigure(0, pad=3)
    frame2.rowconfigure(1, pad=3)
    frame2.rowconfigure(2, pad=3)
    frame2.rowconfigure(3, pad=3, weight = 1)

    #display ui
    labackground = PhotoImage(file="icons/background.gif")
    canvas=Canvas(frame1, height=100, bg='skyblue')
    canvas.grid(row=0, columnspan = 5, sticky=EW)
    canvas.image=labackground
    canvas.create_image(0, 0, anchor="nw", image=labackground)
    time_display=canvas.create_text(10, 25, anchor="nw", fill='cornsilk', text = "Music Analyser")
    song_display=canvas.create_text(220,40, anchor="nw", fill='cornsilk', text = "by: Sreenidhin C C")
    song_duration=canvas.create_text(220,65, anchor="nw", fill='cornsilk', text = "Audrey Technologies")

    #control UI
    pauseicon=PhotoImage(file="icons/pause.gif")
    pausebutton = Button(frame1, image=pauseicon, command=pausesong)
    pausebutton.image = pauseicon
    pausebutton.grid(row=1, column=0, sticky=E)
    previous_icon=PhotoImage(file="icons/previous.gif")
    previous_button = Button(frame1, image=previous_icon, command=prevsong)
    previous_button.image = previous_icon
    previous_button.grid(row=1, column=1, sticky=E)
    playicon=PhotoImage(file="icons/play.gif")
    playbutton = Button(frame1, image=playicon, command=playsong)
    playbutton.image = playicon
    playbutton.grid(row=1, column=2, sticky=E)
    next_icon=PhotoImage(file="icons/next.gif")
    next_button = Button(frame1, image=next_icon, command=nextsong)
    next_button.image = next_icon
    next_button.grid(row=1, column=3, sticky=E)
    stopicon=PhotoImage(file="icons/stop.gif")
    stopbutton = Button(frame1, image=stopicon, command=stopsong)
    stopbutton.image = stopicon
    stopbutton.grid(row=1, column=4, sticky=E)

    #Listbox for Playlist from directory choosen
    musiclistcanvas=Canvas(frame1, bg='#333')
    musiclistcanvas.grid(row=3, columnspan = 5, sticky=E+W+N+S)
    musiclistbox = Listbox(musiclistcanvas, height=31, width=51)
    musiclistbox.grid(row=3, sticky="ew", padx=7, pady=5)



    #Link scrollbar to canvas
    vertscrollbar =Scrollbar(musiclistcanvas, orient="vertical", command=musiclistcanvas.yview)
    vertscrollbar.grid(row=3, column=5, sticky='ns')
    musiclistcanvas.configure(yscrollcommand=vertscrollbar.set)



    #button for Adding Source Directory
    selectSource = Button(frame1, text="Add Source Directory", command=lambda: setlistbox(musiclistbox))
    selectSource.grid(row=2, columnspan=5, sticky=EW)
    print("hello")


    #button to start classification
    startclassifyButton = Button(frame2, text="Start Collecting", command = classifier)
    startclassifyButton.grid(row = 0, column = 1 )

    #button to select Destination
    selectDestination = Button(frame2, text="Add Destination Directory", command = destchooser)
    selectDestination.grid(row = 0, column = 0)

    #button to select trainingset
    trainselbutton = Button(frame2, text="Add Training Set Directory", command = choosetrainingsetdir)
    trainselbutton.grid(row = 1, column = 0)

    #button to select testset
    testselbutton = Button(frame2, text="Add Test Set Directory", command = choosetestdir)
    testselbutton.grid(row = 1, column = 1 )


    #button to start predict on test set
    predictbutton = Button(frame2, text="Start Prediction", command = lambda: startpred(tree))
    predictbutton.grid(row = 1, column = 2)


    #button to display graph
    graphbutton = Button(frame2, text="Show Graph", command = dispgraph)
    graphbutton.grid(row = 1, column = 3)

    #To create a treeview (table of 2 columns)
    tree = ttk.Treeview(frame2)
    tree['show'] = 'headings'
    tree["columns"]=("title","genre")
    tree.column("genre", width=100)
    tree.heading("genre", text="Predicted Genre")
    tree.heading("title", text="Title")

    tree.grid(row = 2, columnspan = 5, rowspan =4, padx = 10, pady = 30, sticky = N+S+E+W)


def main():

    global listofsongs, realnames, index, pause, title, directory
    global genre, musiclistbox, tree
    root = Tk()
    app = musicAnalyser(root)

    root.mainloop()


if __name__=='__main__':
    main()
