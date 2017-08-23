import cProfile
from main import main
cProfile.run("main(1)", sort="cumtime")
