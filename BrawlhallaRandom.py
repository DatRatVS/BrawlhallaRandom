from random import randint

legends = ["Bödvar", "Cassidy", "Orion", "Lord Vraxx", "Gnash", "Queen Nai", "Hattori", "Sir Roland",
          "Scarlet", "Thatch", "Ada", "Sentinel", "Lucien", "Teros", "Brynn", "Asuri", "Barraza", "Ember",
          "Azoth", "Koji", "Ulgrim", "Diana", "Jhala", "Kor", "Wu Shang", "Val", "Ragnir", "Cross", "Mirage",
          "Nix", "Mordex", "Yumiko", "Artemis", "Caspian", "Sidra", "Xull", "Kaya", "Isaiah", "Jiro", "Lin Fei",
          "Zariel", "Rayman", "Dusk", "Fait", "Thor", "Petra", "Vector", "Volkov", "Onyx", "Jaeyun", "Mako",
          "Magyar", "Reno"]

i = 1
inp = int(input("How many times you want it to be rolled? "))
print("ok, rolling " + str(inp) + " times.")

while i < inp:
 print(legends[randint(0 ,len(legends)- 1)])
 i += 1
