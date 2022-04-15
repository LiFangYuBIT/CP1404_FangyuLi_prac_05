color = {"Absolute Zero": "#048ba", "Acid Green": "#b0bf1a", "Aliceblue": "#f0f8ff", "Alizarin crimson": "#e32636",
         "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc", "Antiquewhite": "#faebd7",
         "Antiquewhite1": "#ffefdb", "Aqua": "#00ffff"}

color_name = input("Enter a colour name: ")
while color_name.strip() != "":
    print(f"The code for {color_name} is {color.get(color_name.title())}")
    color_name = input("Enter a colour name: ")
