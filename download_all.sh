#!/usr/bin/env bash
set -euxo pipefail

# Download the first 100 repos, in serial so GitHub doesn't get mad.
# Max results per page is 100. See https://developer.github.com/v3/#pagination
curl -s "https://api.github.com/orgs/unimorph/repos?per_page=100&page=1" | 
  grep ssh_url | 
  grep -oP 'git@github.com:unimorph/.{3}.git' |  # Pattern only matches language repos, ignoring utility repos.
  xargs -I@ bash -c "git clone @; sleep 5"

# Download the rest.
curl -s "https://api.github.com/orgs/unimorph/repos?per_page=100&page=2" | 
  grep ssh_url | 
  grep -oP 'git@github.com:unimorph/.{3}.git' | 
  xargs -I@ bash -c "git clone @; sleep 5"
