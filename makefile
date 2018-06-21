.DEFAULT_GOAL := all

FILES :=                                  \
    RunCollatz                            \
    TestCollatz

# uncomment these three lines when you've created those files
# you must replace GitLabID with your GitLabID
#    .gitlab-ci.yml                        \
#    collatz-tests/GitLabID-RunCollatz.in  \
#    collatz-tests/GitLabID-RunCollatz.out \

.pylintrc:
	pylint --disable=locally-disabled --reports=no --generate-rcfile > $@

collatz-tests:
	git clone git@gitlab.com:gpdowning/cs373-collatz-tests.git

Collatz.html: Collatz.py
	-pydoc -w Collatz

Collatz.log:
	git log > Collatz.log

RunCollatz.pyx: Collatz.py RunCollatz.py .pylintrc
	-mypy   Collatz.py
	-pylint Collatz.py
	-mypy   RunCollatz.py
	-pylint RunCollatz.py
	./RunCollatz.py < RunCollatz.in > RunCollatz.tmp
	-fc RunCollatz.tmp RunCollatz.out

TestCollatz.pyx: Collatz.py TestCollatz.py .pylintrc
	-mypy     Collatz.py
	-pylint   Collatz.py
	-mypy     TestCollatz.py
	-pylint   TestCollatz.py
	-coverage run    --branch TestCollatz.py
	-coverage report -m

all:

clean:
	rm -f  .coverage
	rm -f  .pylintrc
	rm -f  *.pyc
	rm -f  *.tmp
	rm -rf __pycache__
	rm -rf .mypy_cache

config:
	git config -l

docker:
	docker run -it -v $(PWD):/usr/collatz -w /usr/collatz gpdowning/python

format:
	autopep8 -i Collatz.py
	autopep8 -i RunCollatz.py
	autopep8 -i TestCollatz.py

init:
	touch README
	git init
	git add README
	git commit -m 'first commit'
	git remote add origin git@gitlab.com:gpdowning/cs373-collatz.git
	git push -u origin master

pull:
	make clean
	@echo
	git pull
	git status

push:
	make clean
	@echo
	git add .gitignore
	git add .gitlab-ci.yml
	git add Collatz.html
	git add Collatz.log
	git add Collatz.py
	git add makefile
	git add RunCollatz.in
	git add RunCollatz.out
	git add RunCollatz.py
	git add TestCollatz.py
	git commit -m "another commit"
	git push
	git status

run: $(FILES:=.pyx)

scrub:
	make clean
	rm -f  Collatz.html
	rm -f  Collatz.log
	rm -rf collatz-tests

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

versions:
	which     autopep8
	autopep8 --version
	@echo
	which    coverage
	coverage --version
	@echo
	which    git
	git      --version
	@echo
	which    make
	make     --version
	@echo
	which    mypy
	mypy     --version
	@echo
	which    pip
	pip      --version
	@echo
	pip      list
	@echo
	which    pydoc
	pydoc    --version
	@echo
	which    pylint
	pylint   --version
	@echo
	which    python
	python   --version
	@echo
	which    vim
	vim      --version
