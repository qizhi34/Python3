#!/usr/bin/env bash

commit_comment=$1
if [ -z "${commit_comment}" ]; then
    timestamp=`date +"%Y%m%d_%H%M%S"`
    commit_comment="modify at ${timestamp}"
fi

git commit -am "${commit_comment}"
git push