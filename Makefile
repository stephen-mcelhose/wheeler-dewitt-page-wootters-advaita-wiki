index:
	python3 .agents/skills/doc-manager/scripts/build_index.py .
validate:
	python3 .agents/skills/doc-manager/scripts/validate.py .
web-data: index
	python3 scripts/generate_web_data.py
web-install:
	cd web && bun install
web-dev: web-data
	cd web && bun run dev
web-build: web-data
	cd web && bun run build
explore: web-dev
package: clean index validate
	python3 scripts/package.py
clean:
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	rm -f viewer/wiki-data.json web/src/data.ts
