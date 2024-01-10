#!/usr/bin/python3

from __future__ import print_function
import argparse
import base64
from collections import OrderedDict
import datetime
import glob
import json
import os
import platform
import pwd
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import threading
import time
import zipfile
import ezfio

if __name__ == "__main__":
    ezfio.ParseArgs()
    ezfio.CheckFIOVersion()
    ezfio.CheckAIOLimits()
    ezfio.CollectSystemInfo()
    ezfio.CollectDriveInfo()
    ezfio.VerifyContinue()
    ezfio.SetupFiles()
    ezfio.GenerateResultODS()

    print("\nCOMPLETED!\nSpreadsheet file: ")
