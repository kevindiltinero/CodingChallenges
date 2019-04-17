import collections

"""
def runTest(msg, expected, hand, other):
    player, opponent = PokerHand(hand), PokerHand(other)
    test.assert_equals(player.compare_with(opponent), expected, "{}: '{}' against '{}'".format(msg, hand, other))


runTest("Highest straight flush wins",        "Loss", "2H 3H 4H 5H 6H", "KS AS TS QS JS")
runTest("Straight flush wins of 4 of a kind", "Win",  "2H 3H 4H 5H 6H", "AS AD AC AH JD")
runTest("Highest 4 of a kind wins",           "Win",  "AS AH 2H AD AC", "JS JD JC JH 3D")
runTest("4 Of a kind wins of full house",     "Loss", "2S AH 2H AS AC", "JS JD JC JH AD")
runTest("Full house wins of flush",           "Win",  "2S AH 2H AS AC", "2H 3H 5H 6H 7H")
runTest("Highest flush wins",                 "Win",  "AS 3S 4S 8S 2S", "2H 3H 5H 6H 7H")
runTest("Flush wins of straight",             "Win",  "2H 3H 5H 6H 7H", "2S 3H 4H 5S 6C")
runTest("Equal straight is tie",                 "Tie",  "2S 3H 4H 5S 6C", "3D 4C 5H 6H 2S")
runTest("Straight wins of three of a kind",   "Win",  "2S 3H 4H 5S 6C", "AH AC 5H 6H AS")
runTest("3 Of a kind wins of two pair",       "Loss", "2S 2H 4H 5S 4C", "AH AC 5H 6H AS")
runTest("2 Pair wins of pair",                "Win",  "2S 2H 4H 5S 4C", "AH AC 5H 6H 7S")
runTest("Highest pair wins",                  "Loss", "6S AD 7H 4S AS", "AH AC 5H 6H 7S")
runTest("Pair wins of nothing",               "Loss", "2S AH 4H 5S KC", "AH AC 5H 6H 7S")
runTest("Highest card loses",                 "Loss", "2S 3H 6H 7S 9C", "7H 3C TH 6H 9S")
runTest("Highest card wins",                  "Win",  "4S 5H 6H TS AC", "3S 5H 6H TS AC")
runTest("Equal cards is tie",                  "Tie",  "2S AH 4H 5S 6C", "AD 4C 5H 6H 2C")

"""

class PokerHand(object):

    RESULT = ["Loss", "Tie", "Win"]

    def __init__(self, hand):
        royal_translation = {"J":"11", "Q":"12", "K":"13", "A":"14"}
        self.cards = [royal_translation[x[:-1]]+x[-1] if x[:-1] in royal_translation.keys() else x for x in hand.split()]
        print(self.cards)
        pass
        
    def compare_with(self, other):
        # Shorty different types of bonds
        if self.checking_hands() != other.checking_hands():
            return max()
        pass
    
    def checking_hands(self):
        if self.checking_order() and self.checking_same() and self.checking_royals():
            return ("Royal Flush", 10)
        elif self.checking_order() and self.checking_same():
            return ("Straight Flush", 9)
        elif self.checking_same():
            return ("Flush", 6)
        elif self.checking_order():
            return ("Straight", 5)
        elif self.checking_pairs()[0]:
            return self.checking_pairs()
        else:
            return self.checking_highest()
                
    def checking_pairs(self):
        self.cards.sort(key=lambda x:x[0])
        count = 1
        current_card = ""
        pears = []
        tracking_dictionary = collections.defaultdict(int)
        results_changing = {(2, 3):7, (1, 4):8, (1, 2, 2):3, (1, 1, 1, 2):2, (1, 1, 3):4, (1, 1, 1, 1, 1):None}
        for x in range(len(self.cards)):
            tracking_dictionary[self.cards[x][:-1]] += 1
        my_list = [x for x in tracking_dictionary.items() if x[1] > 1]
        return results_changing[tuple(sorted(tracking_dictionary.values()))], my_list 
    
    def checking_order(self):
        self.cards.sort(key=lambda x:int(x[:-1]))
        for x in range(1, len(self.cards)):
            if int(self.cards[x][:-1]) != int(self.cards[x-1][:-1]) + 1:
                return False
        return True
            
    def checking_same(self):
        for x in range(1, len(self.cards)):
            if self.cards[x][-1] != self.cards[x-1][-1]:
                return False
            return True
        
    def checking_royals(self):
        for x in ["14", "13", "12", "11", "10"]:
            if x not in [y[:-1] for y in self.cards]:
                return False
        return True
    
    def checking_highest(self):
        return (1, max([int(x[:-1]) for x in self.cards]))
               
obj1 = PokerHand("KD QD AD JD 10D")
obj2 = PokerHand("KD QD 9D JD 10D")
obj3 = PokerHand("10H 10D 10S 10C AD")
obj4 = PokerHand("10H 10D 10S 7C 7D")
obj5 = PokerHand("10H 9H 8H 7H AH")
obj6 = PokerHand("10H 9H 8H 7H 6D")
obj7 = PokerHand("10H 10D 10S 9C AD")
obj8 = PokerHand("10H 10D 9S 9C AD")
obj9 = PokerHand("10H 10D 9S 4C AD")
obj10 = PokerHand("10H 3D 9S 4C AD")
print(obj8.checking_hands())
# print(obj2.checking_hands())
