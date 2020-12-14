import re

import numpy as np
from math import lcm, prod

from copy import deepcopy

from collections import namedtuple, deque, defaultdict
from itertools import product, permutations

from pulp import LpMinimize, LpProblem, PULP_CBC_CMD, LpStatus, lpSum, LpVariable, LpInteger

import pretty_errors
pretty_errors.configure(
    separator_character = '*',
    filename_display    = pretty_errors.FILENAME_EXTENDED,
    line_number_first   = True,
    display_link        = True,
    lines_before        = 5,
    lines_after         = 2,
    line_color          = pretty_errors.RED + '> ' + pretty_errors.default_config.line_color,
    code_color          = '  ' + pretty_errors.default_config.line_color,
)