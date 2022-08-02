# ------------------------------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------------------------------

# This script parses release version from Git tag and set the parsed version to
# environment variable, REL_VERSION.

import os
import sys

gitRef = os.getenv("GITHUB_REF")
tagRefPrefix = "refs/tags/v"

with open(os.getenv("GITHUB_ENV"), "a") as githubEnv:
    if gitRef is None or not gitRef.startswith(tagRefPrefix):
        githubEnv.write("REL_VERSION=edge\n")
        print(f"This is daily build from {gitRef}...")
        sys.exit(0)

    releaseVersion = gitRef[len(tagRefPrefix):]
    releaseNotePath = f"docs/release_notes/v{releaseVersion}.md"

    if gitRef.find("-rc.") > 0:
        print(f"Release Candidate build from {gitRef}...")
    else:
        # Set LATEST_RELEASE to true
        githubEnv.write("LATEST_RELEASE=true\n")
        print(f"Release build from {gitRef}...")

    githubEnv.write(f"REL_VERSION={releaseVersion}\n")
