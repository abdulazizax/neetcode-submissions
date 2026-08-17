class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        """
        [[], [100, 1], [80, 1], [60, 1], [70, 2], [60, 3], [75, 4], [85, 6]]
        """
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        
        self.stack.append([price, span])

        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)