
from core_f import Core
import gc
#import pprint
#import sys

if __name__ == '__main__':
    with Core() as root:
        #print(sys.modules)
        root.on_content_changed()
        root.mainloop()
        print("Destroying")
        del root

    gc.collect()
