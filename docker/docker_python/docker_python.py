from skilletlib.skilletLoader import SkilletLoader

sl = SkilletLoader()
skillet = sl.load_skillet_from_path('.')
out = skillet.execute(dict())
print(out)
