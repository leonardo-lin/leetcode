class A:
    a=10
    def use(self):
        self.a*=2
        print(self.a)


n=A
n.use(n)