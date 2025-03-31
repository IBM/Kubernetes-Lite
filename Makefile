# Makefile for gopy pkg generation of python bindings to python_go_kubernetes_client
# File is generated by gopy (will not be overwritten though)
# gopy pkg -author=Michael Honaker -email=michael.honaker@ibm.com -name=python_go_kubernetes_client github.ibm.com/Michael-Honaker/kubernetes-go-python-client/wrapper/pkg

PYTHON=python
PIP=$(PYTHON) -m pip
LOCAL_PY_CFLAGS=$(shell python3.11-config --includes)
LOCAL_PY_LDFLAGS=$(shell python3.11-config --ldflags)

all: check

################################## GENERATION ##################################
gen: 
	export GOWORK=off && \
	rm -rf kubernetes_lite/wrapper/* && \
	cd kubernetes_lite && \
	gopy pkg -no-make -author="Michael Honaker" -email="michael.honaker@ibm.com" -name=wrapper github.ibm.com/Michael-Honaker/kubernetes-lite/kubernetes_lite/go_wrapper/pkg/client github.ibm.com/Michael-Honaker/kubernetes-lite/kubernetes_lite/go_wrapper/pkg/envtest/setup github.ibm.com/Michael-Honaker/kubernetes-lite/kubernetes_lite/go_wrapper/pkg/envtest/server && \
	python3 ../scripts/post_gen_cleanup.py ./ wrapper

license-gen:
	pip-licenses --format=plain-vertical --with-license-file -p kubernetes_lite -p orjson > ./kubernetes_lite/licenses/PYTHON_LICENSES && \
	cd kubernetes_lite/go_wrapper && \
	go-licenses save --save_path ../licenses/go ./...


##################################### BUILD ####################################
local-build:
	export GOWORK=off && \
	rm -rf kubernetes_lite/wrapper/_wrapper.*.* && \
	cd kubernetes_lite/wrapper && \
	CGO_CFLAGS_ALLOW="-O.*" CGO_CFLAGS="${LOCAL_PY_CFLAGS}" CGO_LDFLAGS="${LOCAL_PY_LDFLAGS} -Wl,-undefined,dynamic_lookup" go build -buildmode=c-shared -o _wrapper.so '-ldflags=-s -w'

python-build:
	rm -rf dist
	python3 -m build

local-docker-build:
	docker build --target=local --file=scripts/Dockerfile .

docker-build: python-build local-docker-build

################################ FORMAT AND LINT ###############################
format: 
	ruff format && ruff check --fix
check-format:
	ruff format --check && ruff check

##################################### DOCS #####################################
docs-gen:
	python3 -m mkdocs build --config-file ./docs/mkdocs.yaml --site-dir ./site

docs-serve:
	python3 -m mkdocs serve --config-file ./docs/mkdocs.yaml
##################################### SECRETS ##################################

update-secrets:
	detect-secrets scan --update .secrets.baseline --exclude-files '(go.sum|tests\/performance\/data\/.*)'
check-secrets:
	detect-secrets audit --report  .secrets.baseline

################################ Checks ###############################
check: check-format check-secrets