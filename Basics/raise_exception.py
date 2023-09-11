def process_file():
   try:
       f=open("data.txt")
       x=1/0
   except FileNotFoundError as e:
       print("inside except")
   finally:
       print("cleaning up file")
       f.close()

process_file()


# Another Example

class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def print_exception(self):
        print('user Defined Exception: ', self.msg)

try:
    raise Accident("Crash between two cars")
except Accident as e:
    e.print_exception()