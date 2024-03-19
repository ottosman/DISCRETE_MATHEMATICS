
import math
import msvcrt

print('9n^2 +3n - 2 denklemi üzerinde işlem yapmaktasınız \n tek çift deneyleri h4 ödevi')

def nasil_olur_ya():
    while True:    
        try:
            bu_mumkun_degil = []
            bu_mumkun_degil.clear()
            
            print('\n LÜTFEN BOŞ KARAKTER GİRMEYİNİZ \n')
            q = int(input('lütfen  başlangıç değeri giriniz : '))
            w = int(input('lütfen bitiş değeri giriniz : '))
            
            


            a = min(q,w)
            b= max(q,w)
            for i in range (a,b+1):
                
                denklem = 9 * math.pow(i, 2) + 3 * i - 2
                
                if( denklem % 2 == 0):
                    bu_mumkun_degil.append('Ç')

                elif( denklem % 2 != 0):
                    bu_mumkun_degil.append('T')

                else:
                    print('beklenmeyen değer girildi/çıktı f000f')
                    break

            ciftadet= bu_mumkun_degil.count('Ç')
            tekadet= bu_mumkun_degil.count('T')
            print('Girdiğiniz değerler arasındaki tek ve çift değerler:')
            print('Çift adedi:', str(ciftadet))
            print('Tek adedi:', str(tekadet))

            if tekadet <= 0:
                print("Bu denklem her halükarda çifttir.")
            else:
                print('bu denklem mutlak çift değildir')
        except Exception as e:
            print('Hata oluştu baştan başlanıyor...')




def yeniden():
    while True:
        print('uygulamayı kapamak için Q  başlatmak için R tuşuna basınız: ')
        # Bir tuşa basılıncaya kadar bekle
        key = msvcrt.getch()
        # 'q' tuşuna basıldıysa programdan çık
        if key == b"q":
            break
        
        elif key == b"r":
            nasil_olur_ya()
        # Basılan tuşu ekrana yazdır
        print(key)

yeniden()

