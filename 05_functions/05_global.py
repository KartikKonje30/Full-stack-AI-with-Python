
chai_Option = "Irani"

def chai_Order():
    chai_Option = "Tulsi"
    def chai_Order2():
        global chai_Option # Global scope variables can be accessed
        chai_Option = "Ginger"
        print(f"Inner Scope: {chai_Option}")
    chai_Order2()
    print(f"Outer Scope: {chai_Option}")

chai_Order()
print(f"Global Scope: {chai_Option}")