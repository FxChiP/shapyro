import shapyro

a = shapyro.Get["a"]
b = {"a": 1}

print("a is {a}".format(a=a(b)))

a = {
    "one": {
        "attr_a": "foo",
        "attr_b": ["works", "with", "arrays"]
    },
    "five": {
        "attr_c": ("and", "with", "tuples")
    }
}

b = {
    "map_test": shapyro.Template("{one[attr_b][0]} {five[attr_c][2]}")
}

c = shapyro.port(a, b)
print(c)


class SomeObj(object):
    OBJ_PROPERTY = ["bar", "baz", "ping"]


a = SomeObj()
b = {
    "from_obj_attr_array_test": shapyro.Get.OBJ_PROPERTY[2],
    "boop": shapyro.OnlyIfExists(shapyro.FromAttr("boop"))
}

c = shapyro.port(a, b)
print(c)

a.boop = "hi!"
c = shapyro.port(a, b)
print(c)
