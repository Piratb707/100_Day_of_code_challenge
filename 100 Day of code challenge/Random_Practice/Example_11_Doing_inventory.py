from collections import Counter
def main():
    inventory = Counter(STA001=10, SAL002=20, ENT004=13)
    sales = Counter(STA001=5, SAL002=3, ENT004=3)
    inventory = inventory-sales
    shipment_in = {'STA001': 9, 'SAL002': 1}
    inventory.update(shipment_in)
    print(inventory)

if __name__ == "__main__":
    main()