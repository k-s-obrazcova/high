class CalculateMoney:
    def sum_price_count(self, price: [float, int], count: [float, int], discount: int = None):
        result = round(count * price, 2)
        if discount:
            result = round(result * (1 - (discount/100)), 2)

        return result