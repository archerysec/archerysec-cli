#!/usr/bin/env python

"""
======================= START OF LICENSE NOTICE =======================
  Copyright (C) 2021 ArcherySec. All Rights Reserved
  NO WARRANTY. THE PRODUCT IS PROVIDED BY DEVELOPER "AS IS" AND ANY
  EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL DEVELOPER BE LIABLE FOR
  ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
  DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
  GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
  IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
  OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THE PRODUCT, EVEN
  IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
======================== END OF LICENSE NOTICE ========================
  Primary Author: Anand Tiwari
"""
from datetime import datetime


__title__ = 'archerysec-cli'
__authors__ = 'Anand Tiwari'
__copyright__ = f'Copyright {datetime.now().year} Anand Tiwari, ArcherySec'
__version__ = '3.1.12'
__version_info__ = tuple(int(i) for i in __version__.split('.'))
__all__ = [
    '__title__',
    '__authors__',
    '__copyright__',
    '__version__',
    '__version_info__',
]