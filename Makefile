explore: index
	python3 start-wiki.py
validate:
	python3 .agents/skills/doc-manager/scripts/validate.py .
index:
	python3 .agents/skills/doc-manager/scripts/build_index.py .
package: clean index validate
	python3 scripts/package.py
clean:
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	rm -f viewer/wiki-data.json
