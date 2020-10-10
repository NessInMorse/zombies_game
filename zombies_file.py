from random import choice
from random import randint
from time import time
from time import localtime
from time import asctime

rooms={}

hp=10
atk_power=[3,4,7]
weapon=["vuisten","mes","geweer"]
eqp=0
bag=[]
zombies_killed=0
rooms_visited_count=0
rooms_visited=[]
count=0

def maak_kamers(m_aantal):
        global rooms
        #De verschillende items die in de kamers gevonden kunnen worden
        items=["geweer","mes","medicijn","water","dagboek","voedsel"]
        
        #Maakt per kamer een sublist met de items die in de kamer te vinden zijn
        items_in_rooms=[[choice(items)for i in range(randint(0,3))]for j in range(m_aantal)]
        print(items_in_rooms)
        for x in range(len(items_in_rooms)):
                rooms["kamer"+str(x+1)]=items_in_rooms[x]
        print(rooms)
        return rooms

def zombie_gevecht(z_kamer):

        global hp
        global atk_power
        global weapon
        global rooms_visited
        global rooms_visited_count
        global zombies_killed
        rooms_visited_count+=1
        rooms_visited.append(z_kamer)
        
        z_heeft_zombies=randint(0,2)
        z_had_zombies=z_heeft_zombies
        #0 betekent heeft zombies
        if z_heeft_zombies==0:
                z_aantal_zombies=randint(1,3)
                print(f"Er {'zijn'*(z_aantal_zombies!=1)}{'is'*(z_aantal_zombies==1)} {z_aantal_zombies} zombie{(z_aantal_zombies!=1)*'s'} in de kamer")
                while z_aantal_zombies>0:
                        print("Een zombie valt je aan")
                        print(f"Je valt de zombie aan met je {weapon[eqp]}")
                        z_atk=atk_power[eqp]+randint(0,3)

                        if z_atk>=5:
                                z_aantal_zombies-=1
                                zombies_killed+=1
                        else:
                                print("De zombie verslaat jou!")
                                hp-=1
                                
                        if hp==0:
                                break;
                z_heeft_zombies=1
        if hp>0: 
                print(f"er zijn gelukkig geen zombies{' meer'*(z_had_zombies==0)} in de kamer")
        
                        




def spullen_vinden(s_kamer):
        global eqp
        items=len(rooms["kamer"+str((s_kamer+1))])
        for i in rooms["kamer"+str((s_kamer+1))]:
                if weapon.count(i)>0:
                        if weapon.index(i)>eqp:
                                eqp=weapon.index(i)
                                print(f"{weapon[eqp]} gevonden!")
                                if eqp==2:
                                        print("You know what they say, when life gives you lemons; by a fucking gun.")
                        elif weapon.index(i)<eqp:
                                items-=1
                else:
                        print(f"{i} gevonden!")
                        bag.append(i)
        if len(rooms["kamer"+str((s_kamer+1))])==0:
                print("Er is niets in de kamer dat we kunnen gebruiken")


def eet_genees():
        global hp
        if hp<5 and bag.count("medicijn")>0:
                bag.remove("medicijn")
                hp=10
                print("If you need a little revive.. Get some quick revive")
        elif hp<8 and bag.count("voedsel")>0 and bag.count("water")>0:
                hp+=2
                bag.remove("voedsel")
                bag.remove("water")
                print("The sour aftertaste lingers in your mouth")



def write_diary():
        note=input("Wat zou je toch willen schrijven in je dagboek? \n")
        newtext = open("dagboek.txt","a")
        newtext.write(f"\n\n{asctime(localtime(time()))}____________________________________________________________")
        newtext.write(f"Dit is mijn note: {note} \n")
        newtext.write(f"Zombie kill count: {zombies_killed} \n ")
        newtext.write(f"Dit zijn de voorwerpen in m'n tas {bag} \n ")
        newtext.close()
        
            
            


def main():
        n_kamers=int(input("Hoeveel kamers wil je hebben? "))
        kamers=maak_kamers(n_kamers)
        invite=randint(0,len(rooms)-1)
        while hp>0 and len(rooms)>rooms_visited_count:
                while rooms_visited.count(invite)!=0:
                        invite=randint(0,len(rooms)-1)
                        
                zombie_gevecht(invite)
                if hp>0:
                        spullen_vinden(invite)
                        eet_genees()
                        if bag.count("dagboek")>0:
                                write_diary()
                else:
                        print("Helaas je bent een zombie geworden")
        if hp>0:
                print("Je bent door alle rooms heen gegaan, gefeliciteerd; je bent geen zombie geworden")
        else:
                print("Je hebt verloren maat")
        
main()
