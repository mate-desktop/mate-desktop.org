#!/usr/bin/env bash

NIKOLA_ENV="nikola-621"

echo "Deploying mate-desktop.org"

if [ -d ${HOME}/PythonEnvs/${NIKOLA_ENV} ]; then
	echo " - Found Nikola stack."
	source ${HOME}/PythonEnvs/${NIKOLA_ENV}/bin/activate
else
	echo " - ERROR! I couldn't find the Nikola stack. Exitting."
	exit 1
fi

if [ -d ${HOME}/Websites/mate-desktop.org/.git ]; then
	echo " - Found mate-desktop.org Git repository. Pulling..."
	cd ${HOME}/Websites/mate-desktop.org
	git pull
	if [ $? -ne 0 ]; then
		echo " - WARNING! 'git pull' encountered problems."
	fi
else
	echo " - Cloning mate-desktop.org Git repository..."
	${HOME}/Websites
	git clone https://github.com/mate-desktop/mate-desktop.org
	if [ $? -ne 0 ]; then
		echo " - ERROR! 'git clone' encountered problems. Exitting."
		exit 1
	fi
	cd ${HOME}/Websites/mate-desktop.org
fi


# Optionally deep clean before the build.
if [ "${1}" == "clean" ]; then
	nikola clean
	nikola forget
fi

nikola build
nikola deploy
