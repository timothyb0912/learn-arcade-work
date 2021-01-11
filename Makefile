## environment : Create the project's virtual environment with conda and mamba
.PHONY : env
env :
	conda install mamba
	mamba env create -n arcade -f environment.yml

## install     : Install project package locally and install pre-commit.
.PHONY : install
install :
	pip-compile requirements.in
	pip install -r requirements.txt
	flit install --pth-file
	pre-commit install

## help        : Documentation for make targets.
.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<
