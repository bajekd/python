'''Based on: https://www.youtube.com/watch?v=3dt4OGnU5sM&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=21&t=0s
and https://www.youtube.com/watch?v=bD05uGo_sVI&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=37&t=0s'''
import timeit

run_only_once = """
data = [x for x in range(1000000)]
"""

code_to_test_generator = '''
cubes = (x*x*x for x in data)
sum = 0
'''

code_to_test_list = '''
cubes = [x * x * x for x in data]
sum = 0
'''

# print(timeit.timeit(stmt=code_to_test, setup='data = [x for x in range(10)]', number=10))
print(f"\nGenerator - Kod działa w czasie: "
      f"{timeit.timeit(stmt=code_to_test_generator, setup=run_only_once,number=50)}")

print(f"\nLista - Kod działa w czasie: "
      f"{timeit.timeit(stmt=code_to_test_list, setup=run_only_once, number=50)}")









