import sys
import os
import logging
import logging.config
import copy
import types

import settings

__version__ = "1.0"

def t1(args):
    import requests
    
    url = "http://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={appid}"

    city = "Melbourne"
    country = "au"
    fURL = url.format(city_name=city, country_code=country, appid=settings.keyValue)
    print fURL

    r = requests.get(fURL)

    print r.text



def _showAll(args):
    all = copy.copy(args.items())
    print "Script version", __version__

    for name, f in all:
        if isinstance(f, types.FunctionType):
            if not name.startswith("_"):
                print "******************************"
                print "Function ** %s **" % name
                print "******************************"
                if f.__doc__ is not None:
                    print '\t', f.__doc__



if __name__ == '__main__':
    REVISION = "$LastChangedRevision: 10220 $"
    if os.path.exists("logging.conf"):
        logging.config.fileConfig("logging.conf")
        logging.info("Using logging.conf for logging settings.")
    else:
        logging.basicConfig(level=logging.INFO)

    logging.info('Version =%s', REVISION)
    if len(sys.argv) < 2:
        _showAll(locals())
        os._exit(0)

    # Globals
    fnName = sys.argv[1]
    logging.info('Function *** %s ***', fnName)

    if fnName not in locals():
        logging.error("Unknown function '%s'", fnName)
        os._exit(0)

    n = locals()[fnName](args=sys.argv[2:])
    sys.stdout.flush()

    logging.info('** bye')
    os._exit(0)
