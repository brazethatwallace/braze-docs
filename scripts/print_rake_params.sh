#!/bin/bash
#
# Prints all supported parameters for 'rake', which includes syntax for:
# non-english languages, markdown embeds, and partner tiles.
# 
# Usage: ./bdocs rake

cat << EOF
These are all the supported parameters for 'rake':

# for 'en' language:
rake

# for other languages:
rake de
rake es
rake fr
rake ja
rake ko
rake pt_br

# Partner hub (Sanity): on by default when partner_api is true in _config.yml. Skip: PARTNER_API=false rake

# to render content in '{% markdown_embed %}' tags:
MARKDOWN_API=true rake
EOF
