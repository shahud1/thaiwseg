#!/usr/bin/env python
# -*- coding: utf-8 -*-
## IF THIS CODE DOESN'T RUN, RUN SSL COMMAND FROM PYTHON SETTINGS

from mtranslate import translate


def main():
    to_translate = 'Try to organise your writing so that your ideas are developed logically and sequentially. If you find that a paragraph contains more than one idea, you may need to reorganise your essay so that your ideas are developed more logically.'
    print(translate(to_translate))
    print(translate(to_translate, 'tr'))
    print(translate(to_translate, 'th'))

if __name__ == '__main__':
    main()
