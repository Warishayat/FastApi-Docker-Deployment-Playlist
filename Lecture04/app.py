posts = [
    {"id":1 , "name" : "waris hayat abbasi","Department":"AI Engineer","rollnum":12,"course":"Software Enginner"},
    {"id":2 , "name" : "Kashan Mehfooz Ali","Department":"Real Estate Agency","rollnum":13,"course":"Digital Marketing"},
    {"id":3 , "name" : "Wakar Zakka","Department":"Trading","rollnum":14,"course":"Trading On Harvard School of Business"}
]




for key,value in enumerate(posts):
    if value["id"] == 3:
        print(key)


posts.pop(2)
print(posts)