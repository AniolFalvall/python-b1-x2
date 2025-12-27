from .entity import *
from .item import *

class OrderType:
    # Do not change this enum
    ASC = 0
    DES = 1


class Statistics:
    def __init__(self, bills: list[Bill]):
        # Do not change this method
        self.bills = bills

    def find_top_sell_product(self) -> (Product, int):
        counter = {}

        for bill in self.bills:
            for product in bill.products:
                if product in counter:
                    counter[product] += 1
                else:
                    counter[product] = 1

        top_product = max(counter.items(), key=lambda item: item[1])
        return top_product

    def find_top_two_sellers(self) -> list:
        counter = {}

        for bill in self.bills:
            seller = bill.seller
            total_bill = bill.calculate_total()

            if seller in counter:
                counter[seller] += total_bill
            else:
                counter[seller] = total_bill

        order_sellers = sorted(counter.items(), key=lambda item: item [1],
                               reverse=True)
        
        top_two_sellers = [order_sellers[0][0], order_sellers[1][0]]
        return top_two_sellers
        
    def find_buyer_lowest_total_purchases(self) -> (Buyer, float):
        counter = {}

        for bill in self.bills:
            buyer = bill.buyer
            total_bill = bill.calculate_total()

            if buyer in counter:
                counter[buyer] += total_bill
            else:
                counter[buyer] = total_bill

        buyer_lowest_total_purchase = sorted(counter.items(), 
                              key=lambda item: item [1])
        return buyer_lowest_total_purchase[0]

    def order_products_by_tax(self, order_type: OrderType) -> tuple:
        counter = {}

        for bill in self.bills:
            for product in bill.products:
                total_taxes = product.calculate_total_taxes()
                if product in counter:
                    counter[product] += total_taxes
                else:
                    counter[product] = total_taxes

        reverse = True if order_type == OrderType.DES else False
        ordered = sorted(counter.items(), key=lambda item: item[1],
                         reverse=reverse)
        return tuple(ordered)

    def show(self):
        # Do not change this method
        print("Bills")
        for bill in self.bills:
            bill.print()
