import cProfile
from main import main
cProfile.run("main(2)", sort="cumtime")