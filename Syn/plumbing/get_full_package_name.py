# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.exceptions
import Syn.plumber
import Syn.log

PLUMBING_NAME = "synball-pkgfullid"

def run(args):
	"""
	Get the package's fullid. Verbosity on logging
	has been set to super-quiet (Milford Academy mode)
	so this can be safely used in bash-subcommand syntax.
	"""
	Syn.log.VERBOSITY = -1
	try:
		if Syn.sh.xists(args[2]):
			stb = Syn.source_tarball.source_tarball(args[2])
			otb = stb.package_fullid()
			print otb
		else:
			raise Syn.exceptions.SynShittyPlumbingException("Synball does not exist!: %s" % args[2])
	except IndexError as e:
		raise Syn.exceptions.SynShittyPlumbingException("You forgot an argument!: %s" % str(e))

Syn.plumber.registerRoute(PLUMBING_NAME, run)

