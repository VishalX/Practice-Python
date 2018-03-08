# "is" & "is not" should be used for special constants as True, False, None !

foo = 1
bar = None

if foo is None:
    print("'foo' is None")
else:
    print("'foo' is not None, it is :", foo)

if bar is not None:
    print("'bar' is not None, it is :", bar)
else:
    print("'bar' is None")