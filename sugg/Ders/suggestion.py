import tkinter as tk
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import messagebox
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By


suggestion_list_ = ["elma bir meyvedir",
                     "brokoli bir sebzedir",
                     "atatürk türkiye cumhuriyetinin kurucusudur",
                     "çağla ramis ilgüz bir nevüde akademisyendir",
                     "metallica en iyi metal müzik grubudur",
                     "cafer osman yıldız nevüde 2023 yılında ayrık matematik dersinden başarısız olmuştur",
                     "çağla ramis ilgüz doktorasını ankara üniversitesinde alt manifoldlarda minimal yüzeyler üzerine yapmıştır"]



window = tk.Tk()
window.title("Lütfen sorunuzu yazınız. CASE SENSITIVE! \n hazır önerme örneklerini deneyebilirsiniz ")

entry = tk.Entry(window, width=100)
entry.pack()

def get_input():
    global user_input
    user_input = entry.get()
    user_input.lower()
    print(f"Soru: {user_input}")
    window.destroy()


button = tk.Button(window, text="Devam", command=get_input)
button.pack()

window.mainloop()




if ( "!" in user_input or "?" in user_input):
    messagebox.showinfo("Bilgi" ,"Girdi önerme değildir. Webde bulduğum sonuçlara kutuyu kapadıktan 3 saniye sonra bakabilirsiniz.")
    print("Girdi önerme değildir ")
    try:   
        driver = webdriver.Chrome()
        driver.get("https://www.google.com")
        search_box = driver.find_element("name", "q")
        search_box.send_keys(user_input)
        search_box.send_keys(Keys.RETURN)
        # time.sleep(20) #20 saniye geçtikten sonra browser kapanır/ browserı siz kapatırsanız lütfen kodu bitirin
        # driver.quit()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.result")))
    
    except Exception as e:
        print(f"browser kapatıldı" )
    
    finally:
        driver.quit()

    
    
elif(user_input== i for i in suggestion_list_):
    if(user_input == suggestion_list_[0]):
        messagebox.showinfo("Bu bir önermedir." ,"Evet, Elma bir meyvedir --> 1")
        print("Evet, Elma bir meyvedir --> 1")
    
    elif(user_input == suggestion_list_[1]):
        messagebox.showinfo("Bu bir önermedir." ,"Evet, Brokoli bir sebzedir. --> 1")
        print("Evet, Brokoli bir sebzedir. --> 1")
    
    elif(user_input == suggestion_list_[2]):
        messagebox.showinfo("Bu bir önermedir." ,"Evet, Mustafa Kemal Atatürk Türkiye Cumhireti devletinin kurucusudur. --> 1")
        print("Evet, Mustafa Kemal Atatürk Türkiye Cumhireti devletinin kurucusudur.")
    
    elif(user_input == suggestion_list_[3]):
        messagebox.showinfo("Bu bir önermedir." ,"Evet, Çağla Ramis İlgüz Nevşehir HBV Üniversiteinde bir akademisyendir. --> 1")
        print("Evet, Çağla Ramis İlgüz Nevşehir HBV Üniversiteinde bir akademisyendir. --> 1")
    
    elif(user_input == suggestion_list_[4]):
        messagebox.showinfo("Bu bir önermedir." ,"Hayır, bu önerme yanlıştır (en iyi metal grubu Rammsteindir) --> 0")
        print("Hayır, bu önerme yanlıştır --> 0 (en iyi metal grubu Rammsteindir) ")

    elif(user_input == suggestion_list_[5]):
        messagebox.showinfo("Bu bir önermedir." ,"Evet Cafer Osman YILDIZ ayrık matematik dersinden başarısız olmuştur (hakkı da yenmiştir) --> 0")
        print("Evet, Cafer Osman YILDIZ ayrık matematik dersinden başarısız olmuştur (hakkı da yenmiştir) --> 1")
    
    elif(user_input == suggestion_list_[6]):
        messagebox.showinfo("Bu bir önermedir." ,"Evet Çağla Ramis İlgüz Doktrasını Ankara Üniversitesi Fen Fakültesi Matematik Bölümünde alt manifoldlarda minimal yüzeyler üzerine yapmıştır. --> 1 \n https://gazeteler.ankara.edu.tr/xmlui/handle/20.500.12575/88575")
        print("Evet, \n Çağla Ramis İlgüz Doktrasını Ankara Üniversitesi Fen Fakültesi Matematik Bölümünde alt manifoldlarda minimal yüzeyler üzerine yapmıştır. --> 1 \n https://gazeteler.ankara.edu.tr/xmlui/handle/20.500.12575/88575") 
   
    else:
        messagebox.showinfo("Dingdong","Girdi önerme olabilir.")
        print("Hmmm", "Girdi önerme olabilir.")

else:
        messagebox.showinfo("Dingdong","Girdi önerme olabilir.")
        print("Hmmm", "Girdi önerme olabilir.")

