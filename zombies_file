from random import choice
from random import randint



rooms={}

hp=10
atk_power=[3,4,7]
weapon=["vuisten","mes","geweer"]
eqp=0
bag=[]
zombies_killed=0
rooms_visited_count=0
rooms_visited=[]


def maak_kamers(m_aantal):
        global rooms
        b=["geweer","mes","medicijn","water","dagboek","voedsel"]
        a=[[choice(b)for i in range(randint(0,3))]for j in range(m_aantal)]
        for x in range(len(a)):
                rooms["kamer"+str(x+1)]=a[x]
        print(rooms)
        return rooms

def zombie_gevecht(z_kamer):

        global hp
        global atk_power
        global weapon
        global rooms_visited
        rooms_visited_count+=1
        rooms_visited.append(i)
        
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
                
        print(f"er zijn gelukkig geen zombies{' meer'*(z_had_zombies==0)} in de kamer")
        spullen_vinden(z_kamer)
                        
#print(zombie_gevecht(3))



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


def main():
        n_kamers=int(input("Hoeveel kamers wil je hebben? "))
        kamers=maak_kamers(n_kamers)
        while hp>0 and len(dic)>rooms_visited_count:
                while rooms_visited.count(invite)!=0:
                        invite=randint(0,len(dic))
                zombie_gevecht(invite)
        print()
        
main()

