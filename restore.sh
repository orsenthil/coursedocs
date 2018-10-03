#!/usr/bin/env bash

# die on error
set -e

# https://developer.travis-ci.org/resource/builds#Builds
echo 'Retrieving last successful Travis-CI build...'
for row in $(curl -H "Travis-API-Version: 3" -H "User-Agent: API Explorer" -H "Authorization: token $TRAVISCI_API_KEY" https://api.travis-ci.org/builds?limit=10 | jq -r '.builds[] | @base64'); do
    _jq() {
        echo ${row} | base64 --decode | jq -r ${1}
    }

    if [ $(_jq '.state') == "passed" ]; then
        good_build=$(_jq '.commit.sha')
        break
    fi
done

# https://www.netlify.com/docs/api/#deploys
echo "Retrieving Netlify deploy for Travis-CI build ${good_build}..."
for row in $(curl -H "Authorization: Bearer $NETLIFY_PUBLISH_KEY" https://api.netlify.com/api/v1/sites/coursedocs.netlify.com/deploys | jq -r '.[] | @base64'); do
    _jq() {
        echo ${row} | base64 --decode | jq -r ${1}
    }

    deploy_commit=$(_jq '.commit_ref')

   if [ "$deploy_commit" == "$good_build" ]; then
        good_deploy=$(_jq '.id')
   fi
done

# https://www.netlify.com/docs/api/#deploys
echo "Publishing Netlify build ${good_deploy}..."
curl -X POST -H "Authorization: Bearer $NETLIFY_PUBLISH_KEY" -d "{}" "https://api.netlify.com/api/v1/sites/coursedocs.netlify.com/deploys/${good_deploy}/restore"
