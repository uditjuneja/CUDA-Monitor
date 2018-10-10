from tkinter import *

root = Tk()

text1 = Text(root, height=40, width=55)
photo=PhotoImage(file='./logo.gif')
text1.insert(END,'\n')
text1.image_create(END, image=photo)

text1.pack(side=LEFT)

text2 = Text(root, height=90, width=200)
scroll = Scrollbar(root, command=text2.yview)
text2.configure(yscrollcommand=scroll.set)
text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
text2.tag_configure('big', font=('Verdana', 20, 'bold'))
text2.tag_configure('color', foreground='#476042', 
						font=('Tempus Sans ITC', 12, 'bold'))
text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END, "Not now, maybe later!"))
text2.insert(END,'\n\t\tMore Information\n', 'big')
quote = """
	The		import signal 
			import threading 

	are  modules that provide the utility to get the GPU monitoring system working.


	GPUtil is a Python module for getting the GPU status from NVIDA GPUs using nvidia-smi.

	Requirements
	CUDA GPU with latest CUDA driver installed. GPUtil uses the program nvidia-smi to get the GPU status of all available CUDA GPUs. 
	nvidia-smi should be installed automatically, when you install your CUDA driver.

	
	Supports both Python 2.X and 3.X.
	And the other requirements -----
	Python libraries:

	subprocess (The Python Standard Library)
	math (The Python Standard Library)
	random (The Python Standard Library)
	time (The Python Standard Library)
	os (The Python Standard Library)
	sys (The Python Standard Library)
	Tested on CUDA driver version 390.77 Python 2.7 and 3.5.
"""
text2.insert(END, quote, 'color')
text2.insert(END, '\n', 'follow')
text2.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)

root.mainloop()