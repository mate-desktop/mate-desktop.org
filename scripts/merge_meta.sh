#!/usr/bin/env bash

for DIR in blog pages
do
	echo ${DIR}
	mkdir -p ${HOME}/Merged/${DIR}
	for META in ${DIR}/*.meta
	do
		MARK=`basename ${META} .meta`.md
		echo ${META}
		echo ${MARK}

		TITLE=`sed -n 1p ${META}`
		SLUG=`sed -n 2p ${META}`
		DATE=`sed -n 3p ${META}`
		TAGS=`sed -n 4p ${META}`
		cat <<HEADER > ${HOME}/Merged/${DIR}/${MARK}
<!--
.. link:
.. description:
.. tags: ${TAGS}
.. date: ${DATE}
.. title: ${TITLE}
.. slug: ${SLUG}
-->

HEADER
		cat ${DIR}/${MARK} >> ${HOME}/Merged/${DIR}/${MARK}
	done
done
