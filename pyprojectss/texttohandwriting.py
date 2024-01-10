import pywhatkit as pw
txt="""Right Way to Write Comments ·
 Comments should be short and precise. """


pw.text_to_handwriting(txt,"demo.png",[0,0,138])
print(("end"))
