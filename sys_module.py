import sys

'''stderr use for error, its color is red'''
sys.stderr.write('This is stderr text')
sys.stderr.flush()

'''stdout use for any thing, its color is blue'''
sys.stdout.write('This is stdout text\n')

'''Print file path'''
print(sys.argv)
'''It is also use in command line argument'''



