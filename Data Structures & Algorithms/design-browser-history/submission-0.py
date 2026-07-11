class ListNode:
    def __init__(self, url):
        self.left = None
        self.url = url
        self.right = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = ListNode(homepage)

    def __str__(self):
        # Build left (back history) by traversing from current to the left
        curr = self.current
        left = []
        tmp = curr
        while tmp.left:
            tmp = tmp.left
            left.append(tmp.url)
        left = left[::-1]

        # Build right (forward history) by traversing from current to the right
        right = []
        tmp = curr
        while tmp.right:
            tmp = tmp.right
            right.append(tmp.url)

        temp = left + [f"| {self.current.url} |"] + right
        return "[" + " ---> ".join(temp) + "]"

    def visit(self, url: str) -> None:
        # When visiting a new url, drop all forward history
        new_url = ListNode(url)
        # break forward history
        self.current.right = None
        new_url.left = self.current
        self.current.right = new_url
        self.current = new_url

    def back(self, steps: int) -> str:
        curr = self.current
        for _ in range(steps):
            if curr.left:
                curr = curr.left
            else:
                break
        self.current = curr
        return self.current.url

    def forward(self, steps: int) -> str:
        curr = self.current
        for _ in range(steps):
            if curr.right:
                curr = curr.right
            else:
                break
        self.current = curr
        return self.current.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)