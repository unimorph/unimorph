#!/usr/bin/env bash
set -euxo pipefail

# Getting "Permission denied (publickey)."?
# Make sure that you've registered your public key with GitHub!

# Max results per page is 100. See https://developer.github.com/v3/#pagination
# So we concatenate the 100-item lists.
# If there are ever more than 200 repos, we should increment this number.
for i in {1..2}
do
  curl -s "https://api.github.com/orgs/unimorph/repos?per_page=100&page=$i"
done |
  grep ssh_url | 
  grep -o 'git@github.com:unimorph/[a-z]\{3\}.git' |  # Pattern only matches language repos, ignoring utility repos.
  xargs -I@ bash -c "git clone @; sleep 5"
