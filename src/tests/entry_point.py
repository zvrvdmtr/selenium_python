import argparse
import os
from pathlib import Path
import sys
import logging

source_folder = Path(__file__).parents[1].resolve()
sys.path.append(str(source_folder))

import utilities.custom_logger as cl

log = cl.customLogger(logging.DEBUG)
parser = argparse.ArgumentParser()
browsers = ['chrome', 'firefox', 'safari']
projects = ['market', 'bank', 'intranet']
parser.add_argument("browser")
parser.add_argument("project")
parser.add_argument("test_path")
args = parser.parse_args()
path = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), args.project), args.test_path)
if args.browser not in browsers:
    log.error('Browser "%s" is not supported' % args.browser)
elif args.project not in projects:
    log.error('There is no project as "%s"' % args.project)
elif os.path.exists(path) is False:
    log.error('There is no such path as %s' % path)
else:
    log.info('Starting browser "%s", project "%s" and test path "%s"' % (args.browser, args.project, path))
    os.system('pytest -s -v -p no:cacheprovider --no-print-logs --browser %s --project %s %s' % (args.browser, args.project, path))

