import Practice_1_2

# 1
purse = Practice_1_2.WizCoin(2, 5, 99)
print(purse)
print('G:', purse.galleons, 'S:', purse.sickles, 'K:', purse.knuts)
print('Total value:', purse.value())
print('Weight:', purse.weightInGrams(),'grams')
print()

# 2
coinJar = Practice_1_2.WizCoin(13, 0, 0)
print(coinJar)
print('G:', coinJar.galleons, 'S:', coinJar.sickles, 'K:', coinJar.knuts)
print('Total value:', coinJar.value())
print('Weight:', coinJar.weightInGrams(),'grams')
print()

# 3
change = Practice_1_2.WizCoin(9, 7, 20)
print(change.sickles)
change.sickles += 10
print(change.sickles)

# 4
pile = Practice_1_2.WizCoin(2, 3, 31)
print(pile)
pile.someNewAttribute = "a new attr"
print(pile.someNewAttribute)