##test 1st time makng Classes;Python;Pokemon examples - 6/6/2020 ###


##Pokemon class Defined
class Pokemon:
    def summary_self(self):
        print(self.name + "\n" + "Type: "+ self.type +"\n")

##Pokemon data##
pkm1 = Pokemon()
pkm1.name = "Bulbasaur"
pkm1.type = "Grass/Poison"
pkm1.lvl = "LvL.10"

pkm2 = Pokemon()
pkm2.name = "Alcremie"
pkm2.type = "Fairy"
pkm2.lvl = "LvL.50"


##Type Display##

pkm1.summary_self()

pkm2.summary_self()




