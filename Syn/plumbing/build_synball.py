# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.plumber
import Syn.synd
import Syn.sh

PLUMBING_NAME = "synball-compile"

def run(args):
	"""
	**Needed argument**: path to a synball

	Compile a Syn sourceball (synball) in the
	current working directory. 
	"""
	try:
		if Syn.sh.xists(args[2]):
			Syn.synd.build(args[2])
		else:
			raise Syn.exceptions.SynShittyPlumbingException("Synball does not exist!: %s" % args[2])
	except Syn.exceptions.BuildFailureException as e:
		print "Build failure!!!! %s" % e
	except IndexError as e:
		raise Syn.exceptions.SynShittyPlumbingException("You forgot an argument!: %s" % str(e))

Syn.plumber.registerRoute(PLUMBING_NAME, run)

