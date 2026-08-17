class StockSpanner:

    def __init__(self):
        self.spanner = []

    def next(self, price: int) -> int:
        count = 1
        # print(self.spanner)
        for i in range(len(self.spanner) - 1, -1, -1):
            # print(i)
            if self.spanner[i] > price:
                break
            count += 1
        
        self.spanner.append(price)

        # print("")

        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)