thriller=["Dark","Mindhunter","Parasite","Inception","Insidious","Interstellar","Prison Break","Money Heist","War","Jack Ryan"]
comedy=["Friends","3 Idiots","Brooklyn 99","How I Met Your Mother","Rick And Morty","The Big Bang Theory","The Office","Space Force"]

thriller1=(a.lower() for a in thriller)
comedy1=(a.lower() for a in comedy)

ans=input()

if ans.lower() in thriller1:
    print("It is a thriller")
elif ans.lower() in comedy1:
    print("It is a comedy")
else:
    print("It is neither thriller nor comedy")
