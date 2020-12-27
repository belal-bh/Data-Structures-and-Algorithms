import random
import sys
import os

main_py = 'maximum_pairwise_product.py'
main_file = 'main.txt'
generator_py = 'gen.py'
input_file = 'input.txt'
model_py = 'model.py'
model_file = 'model.txt'

# accept the number of tests as a command line parameter
tests = int(sys.argv[1])
# accept the parameter for the tests as a command line parameter
n = int(sys.argv[2])

for i in range(tests):
    print("Test #" + str(i))
    # run the generator gen.py with parameter n and the seed i
    os.system(f"python {generator_py} {n} {i} > {input_file}")
    # run the model solution model.py
    # Notice that it is not necessary that solution is implemented in
    # python, you can as well run ./model <input.txt >model.txt for a C++
    # solution.
    os.system(f"python {model_py} < {input_file} > {model_file}")
    # run the main solution
    os.system(f"python {main_py} < {input_file} > {main_file}")


    # read the output of the model solution:
    with open(model_file) as f:
        model = f.read()
    print("Model: ", model)
    # read the output of the main solution:
    with open(main_file) as f:
        main = f.read()
    print("Main: ", main)
    if model != main:
        print(f"Wrong! {model} != {main}")
        break