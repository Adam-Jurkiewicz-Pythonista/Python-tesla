class Statek:
    def __init__(self):
        print("Initializing Statek")

    def __new__(cls, *args, **kwargs):
        print("__new__ called")



orp_orzel = Statek()
print(orp_orzel)
print(dir(orp_orzel))
