shirt = input("What color of Shirt do you like? ")
cap = input("Do you wear caps? ")
trouser = input("What type of Trouser do you like? ")
shoe = input("What type of Shoe do you wear normally? ")
stockings = input("Do you wear stockings? ")

stockings_yes = ""
cap_type = ""

if stockings.lower() == "yes":
    stockings_yes = input("What color do you normally wear? ")

if cap.lower() == "yes":
    cap_type = input("What color of Cap do you wear? ")

output = f"You can wear a {shirt} shirt with a {trouser} trouser"
if stockings_yes:
    output += f" and {stockings_yes} stockings"
output += f" on a {shoe} shoes"
if cap_type:
    output += f" and a cap {cap_type}"

print(output)
