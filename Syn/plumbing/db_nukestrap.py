# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.policy.db as D

import Syn.package_registry
import Syn.plumber
import Syn.sh

PLUMBING_NAME = "_nukestrap"

# Need to add in reset-able roots

PREFIX = ""

def run(args):
	"""
	@WARNING: DO NOT USE ME.
	DO NOT USE THIS FUNCTION.
	**SERIOUSLY**. BABIES WILL DIE, YOUR SYSTEM WILL CRY,
	AND I'LL FIND YOU, GUY.

	SERIOUSLY
	"""
	ROOT_PATH = PREFIX + D.DB_ROOT
	if not Syn.sh.xists(ROOT_PATH):
		Syn.sh.mkdir(ROOT_PATH)
	Syn.package_registry.do_not_call_me_nukestrap_database_files(ROOT_PATH)

Syn.plumber.registerRoute(PLUMBING_NAME, run)

