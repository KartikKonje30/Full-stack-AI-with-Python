

def chai_Order():
    chai_Option = "Ginger" # Enclosing scope
    def chai_Order2():
        chai_Option = "Lemon"
        print(f"Inner Scope: {chai_Option}")
    chai_Order2()
    print(f"Outer Scope: {chai_Option}")

chai_Order()

chai_Option = "Tulsi"
print(f"Global Scope: {chai_Option}")