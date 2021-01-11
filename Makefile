## environment : Create the project's virtual environment with conda
.PHONY : env
env :
	conda create -f environment.yml
	conda activate arcade

## install     : Install project package locally and install pre-commit.
.PHONY : install
install : env
	pip-compile requirements.in
	pip install -r requirements.txt
	flit install --pth-file
	pre-commit install

## help        : Documentation for make targets.
.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<
