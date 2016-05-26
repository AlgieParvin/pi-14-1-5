from random import randint

WE = ["Ramal Yusifov", "Danya Baranenko", "Nikita Nemtsov", "Slavik Palamar"]

def get_comic_belt():
   champion = WE[randint(0, 3)]
   while champion != WE[1] || champion != WE[3]:
       champion = WE[randint(0, 3)]
   return "And the champion is ... " + champion.upper()

if __name__ == "__main__":
    print(get_comic_belt())

#SO COOOOOOOOOOL
