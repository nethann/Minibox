#module import
from tkinter import *
from tkinter import messagebox
import time
import tkinter
from tkinter import font
from colorama.ansi import Fore 
import pyautogui 
import random 
import webbrowser

from time import strftime
from datetime import date
import colorama
from colorama import Style
from PIL import ImageTk, Image
import requests

#loop checkbutton window
def main():
    #add these fx colors 
    colors = [
        "#57697a",
        "#3d4955",
        "#2C2F32",
        "#3C434E",
        "#46515A"
    ]


    #randonmizes the colors 
    r = random.choice(colors)

    
    root = Tk()
    root.title('Minibox')
    root.geometry('800x570')
    root.resizable(TRUE,TRUE)
    root.config(bg = r)
    root.eval('tk::PlaceWindow . center')


    #clears the root 
    def clear():
        frame.quit



    frame = Frame(root)
    frame.pack()
    frame.config(bg = r)
    #remove this if have problems in the future with placement of the menu

    def gmail_window():    
        mail_window = Frame(root)
        mail_window.pack()
        mail_window.config(bg = r)
        mail_window.place(relx=0.5, rely=0.4, anchor="c")
        frame_title = Label(mail_window, text="Discord Menu", font = "Ariel 45", fg = "white", bg = r).pack(pady=20)
        #Don't delete this
        value_inside = tkinter.StringVar(mail_window)


        #mails list
        choices = [
            #A day#
            'Gmail Spammer'
        ]

        def destroy_gmail_win():
            mail_window.destroy()

        def clear():
            root.destroy()


        #clears windows 
        def clear_mail_option():
            mail_window.quit()



        #gmail option menu
        value_inside.set('Choose your choice')
        discord_class = LabelFrame(mail_window, text = "Discord Choices:", fg = "white", font = "Ariel 15",  bg = r)  
        discord_class.pack(fill="both", expand = "yes")
        #_____#
        option = tkinter.OptionMenu(discord_class, value_inside,*choices)
        option.pack()
        option.config(background=r)

        discord_open_btn = Checkbutton(mail_window, text = 'Open', font = "Ariel 17", fg = "white", bg = r, command=lambda:[destroy_gmail_win(),mail_win_func()])
        discord_open_btn.pack(pady=10)

        discord_back_btn_window = Checkbutton(mail_window, text = 'back', font = "Ariel 17", fg = "white", bg = r, command=lambda:[clear(),clear_mail_option(),main()])
        discord_back_btn_window.pack()

        def mail_win_func():
            #If gmail spammer chose
            if value_inside.get() == 'Gmail Spammer':
                root.geometry('800x690')
                root.resizable(TRUE,TRUE)
                root.config(bg = r)
                gmail_spammer_frame = Frame(root)
                gmail_spammer_frame.pack()
                gmail_spammer_frame.config(bg = r)
                frame_title = Label(gmail_spammer_frame, text="Gmail Spammer", font = "Ariel 45", fg = "white", bg = r).pack(pady=10)

                Repeat_times = LabelFrame(gmail_spammer_frame, text = 'How many times to repeat:',fg = "white", bg=r, font = "Ariel 15")
                Repeat_times.pack(pady=15)

                #________#

                #user input string variable
                repeat_entry_str = IntVar()

                #times repeat entry
                repeat_entry = Entry(Repeat_times, border=0, borderwidth=0, width=5, textvariable=repeat_entry_str)
                repeat_entry.pack()

                #______________#

                sender_name_frame = LabelFrame(gmail_spammer_frame, text = 'Who do you want to send to?:',fg = "white", bg=r, font = "Ariel 15")
                sender_name_frame.pack()

                #sender name stringvar
                sender_name_str = StringVar()
                
                #sender name input
                sender_name_entry = Entry(sender_name_frame, border=0, borderwidth=0, width=25, textvariable=sender_name_str)
                sender_name_entry.pack()


                underline_2 = Label(gmail_spammer_frame, text = '>>>>>______________________________<<<<<', fg = 'white', bg = r, font='Ariel 20 bold').pack(pady=10)



                #______________#

                subject_frame = LabelFrame(gmail_spammer_frame, text = 'Subject:',fg = "white", bg=r, font = "Ariel 15")
                subject_frame.pack(pady=5)

                #subject string variable
                subject_str = StringVar()
                
                #subject line info
                subject_entry = Entry(subject_frame, border=0, borderwidth=0, width=35, textvariable=subject_str)
                subject_entry.pack()


                #______________#

                information_frame = LabelFrame(gmail_spammer_frame, text = 'Information:',fg = "white", bg=r, font = "Ariel 15")
                information_frame.pack()

                #information stringvariable
                information_str = StringVar()
                
                #information below
                file_information = Text(information_frame, border=0,borderwidth=0,width=65,height=20,fg = "black")
                file_information.pack()


                def function_mail_spammer():


                    #repeat entry defining
                    repeat_entry_str = repeat_entry.get()

                    #sender name string defining
                    sender_name_str = sender_name_entry.get()

                    #subject defining
                    subject_str = subject_entry.get()

                    #text information
                    information_str = file_information.get(1.0,  "end-1c")


                    webbrowser.open('https://gmail.com')
                    #for loop
                    for i in range(0,int(repeat_entry_str)):
                        #pg start
                        #sleep 1 second
                        time.sleep(2)
                        #press c to compose
                        pyautogui.press('c')
                        time.sleep(2)
                        #gmail name typer
                        pyautogui.typewrite(str(sender_name_str))
                        pyautogui.press('tab')
                        pyautogui.press('tab')
                        #subject line typer
                        pyautogui.typewrite(str(subject_str))
                        pyautogui.press('tab')
                        #information typer
                        pyautogui.typewrite(str(information_str))
                        #submit btn
                        pyautogui.press('tab')
                        pyautogui.press('enter')


                    

                #______________#

                #submit
                post = Button(gmail_spammer_frame, text = 'Post', fg = 'black', bg = r, font = 'Ariel 17', command=lambda:[function_mail_spammer()])
                post.pack(pady=10)

                back = Checkbutton(gmail_spammer_frame, text = 'Back', fg = 'white', bg = r, font = 'Ariel 17', command=lambda:[clear(),  main()])
                back.pack()







        #mainloops
        mail_window.mainloop()



    def discord_window():

        root.geometry('800x570')
        root.resizable(TRUE,TRUE)
        root.config(bg = r)
        discord_window = Frame(root)
        discord_window.pack()
        discord_window.config(bg = r)
        discord_window.place(relx=0.5, rely=0.4, anchor="c")
        frame_title = Label(discord_window, text="Discord Menu", font = "Ariel 45", fg = "white", bg = r).pack(pady=20)
        value_inside = tkinter.StringVar(discord_window)


        #classes list
        choices = [
            #A day#
            'Request Discord Bot'
        ]

        def clear():
            discord_window.destroy()
            

        def option_menu_func():
            if value_inside.get() == 'Request Discord Bot':
                root.geometry('800x570')
                root.resizable(TRUE,TRUE)
                root.config(bg = r)
                requirest_discord_window = Frame(root)
                requirest_discord_window.pack()
                requirest_discord_window.config(bg = r)
                frame_title = Label(requirest_discord_window, text="Request Discord", font = "Ariel 45", fg = "white", bg = r).pack(pady=10)

                #request URL
                request_url = LabelFrame(requirest_discord_window, text = "Type Request URL: ", fg = "white", bg=r, font = "Ariel 15")  
                request_url.pack(fill="both", expand = "yes")

                def work_field():
                    request_url_get = request_url.get()
                    #header auth
                    header_authorization_get = header_authorization.get()

                    information = file_information.get(1.0,  "end-1c")

                    print(request_url_get)
                    print(header_authorization_get)
                    print(information)

                    payload = {
                        'content': str(information)
                    }

                    header = {
                        'authorization': str(header_authorization_get)
                    }

                    req = requests.post(str(request_url_get), data = payload, headers=header)



                def clear():
                    requirest_discord_window.destroy()

                def root_destroy():
                    root.destroy()

                def mn():
                    print("insert main")

                def discord_flie_sv():
                    request_url_get = request_url.get()

                    header_authorization_get = header_authorization.get()

                    file = open("Discord File", 'w')
                    file.write("______Discord file information save______")
                    file.write("\n Requests: " + str(request_url_get))
                    file.write("\n Authorization: " + str(header_authorization_get))
                    file.close()


                #string var
                request_url_get = StringVar()
                request_url = Entry(request_url, bg = 'white', fg = "black", border=0, borderwidth=0, width=55, textvariable=request_url_get)
                request_url.pack()

                header_authorization_frm = LabelFrame(requirest_discord_window, text = "Type Header Authorization: ", fg = "white", bg=r, font = "Ariel 15")  
                header_authorization_frm.pack(fill="both", expand = "yes", pady=10)

                header_authorization_get = StringVar()
                header_authorization = Entry(header_authorization_frm, bg = 'white', fg = "black", border=0, borderwidth=0, width=50, textvariable=header_authorization_get)
                header_authorization.pack()

                information_frm = LabelFrame(requirest_discord_window, text = "Type Header Authorization: ", fg = "white", bg=r, font = "Ariel 15")  
                information_frm.pack(fill="both", expand = "yes", pady=10)

                information = StringVar()
                file_information = Text(information_frm, border=0,borderwidth=0,width=70,height=15,fg = "black")
                file_information.pack()

                #___# ab
                sbt = Checkbutton(requirest_discord_window, text = 'Submit', fg = 'white', bg = r, font = 'ariel 17',command = lambda:[work_field()])
                sbt.pack(pady=5)


                txt_file = Button(requirest_discord_window, text = 'Text file', fg = 'black', bg = r, font = 'ariel 17',command = lambda:[discord_flie_sv()])
                txt_file.pack(pady=5)


                bck_btn = Button(requirest_discord_window, text = 'back', bg = r, fg = 'black', font = 'ariel 17',command=lambda:[clear(), root_destroy(),main()])
                bck_btn.pack(pady=2)

            

            
                

        #setting the title of the option menu
        def root_destroy():
            root.destroy()

        value_inside.set('Choose your choice')
        discord_class = LabelFrame(discord_window, text = "Discord Choices:", fg = "white", font = "Ariel 15",  bg = r)  
        discord_class.pack(fill="both", expand = "yes")
        #_____#
        option = tkinter.OptionMenu(discord_class, value_inside,*choices)
        option.pack()
        option.config(background=r)

        discord_open_btn = Checkbutton(discord_window, text = 'Open', font = "Ariel 17", fg = "white", bg = r, command=lambda:[clear(),option_menu_func()])
        discord_open_btn.pack(pady=10)

        discord_back_btn_window = Checkbutton(discord_window, text = 'back', font = "Ariel 17", fg = "white", bg = r, command=lambda:[clear(),root_destroy(),main()])
        discord_back_btn_window.pack()
        #_____#

        root.mainloop()


    def text_file():
        root.geometry('800x610')
        root.resizable(TRUE,TRUE)
        root.config(bg = r)

        frame_text_file = Frame(root)
        frame_text_file.pack()
        frame_text_file.config(bg = r)

        def file_save():
            input_field_file_name = filename_entry.get()
            information = file_information.get(1.0,  "end-1c")

            file = open(str(input_field_file_name), 'w')
            file.write(str(information))
            file.write("")
            file.close()

        def clear_frame_text_file():
            frame_text_file.destroy()
            root.destroy()

        text_file_logo = Label(frame_text_file, text="Text File Creation", font = "Ariel 35", bg = r, fg = "white").pack(pady=10)

        #file_name lbl frame for naming file
        file_name = LabelFrame(frame_text_file, text = "Enter file name below:", fg = "white", bg=r, font = "Ariel 15")  
        file_name.pack(fill="both", expand = "yes", pady=20)

        #creating file name (input)
        input_field_file_name = StringVar()
        filename_entry = Entry(file_name, textvariable=input_field_file_name, border=0,borderwidth=0,fg = "black")
        filename_entry.pack(pady=10)

        #text input for file
        file_txt = LabelFrame(frame_text_file, text = "Type your text:", fg = "white", bg=r, font = "Ariel 15")  
        file_txt.pack(fill="both", expand = "yes", pady=10)

        #string var for text input (information)
        information = StringVar()
        file_information = Text(file_txt, border=0,borderwidth=0,width=95,height=22,fg = "black")
        file_information.pack()


        #checkbutton to create the file
        create_btn = Checkbutton(root, text= 'Create', fg = 'white', bg = r, font = 'Ariel 17', command=lambda:[file_save()])
        create_btn.pack(pady=5)

        #back button to go back to the main menu 
        back_btn = Button(root, text = 'Back', font = 'Ariel 17', borderwidth=0, border=0, fg = 'black', bg = r, command=lambda:[clear_frame_text_file(), main()])
        back_btn.pack(pady=5)



        frame_text_file.mainloop()


    def web_search():
        root.geometry('800x600')
        root.title("Web Search Window")
        root.resizable(TRUE,TRUE)
        root.config(bg = r)

        frame_scrape = Frame(root)
        frame_scrape.pack()
        frame_scrape.config(bg = r)

        #webbing def 
        def webbing():
            #question webentry.getting info 
            question = web_entry.get()

            print(Fore.RED + "Searching for " + question)

            #adding str to webrowser
            webbrowser.open(str(question))

        def win_quit():
            root.quit()

        def root_clear():
            root.destroy()


        loop_autotype = Label(frame_scrape, text="Web Search", font = "Ariel 35", bg = r, fg = "white").pack(pady=10)

        web_open = LabelFrame(frame_scrape, text = "Search webrowser:", fg = "white", bg=r, font = "Ariel 15")  
        web_open.pack(fill="both", expand = "yes", pady=20)

        question = StringVar()
        web_entry = Entry(web_open, bg = "white", fg = "black",border=0, borderwidth=0, width=55,textvariable=question)
        web_entry.pack(pady=5)

        web_search = Button(web_open,text = "Visit", bg=r, fg="black", font = "Ariel 17", command=lambda:[webbing()])  
        web_search.pack(pady=20)


        #getting value as string var and connecting to frame_scrape
        value_inside = tkinter.StringVar(frame_scrape)

        #classes list
        choices = [
            #A day#
            'Rec Games',
            'Computer Applications',
            'Study Skills',
            'AP Language',
            '______________________',
            #B day#
            'Biology',
            'Algebra II',
            'US History',
            'Music Appreciation'

        ]
        #setting the title of the option menu
        value_inside.set('Choose one of the classes below')



        web_classes = LabelFrame(frame_scrape, text = "Classes Open:", fg = "white", bg=r, font = "Ariel 15")  
        web_classes.pack(fill="both", expand = "yes")

        #_____#
        option = tkinter.OptionMenu(web_classes, value_inside,*choices)
        option.pack()
        option.config(bg = r)
        #_____#

        #callback function 
        def callback():
            #_____ A Day _____ #
            if value_inside.get() == 'Rec Games':
                webbrowser.open('https://zoom.us/j/99380972509?pwd=SHVUaXcwTWMzb0duUlVLdVlITTZBdz09')
            
            if value_inside.get() == 'Computer Applications':
                messagebox.showerror(title = 'error', message='This is a asynchronous class')

            if value_inside.get() == 'Study Skills':
                webbrowser.open('https://zoom.us/j/98553474849?pwd=REsrd0hkblgvVkRZRmNaWkp2Z2U4QT09')

            if value_inside.get() == 'AP Language':
                messagebox.showerror(title = 'error', message='This is a asynchronous class')


            #_____ B Day _____ #
            if value_inside.get() == 'Biology':
                webbrowser.open('https://zoom.us/j/92209323190?pwd=R213U2RSclZMaVFsZC9adDJLUDhGZz09')
            
            if value_inside.get() == 'Algebra II':
                webbrowser.open('https://zoom.us/j/98462296110?pwd=QXVPalFqKzl1eXVHbzFrWWxGWVl6Zz09')

            if value_inside.get() == 'US History':
                webbrowser.open('https://zoom.us/j/95464865295?pwd=SVBBbk8wTlAxUGNjbHFzbVF3VHRuQT09')

            if value_inside.get() == 'Music Appreciation':
                messagebox.showerror(title = 'error', message='This is a asynchronous class')



        webrowser_classes_open = Checkbutton(web_classes,text = "Open", bg=r, fg="white", font = "Ariel 17", command=lambda:[callback()])  
        webrowser_classes_open.pack(pady=5)  



        #add code above this ^
        web_back_btn = Button(frame_scrape,text = "Back", bg=r,fg="black", font = "Ariel 17", command=lambda:[root_clear(),win_quit(),main()])  
        web_back_btn.pack(pady=10)  



        root.mainloop()
      


    def loop_win1():
        print(Fore.GREEN + "While Loop clicked")

        root.geometry('800x570')
        root.resizable(TRUE,TRUE)
        root.config(bg = r)

        frame_2 = Frame(root)
        frame_2.pack()
        frame_2.config(bg = r)
        frame_2.place(relx=0.5, rely=0.4, anchor="c")

        #clears frame 2
        def clear_frame2():
            frame_2.destroy()

        #autotype text def
        def autotype_text():
            print(Fore.GREEN + "autotyoe_text chosen")

            #root def
            root.geometry('800x480')
            root.resizable(TRUE,TRUE)
            root.config(bg = r)

            
            frame_3 = Frame(root)
            frame_3.pack()
            frame_3.config(bg = r)

            def clear_frame3():
                frame_3.destroy()


            #entry range for the outputs
            def entry_range_pyautogui_txt():

                #entry statement.get
                statement = entry.get()

                time_var = lbl_frame_time_wait.get()

                #gets both the statements
                statement_2 = lbl_frame_typewrite_config_1.get()
                statement_3 = lbl_frame_typewrite_config_2.get()

                #prints both the statements for @debug
                print(statement_2)
                print(statement_3)

                messagebox.showinfo(title = "information", message = "Autotyper will start in 5 seconds")

                #time.sleep for each         
                time.sleep(5)
                for i in range(int(statement_2), int(statement_3)):
                    pyautogui.typewrite(str(statement))
                    pyautogui.press('enter')
                    time.sleep(int(time_var))


            #clearing the input
            def clear_entry():
                entry.delete(0, END)
                entry.delete(0.0, END)


            #Label for autotype text
            loop_autotype = Label(frame_3, text="Autotype Text", font = "Ariel 35", bg = r, fg = "white").pack()

            #label frame for how many times want to repeat
            labelframe_typewrite = LabelFrame(frame_3, text="Type how many times to repeat:", font = "Ariel 15", bg = r, fg = "white")  
            labelframe_typewrite.pack(fill="both", expand = "yes")  

            #string varialbe for the range (how many times want to do)
            statement_2 = IntVar()
            statement_3 = IntVar()
            lbl_frame_typewrite_config_1 = Entry(labelframe_typewrite, bg = "white", fg = "black",border=0, borderwidth=0, width=5,textvariable=statement_2)
            lbl_frame_typewrite_config_1.pack(pady=5)

            lbl_frame_typewrite_config_2 = Entry(labelframe_typewrite, bg = "white", fg = "black",border=0, borderwidth=0, width=5,textvariable=statement_3)
            lbl_frame_typewrite_config_2.pack(pady=5)

            #Label for time.wait
            labelframe_wait = LabelFrame(frame_3, text="How many time to wait per text:", font = "Ariel 15", bg = r, fg = "white")  
            labelframe_wait.pack(fill="both", expand = "yes")  

            time_var = IntVar()
            lbl_frame_time_wait = Entry(labelframe_wait, bg = "white", fg = "black",border=0, borderwidth=0, width=5,textvariable=time_var)
            lbl_frame_time_wait.pack(pady=5)

            loop_type = Label(frame_3, text="Type your text below:", font = "Ariel 15", bg = r, fg = "white").pack(pady=15)


            #statement entry field (for the main)
            statement = StringVar()
            entry = Entry(frame_3,font = "Ariel 15", bg = 'white', fg = "black", border=0, borderwidth=0, width=55, textvariable=statement)
            entry.pack()

            clear_loop = Checkbutton(frame_3, text = "Clear: ",font = "Ariel 17", bg = r, fg = "white", borderwidth=0,border=0,command=lambda:[clear_entry()]).pack(pady=5)


            #submit button for the field (entry main pyautogui connect)
            loop_checkbutton = Checkbutton(frame_3, text = "Submit: ",font = "Ariel 17", bg = r, fg = "white", borderwidth=0,border=0,command=lambda:[entry_range_pyautogui_txt()]).pack(pady=5)



            #BACK BUTTON
            btn_frame_3 = Button(frame_3, text = "Back ",font = "Ariel 17", bg = "white", fg = "black", borderwidth=0,border=0,command=lambda:[clear_frame3()]).pack(pady=50)



            root.mainloop()




        def reload_loop_page():

            frame_6 = Frame(root)
            frame_6.pack()
            frame_6.config(bg = r)
            frame_6.place(relx=0.5, rely=0.4, anchor="c")

            def root_clr():
                root.destroy()

            frame_title_6 = Label(frame_6, text="Loop Menu", font = "Ariel 45", bg = r, fg = "white").pack(pady=50)

            frame_6_button = Button(frame_6, text = "Autoclicker",font = "Ariel 17", bg = r, fg = "black", borderwidth=0,border=0,activebackground="black",width=10,activeforeground="black",command=lambda:[clear_frame2(),Autoclicker()]).pack(pady=5)

            frame_6button_6 = Button(frame_6, text = "Autotyper Text",font = "Ariel 17", bg = r, fg = "black", borderwidth=0,border=0,activebackground="white",width=15,activeforeground="black",command=lambda:[autotype_text(), clear_frame2()]).pack(pady=20)

            frame_checkbutton_6 = Checkbutton(frame_6, text = "Back",font = "Ariel 20", bg = r, fg = "white", borderwidth=0,border=0,activebackground="white",width=10,activeforeground="black",command=lambda:[clear_frame2(), root_clr(), main()]).pack(pady=20)


        def Autoclicker():
            root.geometry('800x570')
            root.resizable(TRUE,TRUE)
            root.config(bg = r)
            
            frame_5 = Frame(root)
            frame_5.pack()
            frame_5.config(bg = r)

            #autoclicker functional function
            def autoclicker_functionality_Left():

                #time delay for autoclicker call
                time_delay_autoclicker = lbl_frame_time_daley_autoclicker.get()


                print(Fore.RED + "Autoclicker has started")

                #delivers notification box
                messagebox.showinfo(title="information", message = "AutoClicker will start in 7 seconds")

                #time sleeps for 7 seconds before start
                time.sleep(7)

                #loops while loop process
                while True:

                    #pyauto gui leftclicks
                    pyautogui.leftClick()

                    #time.sleeps for 1 second
                    time.sleep(int(time_delay_autoclicker))

            #autoclicker for right click
            def autoclicker_functionality_Right():

                #time delay for autoclicker call
                time_delay_autoclicker = lbl_frame_time_daley_autoclicker.get()

                print(Fore.RED + "autoclicker started")

                #delivers notification box
                messagebox.showinfo(title="information", message = "AutoClicker will start in 7 seconds")

                #time sleeps for 7 seconds before start
                time.sleep(7)

                #loops while loop process
                while True:

                    #pyauto gui rightclick
                    pyautogui.rightClick()

                    #time.sleeps for 1 second
                    time.sleep(int(time_delay_autoclicker))




            def quit_autoclicker():
                print(Fore.YELLOW + "Autoclicker has paused")

                #messagebox notification for the time limit
                messagebox.showinfo(title = "notification", message = "Autoclicker is now cancelled\nThank you")


            #destroying the frame so that it is reusable
                frame_5.destroy()

                #time sleep = 10
                # time.sleep(10)

            def time_wait_autoclicker():
                pass


            #clears frame5
            def clear_frame5():
                frame_5.destroy()

            #autoclicker window_main
            loop_autotype = Label(frame_5, text="Auto Clicker", font = "Ariel 40", bg = r, fg = "white").pack(pady=40)

            #time_delay label frame for autoclicker slide
            labelframe_time = LabelFrame(frame_5, text = "Time delay:", fg = "white", bg=r, font = "Ariel 20")  
            labelframe_time.pack(fill="both", expand = "yes")  

            #int variable for time delay
            time_delay_autoclicker = IntVar()

            #time delay entry
            lbl_frame_time_daley_autoclicker = Entry(labelframe_time, bg = "white", fg = "black",border=0, borderwidth=0, width=5, textvariable=time_delay_autoclicker)
            lbl_frame_time_daley_autoclicker.pack(pady=5)

            #label frame for autoclicker function
            labelframe2 = LabelFrame(frame_5, text = "Local Autoclicker", fg = "white", bg=r, font = "Ariel 20")  
            labelframe2.pack(fill="both", expand = "yes")  

            underline = Label(frame_5, text = "_____________________________________", fg = "white", bg = r)
            underline.pack(pady=5)

