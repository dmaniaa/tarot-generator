import random
import tkinter as tk
from PIL import ImageTk, Image

def main():
    window = tk.Tk()
    window.title("Tarot")
    window.resizable(False, False)

    class card:
        def __init__(self, name, desc, filename):
            self.id = id
            self.name = name
            self.desc = desc
            self.reversed = False
            self.image = Image.open("img/" + filename).resize((256,512))

    def on_click(card):
        new_window = tk.Toplevel(window)
        new_window.title(card.name)
        new_window.geometry("300x300")
        new_window.resizable(False, False)

        lbl_desc = tk.Label(new_window, text=card.desc, wraplength=300)
        lbl_desc.pack()


    all_cards = []
    all_cards.append(card("Głupiec", "Głupiec to ty i ja. Ktoś, kto każdego dnia stawia pierwszy krok na drodze w świat. Ostatecznie droga zmieni go, ale w uchwyconej na karcie chwili, jest ufnym żółtodziobem, która ma nadzieję, że osiągnie swój cel.", "TarotCard_01_TheFool.png"))
    all_cards.append(card("Mag", "Mag jest kartą wszechstronności i pewności siebie. Opowiada o przezwyciężaniu przeciwności za pomocą intelektu i siły woli. Mag jest intrygantem, który trzyma w zanadrzu niejedną sztuczkę, zawsze stara się utrzymać na powierzchni, i pozostać panem własnego losu.", "TarotCard_02_TheMagician.png"))
    all_cards.append(card("Kapłanka", "Kapłanka jest kartą tajemnicy. Opowiada o łagodności, która stoi na straży sekretów i o zmaganiu między zdrowym rozsądkiem a intuicją. Kapłanka symbolizuje chłód spokojnych wód, jak również tajemnice, które kryją się w ich głębinach.", "TarotCard_03_TheHighPriestess.png"))
    all_cards.append(card("Cesarzowa", "To karta silnej kobiecości i Macierzyństwa. Cesarzowa jest władcza i spełniona, łączy w sobie majestat i zmysłowość. To wielkie arkanum symbolizuje kreatywność i wzrost. Podpowiada, by słuchać intuicji i nie lekceważyć podświadomości." ,"TarotCard_04_TheEmpress.png"))
    all_cards.append(card("Cesarz", "Cesarz reprezentuje patriarchalną władzę, cieszącego się autorytetem wizjonera. Cesarz ustala zasady i egzekwuje je dla dobra ogółu. Prestiż ma jednak swoje ciemne strony: cesarz jest dominujący i bezwzględny, dąży do celu po trupach.", "TarotCard_05_TheEmperor.png"))
    all_cards.append(card("Arcykapłan", "Arcykapłan symbolizuje przywiązanie do tradycji. To ktoś, kto strzeże ustalonego porząku i jest przez ten porządek ukształtowany. Arcykapłan wierzy w instytucje, ponieważ alternatywą dla nich jest chaos. Wiara w ład daje mu siłę.", "TarotCard_06_TheHierophant.png"))
    all_cards.append(card("Kochankowie", "Kochankowie to karta dwoistości. Mówi o przeciwieństwach, które ścierają się w każdym człowieku i o dążeniu do harmonii skrajności. Kochankowie są również arkanum dylematów. Reprezentują wybór głupca, który stoi na rozdrożu i musi wybrać dalszą drogę.", "TarotCard_07_TheLovers.png"))
    all_cards.append(card("Rydwan", "Rydwan zawsze pędzi przed siebie, mimo że wierzchowce wiodą go w przeciwne strony. Nad jego ruchem panuje jeździec, który dzięki rozumowi kontroluje impulsy ciemnej i jasnej strony duszy. Jazda w rydwanie to ciąg wzlotów i upadków.", "TarotCard_08_TheChariot.png"))
    all_cards.append(card("Siła", "Siła jest kartą przetrwania. Jest związana z determinacją, odwagą i zaciętą walką. Mówi o samozaparciu w dążeniu do wyznaczonego celu, o przezwyciężaniu przeciwności. To tężyzna fizyczna i hart ducha, niewinna moc, która pozawala dokonać niemożliwego.", "TarotCard_09_Strength.png"))
    all_cards.append(card("Eremita ", "To karta izolacji. Reprezentuje ucieczkę od gwaru wielkiego miasta, odwrócenie się od pogoni za tym co nowe i zwrócenie się w stronę tradycji. Dla eremity samotność jest drogą do doskonałości, i pustelnik stąpa tą drogą małymi krokami.", "TarotCard_10_TheHermit.png"))
    all_cards.append(card("Koło fortuny", "Zapowiada nadchodzącą zmianę. Jest arkanum losu, który może odmienić życie na lepsze lub gorsze. Koło fortuny przypomina, że nikt nie utrzyma się na szczycie wiecznie, ale równie, że nie ma sytuacji bez wyjścia.", "TarotCard_11_WheelOfFortune.png"))
    all_cards.append(card("Sprawiedliwość", "Sprawiedliwość jest kartą rozwiązania problemu. Mówi o potrzebie zaprowadzenia ładu, przejrzenia przez oszustwo, przywrócenia naturalnego stanu rzeczy. Sprawiedliwość symbolizuje sprawiedliwy wyrok, ale i łaskawe postępowanie.", "TarotCard_12_Justice.png"))
    all_cards.append(card("Wisielec", "Wisielec jest kartą poświęcenia. Symbolizuje cenę, którą trzeba zapłacić za oświecenie. Wyrzeczenie wisielca pozwala mu odnaleźć nowe życie, ale droga do odrodzenia wiedzie przez zawieszony w czasie ból i kończy się śmiercią.", "TarotCard_13_TheHangedMan.png"))
    all_cards.append(card("Śmierć", "Śmierć jest kartą stawania się. Oznacza nieuchronną i trudną przemianę. Mówi o przejściu z jednego stanu do innego, o definitywnym zamknięciu jakiegoś etapu w życiu. Podczas transformacji coś zostaje stracone, ale rodzi się nowy byt.", "TarotCard_14_Death.png"))
    all_cards.append(card("Umiarkowanie", "To karta harmonii. Może symbolizować powściągliwość lub powolny rozwój w celu osiągnięcia stanu dojrzałej równowagi. Umiarkowanie związane jest z umiejętnością panowania nad sobą i z próbą osiągnięcia wewnętrznego spokoju.", "TarotCard_15_Temperance.png"))
    all_cards.append(card("Diabeł", "Diabeł jest uzależnieniem, pożądaniem i namiętnością. Przynosi sławę i bogactwo, ale za cenę zatracenia się w świecie materialnych pokus. Diabeł wabi w pułapkę, jednak zawsze daje wybór. Można z nim igrać i korzystać z jego oferty, ale należy wiedzieć, kiedy się wycofać z gry.", "TarotCard_16_TheDevil.png"))
    all_cards.append(card("Wieża", "Groźne arkanum gwałtownej zmiany, chaosu, i zniszczenia. Wieża rażona piorunem oznacza przewrót grzebiący pod gruzami stary porządek i następujące później narodziny nowego ładu. Symbolizuje tragedią, rozpad świata i autodestrukcję.", "TarotCard_17_TheTower.png"))
    all_cards.append(card("Gwiazda", "Gwiazda to arkanum nadziei. W najgłębszej ciemności świeci jasno, wskazując właściwą drogę podróżnym i przypominając, że na końcu wędrówki jest dom. Gwiazda inspiruje, zachęca do podjęcia wysiłku, daje siłę, by brnąć naprzód.", "TarotCard_18_TheStar.png"))
    all_cards.append(card("Księżyc", "Księżyc przypomina, że rzeczywistość nie jest tym, czym wydaje się być. W świecie pozorów i złudzeń najlepszą drogę znajduje się czasami, ufając intuicji. Księżyc jest również kartą snów i marzeń, a sen jest małym misterium śmierci.", "TarotCard_19_TheMoon.png"))
    all_cards.append(card("Słońce", "Słońce symbolizuje sukces. Jest arkanum wyzwolenia, oczyszczenia, jasnej przyszłości. Słońce to także prawda, ponieważ światło rozjaśnia najciemniejsze zakamarki i ujawnia to, co dotąd było skryte w cieniu. Słońce to również wielkość.", "TarotCard_20_TheSun.png"))
    all_cards.append(card("Sąd ostateczny", "Sąd ostateczny jest kartą odrodzenia. Dmiący w trąbę anioł oznajmia zmartwychwstanie i wyzwolenie. Ta karta mówi o ważnej zmianie, której rezultatem będzie uzdrowienie lub spełnienie. Jest to również arkanum samooceny.", "TarotCard_21_Judgement.png"))
    all_cards.append(card("Świat", "Świat to miasto, kres wędrówki głupca. Po długiej drodze następuje konfrontacja i wzbogaceni o doświadczenie podróży głupcy podejmują decyzję. Jedni godzą się ze światem, inni rzucają światu kolejne wyzwanie. Jedno jest pewne - nikomu nie udało się ujrzeć świata u swoich stóp.", "TarotCard_22_TheWorld.png"))

    random_cards = random.sample(all_cards, 4)

    for card in random_cards:
        if (bool(random.getrandbits(1))):
            card.reversed = True
            card.image = card.image.rotate(180)
    
        card.image = ImageTk.PhotoImage(card.image)

    btns = []
    lbls = []

    for index, card in enumerate(random_cards):
        btns.append(tk.Button(window, image=card.image, command=lambda card=card: on_click(card)))
        lbls.append(tk.Label(window, text=card.name + card.reversed * " (odwrócona)"))
        btns[index].grid(row=0, column=index)
        lbls[index].grid(row=1, column=index)
    

    window.mainloop()

if __name__ == "__main__":
    main()