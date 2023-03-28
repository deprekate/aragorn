default:
	python3 -m pip install ../aragorn/ --user

clean:
	rm -fr build
	rm -fr dist
	rm -fr aragorn.egg-info
	python3 -m pip uninstall aragorn -y

