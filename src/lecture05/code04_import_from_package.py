
from package.util.db import connect
from package import run

print(connect('url', 5000, 'user', 'passwd'))
run.main()


# the bellow won't work
import folder.run
folder.run.main()