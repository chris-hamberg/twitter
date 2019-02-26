import shutil, pathlib, sys, os

top = pathlib.Path(sys.argv[0]).absolute()
top = os.sep.join(str(top).split(os.sep)[:-2])

for root, directory, file in os.walk(top):
    for branch in directory:
        if '__pycache__' in branch:
            shutil.rmtree(os.path.join(root, branch))

os.system('tree')
