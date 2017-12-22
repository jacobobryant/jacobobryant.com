#!/bin/bash
./update_static.sh
hugo && rsync -av --delete ./public/ jacobobryant.com:public/
