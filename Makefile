.PHONY: test i18n

PY = $(wildcard *.py) $(wildcard */*.py) $(wildcard */*/*.py)
HTML = $(wildcard *.html) $(wildcard */*.html) $(wildcard */*/*.html)

test:
	nosetests

i18n: translations/messages.pot
	
translations/messages.pot: $(PY) $(HTML)
	pybabel extract -F translations/babel.cfg -o translations/messages.pot .
	pybabel update -i translations/messages.pot -d translations
	pybabel compile -d translations

example:
	rm inventory.db
	sqlite3 inventory.db <schema.sql
	sqlite3 inventory.db <test/content.sql
