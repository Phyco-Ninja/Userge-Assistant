# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge-Assistant > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Userge-Assistant/blob/master/LICENSE >
#
# All rights reserved.

from sys import version_info

from pyrogram import __version__ as __pyro_version__  # noqa

__assistant_version__ = "v1"

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"

__license__ = ("[GNU General Public License v3.0]"
               "(https://github.com/UsergeTeam/Userge-Assistant/blob/master/LICENSE)")

__copyright__ = "Copyright (C) 2020 by [UsergeTeam@Github](https://github.com/UsergeTeam)"
