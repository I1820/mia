install:
	pip3 install -r requirements.txt
develop:
	pip3 install -r dev-requirements.txt
docker:
	sudo docker build . -t aolab/i1820
.PHONY: install develop docker
