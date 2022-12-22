import logging

try:
    print('-'*40)
    raise TypeError
    print('-'*40)
except TypeError as e:
    logging.exception("Observed error ")