#getting value as string var and connecting to frame_scrape

            value_inside = tkinter.StringVar(frame_5)

            #classes list
            options = [
                #A day#
                'Left Auto Clicker',
                'Right Auto Clicker'
            ]
            #setting the title of the option menu
            value_inside.set('Choose your autoclicker')




            lbl_frame = LabelFrame(frame_5, text = "Autoclicker:", fg = "white", bg=r, font = "Ariel 20")  
            lbl_frame.pack(fill="both", expand = "yes")

            #_____#
            option = tkinter.OptionMenu(lbl_frame, value_inside,*options)
            option.pack(pady=5)
            option.config(bg = r)
            #_____#

            #callback function 
            def callback():
                #_____ Autoclicker _____ #
                if value_inside.get() == 'Left Auto Clicker':
                    autoclicker_functionality_Left()
                
                if value_inside.get() == 'Right Auto Clicker':
                    autoclicker_functionality_Right()


            #left autoclicker start checkbutton
            Start_Autoclickers = Checkbutton(lbl_frame ,text = "Start", bg=r, fg="white", font = "Ariel 20", command=lambda:[callback()])  
            Start_Autoclickers.pack(pady=10)  


            #back back button to go to previous slide
            btn_frame_3 = Button(frame_5, text = "Back ",font = "Ariel 17", bg = "white", fg = "black", borderwidth=0,border=0,command=lambda:[clear_frame5(),reload_loop_page()]).pack(pady=50)

            #mainloops function
            root.mainloop()

        def root_clr():
            root.destroy()


        
        loop_txt = Label(frame_2, text="Loop Menu", font = "Ariel 45", bg = r, fg = "white").pack(pady=50)

        auto_click_loop = Button(frame_2, text = "Autoclicker",font = "Ariel 17", bg = r, fg = "black", borderwidth=0,border=0,activebackground="black",width=10,activeforeground="black",command=lambda:[clear_frame2(),Autoclicker()]).pack(pady=5)

        auto_type_loop = Button(frame_2, text = "Autotyper Text",font = "Ariel 17", bg = r, fg = "black", borderwidth=0,border=0,activebackground="white",width=15,activeforeground="black",command=lambda:[autotype_text(), clear_frame2()]).pack(pady=20)

        back_btn_frame_2 = Checkbutton(frame_2, text = "Back",font = "Ariel 20", bg = r, fg = "white", borderwidth=0,border=0,activebackground="white",width=10,activeforeground="black",command=lambda:[clear_frame2(), root_clr(), main()]).pack(pady=20)





        root.mainloop()

    #Label for the frame option menu
    txt = Label(frame, text="Option Menu", font = "Ariel 45", bg = r, fg = "white").pack(pady=60)



    #checkbuttons for win 1
    web_browser = Checkbutton(frame, text = "Web Search",font = "Ariel 20", bg = r, fg = "white",command=lambda:[clear(),web_search()]).pack()

    while_loopghj4k4 = Checkbutton(frame, text = "While loop",font = "Ariel 20", bg = r, fg = "white", command=lambda:[clear(),loop_win1()]).pack(pady=20)

    discord_ = Checkbutton(frame, text = "Discord",font = "Ariel 20", bg = r, fg = "white", command=lambda:[clear(),discord_window()]).pack()

    gmail = Checkbutton(frame, text = 'Gmail', font = 'Ariel 20', bg = r, fg = 'white', command= lambda:[clear(),gmail_window()]).pack(pady=20)

    txt_file = Checkbutton(frame, text = "Text file",font = "Ariel 20", bg = r, fg = "white", command=lambda:[clear(), text_file()]).pack()


#todays's local date
    date_time = Label(frame, text = date.today(), font = "Ariel 20", bg = r, fg = "white",).pack(pady=40)

    #clear first window
    def clear():
        frame.destroy()


    #mainloops the first window
    root.mainloop()


main()