""" 
# ===========================================================================
# **pyion** provides a Python interface to JPL's Interplantary Overlay Network 
# (ION) via a Proxy class that allows create Endpoints through which you can
# send or receive bytes, bytearrays and memoryviews. They operate in a 
# manner similar to how TCP/UDP sockets operate.
#
# **pyion** also provides similar abstractions to interface with
# - LTP
# - CFDP
# - SDR and PSM
# - Management functions such as add/delete a contact
#
# **NONE OF THE PRIMITIVES PROVIDED IN PYION ARE THREAD-SAFE**
#
# **pyion** does not substitute traditional ION management functions such as ``ionadmin``
# or ``bpadmin`` since only a small subset functionality is implemented. Therefore, to
# use pyion, it is required that
# (1) ION be installed in the host computer
# (2) One or multiple ION nodes are already instantiated and running.
#
# **pyion's** documentation is available at https://pyion.readthedocs.io/en/latest/
#
# Author: Marc Sanchez Net
# Date:   04/17/2019
# Copyright (c) 2019, California Institute of Technology ("Caltech").  
# U.S. Government sponsorship acknowledged.
# ===========================================================================
"""

# General imports
import os
import warnings    

# This pulls up import so that from the user you can do
# ``import pyion`` instead of having to do one of the following:
#   - ``from pyion import pyion``
#   - ``import pyion.pyion as pyion``
from pyion.proxies import *
from pyion.utils import *
from pyion.constants import *

# Handle case where _mgmt was not compiled during setup
try:
    from pyion.mgmt import *
except ImportError:
    warnings.warn("Pyion's management module is not installed.")

# Must be set if multiple ION nodes are run on the same host.
ION_NODE_LIST_DIR = None