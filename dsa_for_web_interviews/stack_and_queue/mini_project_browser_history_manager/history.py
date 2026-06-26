class BrowserHistory:

    def __init__(self):
        self.current = "Home"
        self.back_stack = []
        self.forward_stack = []

    def visit(self, page):
        self.back_stack.append(self.current)
        self.current = page
        self.forward_stack.clear()

    def back(self):
        if self.back_stack:
            self.forward_stack.append(self.current)
            self.current = self.back_stack.pop()

    def forward(self):
        if self.forward_stack:
            self.back_stack.append(self.current)
            self.current = self.forward_stack.pop()

    def current_page(self):
        return self.current

    def show_history(self):
        print("\nBack Stack:", self.back_stack)
        print("Current:", self.current)
        print("Forward Stack:", self.forward_stack)