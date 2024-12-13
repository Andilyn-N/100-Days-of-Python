travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
# to print "Lille"
# print(dictionary["key to list"][entry number in list])
print(travel_log["France"][1])


nested_list = ["A", "B", ["C", "D"]]
# to print D:
print(nested_list[2][1])

travel_log2 = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}
# printing Stuttgart
# print (access dictionary["Key2"]["KeyB_within Key2"][Numberinlist])
print(travel_log2["Germany"]["cities_visited"][2])