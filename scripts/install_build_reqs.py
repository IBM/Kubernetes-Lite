# ***************************************************************** #
# (C) Copyright IBM Corporation 2024.                               #
#                                                                   #
# The source code for this program is not published or otherwise    #
# divested of its trade secrets, irrespective of what has been      #
# deposited with the U.S. Copyright Office.                         #
# ***************************************************************** #
# SPDX-License-Identifier: Apache-2.0
"""This is a helper script to install the build system dependencies. For now this
just installs the correct version of golang. Due to where this is ran we can not have
any external dependencies (e.g. requests)
"""

import platform
import shutil
import subprocess
import tempfile
from pathlib import Path
from urllib.request import urlopen

# Base settings for go/src/dest
GO_VERSION = "1.23.7"
GO_BASE_URL = "https://go.dev/dl/go{version}.{system}-{arch}.tar.gz"
DEST_PATH = tempfile.gettempdir()

# Parse the system architecture and platform
system: str | None = None
arch: str | None = None
if platform.machine() in {"x86_64", "amd64"}:
    arch = "amd64"
elif platform.machine() in {"i386", "i686"}:
    arch = "386"
elif platform.machine() in {"aarch64", "arm64", "armv8b", "armv8l", "aarch64_be"}:
    arch = "arm64"
else:
    raise ValueError(f"Unknown machine platform {platform.machine()}")

if platform.system() == "Linux":
    system = "linux"
elif platform.system() == "Darwin":
    system = "darwin"
elif platform.system() == "Windows":
    system = "windows"
else:
    raise ValueError(f"Unknown machine system {platform.system()}")

# Setup a directory to download the tar to
with tempfile.TemporaryDirectory() as temp_dir:
    temp_path = Path(temp_dir)
    tar_gz_file = temp_path / "go.tar.gz"

    # Template the url and send the request
    go_url = GO_BASE_URL.format(version=GO_VERSION, arch=arch, system=system)
    print(f"# Attempting to download go src from: {go_url}")
    with urlopen(go_url) as response:
        tar_gz_file.write_bytes(response.read())

    print(f"# Attempting to extract archive to: {DEST_PATH}")
    shutil.unpack_archive(tar_gz_file, DEST_PATH)

# Ensure go is usable. ! Note this requires the path be set externally
subprocess.run(["go", "version"], check=True, capture_output=True)

# Print the path used for installation
print("# Install path for go: ")
print(f"export PATH=$PATH:{DEST_PATH}/go/bin")
