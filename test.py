#Function to get the value of a key_path

def get_nested(data, key):
    if key and data:
        element  = key[0]
        #print(element)
        if element:
            value = data.get(element)
            #print(value)
            return value if len(key) == 1 else get_nested(value, key[1:])

obj={"a" : {"b" : {"c" : "d"}}}
key_path= "a/b/c"
paths = key_path.split("/")
x=get_nested(obj, paths)
print(x)
