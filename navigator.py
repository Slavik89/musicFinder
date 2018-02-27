from musicFinder import choose, radio_maximum,bbc_radio, lux_fm_radio, capital_fm

class Navigator():
    condition = True

    while condition == True:
        choose1 = choose.Choose.show_choice()
        value = input()
        if value == "1":
            call1 = radio_maximum.RadioMaximum("https://maximum.fm/")
            call1.show_info_about_song()
        elif value == "2":
            call2 = bbc_radio.RadioBBC("https://www.bbc.co.uk/radio1")
            call2.show_info_about_song()
        elif value == "3":
            call3 = lux_fm_radio.RadioLuxFM("http://lux.fm/player/onAir.do")
            call3.show_info_about_song()
        elif value == "4":
            call4 = capital_fm.RadioBBC("http://www.capitalfm.com/")
            call4.show_info_about_song()
        elif value == "e":
            print("Good-bye. See you later")
            break
        else:
            print("You wrote wrong symbol. Please, repeat your choice")
            print("__________________________________________________________" + '\n')
            continue




