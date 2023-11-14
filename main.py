from item import Item

item1 = Item("MyItem", 750)
item1.name = "OtherItem"

print(item1.read_only_name)

item1.read_only_name = "BBB"