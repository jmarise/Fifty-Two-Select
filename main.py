import random

class luckOfTheDraw:
 
  def __init__(self):
    self.__deck = []
    self.i = 0  
  
  def setdeck(self, i, deck):
    self.__deck = deck
    self.i = i
    

  def _init_deck(self):
    count_cards = ["A","2","3","4","5","6","7","8","9","10","J","Q","K" ]
    suites = ["S", "H", "D", "C"]
    count_index = 0
    
    for c in range(len(count_cards)):
      suites_index = 0
      for s in range(len(suites)): 
        self.__deck.insert(self.i,(count_cards[count_index] + suites[suites_index]))
        self.i += 1 
        suites_index += 1
      

      count_index += 1  
  

  def getdeck(self):
    return self.__deck

  deck = property(getdeck, setdeck)


  def random_pick(self):
    pick = random.randrange(0, 51)
    return self.__deck[pick]



  def binary_search(self, low , high, card):
    print(f"low: {low}")
    print(f"high: {high}")

    
  
    if   int(high) >= int(low)  : 
      mid = ((high + low) // 2) 
      sort = sorted(self.__deck)
      


      if sort[mid] == card:
        print(sort[mid])
        return mid
      
      elif sort[mid] > card:
        print(f"{sort[mid]}")
        return luckOfTheDraw.binary_search(self,low, mid - 1, card)
      
      else:
        print(f"{sort[mid]}")
        return luckOfTheDraw.binary_search(self, mid + 1, high, card)
      
    else: 
      return -1

  def val(self, card):
    low = 0 
    high = int(len(self.__deck))


    return luckOfTheDraw.binary_search(self, low, high, card)
      
  def menu(self): 
    luckOfTheDraw._init_deck(self)
    userinput = input("Enter the card: ")

    return luckOfTheDraw.val(self, userinput.upper())


lotd = luckOfTheDraw()
answer = lotd.menu()
print(f"{answer}")
