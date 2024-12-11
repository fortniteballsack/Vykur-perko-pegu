from pynput.keyboard import Controller
import time

keyboard = Controller()

# The string you want to type
text = ("orchid. co., ho. sedlo. se. soudruha. srdci. ji. hodil. krku. herolda. oka. culhaje. selhal. dlouho. ulice. ruce. dech. sil. dosedl. draka. chce. kroku. ruku. a. . ., j. cd. ego. ega. srdce. h. iii. gui. dolarů. lisa. kusů. roku. kdekdo. kuklu silou jako oklikou akci jeho sedlo jejich radaru, orchid. sice cosi, adresu dechu hladil sekci dalo dohled hlas chrlila dosud odchodu disku josefa hodila jsou klad lehce chci roku co., heslo druhu hrdlo culwur esli kroků rukou odfrkl sedlo. shodou dlouho cujhal ukrad soudruha, koho ohradil sedla sedle dala huldur celou okraji hej, daleko shodil soka krok srdci. dokola oddechuje, odkud dokud dlouho, sluch hledal dodala ruka hodil. kdejakou kolika dodal sahal hodil krku. cujhalu, herolda. ruku doufaje, draku sluje odfoukl lehce, culwara drak draka oka. roku, oko, culhaje. selhal. dlouho. lisa. o jeho kolega a jeho jsou jakousi sociologickou do k. odkudsi je asi druhou houf. kruh, hradec dech. ale akce fajfka fajfka fajfka sadů sadů sadů sadů fajfka sadů fajfka sůl důl kladů sladů klasů sklad kajak kladl sladů klasů sklad kladů kajak hadů gal sůl gag jak fa sadů fük lisa. o jeho kolega a jeho jsou jakousi sociologickou do k. odkudsi je asi")

# Wait for 2 seconds before starting
time.sleep(2)

for char in text:
  keyboard.type(char)
  time.sleep(0.288) # delay v sekundach