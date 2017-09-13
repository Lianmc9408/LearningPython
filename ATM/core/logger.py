#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-13 下午12:46

import logging
# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import settings



def logger(log_type):
	logger1 = logging.getLogger(log_type)
	logger1.setLevel(settings.LOG_LEVEL)

	ch = logging.StreamHandler()
	ch.setLevel(settings.LOG_LEVEL)

	log_file = '%s/log/%s' % (settings.BASE_DIR, settings.LOG_TYPES[log_type])
	fh = logging.FileHandler(log_file)
	fh.setLevel(settings.LOG_LEVEL)

	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

	ch.setFormatter(formatter)
	fh.setFormatter(formatter)

	logger1.addHandler(ch)
	logger1.addHandler(fh)

	return logger1
