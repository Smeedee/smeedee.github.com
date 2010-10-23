# -*- coding: utf-8 -*-

import os
import codecs

from mako.lookup import TemplateLookup
from mako.exceptions import RichTraceback


OUTPUT_FOLDER = '.'
CONTENT_FOLDER = 'content'
FILE_ENCODING = 'utf-8'

content = TemplateLookup([CONTENT_FOLDER],
                                 input_encoding=FILE_ENCODING, 
                                 output_encoding=FILE_ENCODING, 
                                 encoding_errors='replace')

for file_name in os.listdir(CONTENT_FOLDER):
    if file_name.endswith('.html'):
        try:
            page = content.get_template(file_name)
            with codecs.open('/'.join([OUTPUT_FOLDER, file_name]), encoding=FILE_ENCODING, mode='w') as output_file:
                output_file.write(page.render_unicode())
        except:
            traceback = RichTraceback()
            for (filename, lineno, function, line) in traceback.traceback:
                print "File %s, line %s, in %s" % (filename, lineno, function)
                print line, "\n"
            print "%s: %s" % (str(traceback.error.__class__.__name__), traceback.error)
