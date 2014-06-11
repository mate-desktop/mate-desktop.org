#!/usr/bin/env bash

NIKOLA_ENV="nikola-701"

clone ()
{
	echo " - Cloning mate-desktop.org Git repository..."
	if [ -d mate-desktop.org ]; then
		rm -rf "mate-desktop.org"
	fi

	git clone --depth=1 https://github.com/mate-desktop/mate-desktop.org
	if [ $? -ne 0 ]; then
		echo " - ERROR! 'git clone' encountered problems. Exitting."
		exit 1
	fi
}

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

	git fsck-objects --full
	if [$? -ne 0 ]; then
		echo " - WARNING! 'git fsck-objects' failed."
		echo " - WARNING! attempting to do a fresh clone."
		clone
	fi

	# Discard any file modifications
	git checkout master -f
else
	cd ${HOME}/Websites
	clone
fi

cd ${HOME}/Websites/mate-desktop.org

# Optionally deep clean before the build.
if [ "${1}" == "clean" ]; then
	nikola clean
	nikola forget
	rm -rfv cache/*
	rm -rfv output/*
fi

nikola build
nikola deploy
