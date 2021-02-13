# Copyright (c) AIRBUS and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import fnmatch
import os
import sys

for p in sys.path:
    for dirpath, dirs, files in os.walk(p):
        for filename in fnmatch.filter(files, "__skdecide_hub_cpp*"):
            sys.path.append(dirpath)