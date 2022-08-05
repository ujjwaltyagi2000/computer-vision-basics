# Displaying images in their own separate window outside of Jupyter

'''
While we often just use plt.imgshow() to display images inside of a notebook, 
sometimes we want to use OpenCV on its own to display images in their own

This is because sometimes the video or image analysis becomes really complex,
and often Jupyter (being browser based) interferes with closing the window.

Many times JupyterLab's can display a new window with no issues, but the kernel 
crashes when the OpenCV window is losed.

Kernel error occurs mostly on Linux and Mac systems. If you get the error, simply
run the code as a separate Python script.
'''

import cv2

img=cv2.imread('tony.jpg')

while True:
    
    cv2.imshow('Tony Stark', img)

    if cv2.waitKey(1) & 0xFF==27: #K is always capital in waitKey()
    #If we've waited fpr at least 1 ms AND we've pressed the Esc Key, Break the loop
        break
    
    #Logic Behind the above code:

    #waitkey():

    '''
    waitkey() function of Python OpenCV allows users to display a window for given 
    milliseconds or until any key is pressed. It takes time in milliseconds as a 
    parameter and waits for the given time to destroy the window, if 0 is passed in
    the argument it waits till any key is pressed. 
    '''

    '''
    1.waitKey(0) will display the window infinitely until any keypress 
    (it is suitable for image display).

    2.waitKey(1) will display a frame for 1 ms, after which display will 
    be automatically closed. Since the OS has a minimum time between 
    switching threads, the function will not wait exactly 1 ms, it will 
    wait at least 1 ms, depending on what else is running on your computer 
    at that time.

    So, if you use waitKey(0) you see a still image until you actually press 
    something while for waitKey(1) the function will show a frame for at least 1 ms only.
    '''

    #0xFF

    '''0xFF is a hexadecimal constant which is 11111111 in binary. '''

    #Why the and operation with 0xFF:

    '''
    The waitKey(0) function returns -1 when no input is made whatsoever. As soon the event occurs i.e. a Button is pressed it returns a 32-bit integer.

    The 0xFF in this scenario is representing binary 11111111 a 8 bit binary, since we only require 8 bits to represent a character we AND waitKey(0) to 0xFF. 
    As a result, an integer is obtained below 255.

    ord(char) returns the ASCII value of the character which would be again maximum 255.

    ordchar() is used or ASCII code of any key you want to use to break the loop.

    Hence by comparing the integer to the ord(char) value, we can check for a key pressed event and break the loop.
    
    27 is the ASCII code of Esc, how ASCII code for spacebar is 32
    '''

#cv2.destroyAllWindows()
