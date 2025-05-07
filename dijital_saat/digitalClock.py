from tkinter import Label,Tk
import time
app_window=Tk() #pencere oluşturmak için 

app_window.title("Dijital Saat") #pencereye isism  vermek için  .title() kullanıyoruz
app_window.geometry("450x300") # genişlik ve yüksekligi ayaramak için .geometry() metodunu kullanıyoruz
app_window.resizable(0,0) # genişlik ve yüksekligi değiştire bilmek için .resizable(1,1) değiştirmeye izin vermemek için de  .resizable(0,0)
app_window.configure(bg="black") # penceredeki rengi yazıyı falan fialn işte düzeltmek için .configure()metodunu kullanıyoruz
text_font= ("Agency FB", 50, "bold")
background="black"
foreground="white"
border_width= 20 #genişlik değişkeni

#saat etiketi
label= Label(app_window,font=text_font, bg=background, fg=foreground) #b
label.grid(row=0,column=1,padx=border_width,pady=10)# şablona eklemekiçin grid. row satır  padx sol ve sağdan boşlugu ,pady yukardan ve aşagıdan boşlugu ifade ediyor
    
# tarih etiketi
date_label= Label(app_window,font=text_font, bg=background, fg=foreground)

date_label.grid(row=1,column=1,padx=border_width,pady=10,)
 
def digital_clock():
      time_live =time.strftime("%H:%M:%S")
      label.config(text=time_live)
      #tarih alnı
      date_info=time.strftime("%d  %B  %Y")
      date_label.config(text=date_info)
      label.after(200,digital_clock)
digital_clock()

app_window.mainloop() # ekranda görünütüyü sağlamak için ihtyacımız olan metod .mainloop()
