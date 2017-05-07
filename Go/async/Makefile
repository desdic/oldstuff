default: build

BUILDDATE=$(shell date +'%Y%m%d')
GOC=go
GOOS=""
GOARCH=""
GOGC=
GOPATH=$(shell pwd)
PACKAGE = async
LIBS = monitor
RUNPARA=-config samples/config.json

.PHONY: default build

build:
			GOOS=${GOOS} GOARCH=${GOARCH} GOGC=${GOGC} GOPATH=${GOPATH} ${GOC} install $(PACKAGE)

run:format
			GOPATH=${GOPATH} ${GOC} run -race src/$(PACKAGE)/$(PACKAGE).go ${RUNPARA}

clean:
			go clean
			rm -f bin/$(PACKAGE)
