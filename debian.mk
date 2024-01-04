PREFIX ?= /usr/local
all: dependencies python
python: Makefile
	$(MAKE) -f $< -j
Makefile: configure
	./$< --prefix=$(PREFIX)
dependencies:
	sudo apt-get install build-essential gdb lcov pkg-config \
	 libbz2-dev libffi-dev libgdbm-dev libgdbm-compat-dev liblzma-dev \
	 libncurses5-dev libreadline6-dev libsqlite3-dev libssl-dev \
	 lzma lzma-dev tk-dev uuid-dev zlib1g-dev
%: Makefile
	$(MAKE) -f $< "$@"
