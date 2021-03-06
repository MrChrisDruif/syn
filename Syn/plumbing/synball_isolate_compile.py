# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.policy.source_package as S
import Syn.source_tarball
import Syn.exceptions
import Syn.plumber
import Syn.common
import Syn.sh

PLUMBING_NAME = "synball-isolate-compile"

def run(args):
	"""
	Move all sources to a temp location and build there. This helps
	protect the CWD from dammage during a test build
	"""
	try:
		if not Syn.sh.xists(args[2]):
			raise KeyError('offset 2')

		cwd = Syn.common.getcwd()

		wd = Syn.common.getTempLocation()
		if Syn.sh.xists(wd):
			raise Syn.exceptions.ConflictException("Fuck all, dir exists: %s" % wd)

		stb = Syn.source_tarball.source_tarball(args[2])
		fullid   = stb.package_fullid()
		upstream = stb.upstream_tarball_id()

		needed_filez = [
			fullid + S.XTN,
			upstream
		]

		Syn.sh.mkdir(wd)
		for x in needed_filez:
			Syn.sh.cp(x, wd)

		Syn.sh.cd(wd)

		binary = Syn.synd.build(fullid + S.XTN)

		Syn.sh.cd(cwd)
		Syn.sh.mv(binary, cwd)
		Syn.sh.rmdir(wd)
	except KeyError as e:
		raise Syn.exceptions.FileNotPresentException("Fucking asshole. No file: %s" % e)
Syn.plumber.registerRoute(PLUMBING_NAME, run)

