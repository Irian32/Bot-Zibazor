from botzibazor import Botzibazor
import os

token_bazibazor_prod = os.environ['TOKEN_PROD']
token_bazibazot_test = os.environ['TOKEN_TEST']

botzibazor = Botzibazor(token_bazibazor_prod)
botzibazor.start()


