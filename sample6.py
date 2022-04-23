from tkinter import *
from tkhtmlview import *
# create tk instance
root = Tk()
# set window geometry
root.geometry('400x400')
# set window title
root.title('HTML in tkinter')
# write text with html tags
html_text = '''
<h3 style="color:gold2; background-color:black; text-align:center">
HTML View in Tkinter
</h3>
<p style="text-align: left;">
<b>tkhtmlview</b> is a <u>collection of tkinter widgets</u>
whose text can be set in HTML format.<br>
<b>Heading tags</b>
<ol type="1">
<li>h1</li>
<li>h2</li>
</ol>
</p>
'''
# create HTMLLabel
label = HTMLLabel(root, html=html_text)
label.pack(pady=15, padx=15, fill=BOTH)
root.mainloop()