#!c:\users\jorge.rubio\documents\estudio\cursosplatzi\python3\aplicacionventaspoo\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pv','console_scripts','pv'
__requires__ = 'pv'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pv', 'console_scripts', 'pv')()
    )
