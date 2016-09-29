# This is a Makefile for the "make" utility.
#
# This file is not part of the exercises for class, it is for the instructors
# to automate building the exercises.
PYTHON ?= python3

LAB_TOOLS = .lab-tools

write-check-solutions:
	$(PYTHON) $(LAB_TOOLS)/proc_solutions.py write-solutions
	$(PYTHON) code/tests/test_spm_funcs.py
	$(PYTHON) code/tests/test_detectors.py
	$(PYTHON) $(LAB_TOOLS)/proc_solutions.py write

check:
	$(PYTHON) $(LAB_TOOLS)/proc_solutions.py check

write:
	$(PYTHON) $(LAB_TOOLS)/proc_solutions.py write

