import textwrap

def textwrapper(text, width):
    wrapper = textwrap.TextWrapper(width=width)
    wrapped_text = wrapper.wrap(text=text)
    line_number=1
    for element in wrapped_text:
        print("Array["+str(line_number)+"] = "'\"'+ element + '\"')
        line_number += 1

textwrapper("To run this program follow below steps, install py locally. Clone this py file & run as shown below python scriptname",20)

#below is other way to assign values to variables and call function passing variables as argument/params
"""
width=20
text = "To run this program follow below steps, install py locally. Clone this py file & run as shown below python scriptname"
func_textwrapper(text,width)
"""
