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

def main():
    """Generates html-pages from all *.html content pages
    found in the content folder."""
    for file_name in os.listdir(CONTENT_FOLDER):
        if file_name.endswith('.html'):
            try_generate_page(file_name)

def try_generate_page(file_name):
    try:
        page = content.get_template(file_name)
        with codecs.open('/'.join([OUTPUT_FOLDER, file_name]), encoding=FILE_ENCODING, mode='w') as output_file:
            output_file.write(page.render_unicode())
        print "*** Successfully generated page: %s" % (file_name)
    except:
        traceback = RichTraceback()
        print_traceback(traceback)

def print_traceback(traceback):
    for (filename, line_number, function, line) in traceback.traceback:
        print "File %s, line %s, in %s" % (filename, line_number, function)
        print line, "\n"
    print "%s: %s" % (str(traceback.error.__class__.__name__), traceback.error)

if __name__=="__main__":
    main()
