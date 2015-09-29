#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pylibmc
Version  : 1.5.0
Release  : 16
URL      : https://pypi.python.org/packages/source/p/pylibmc/pylibmc-1.5.0.tar.gz
Source0  : https://pypi.python.org/packages/source/p/pylibmc/pylibmc-1.5.0.tar.gz
Summary  : Quick and small memcached client for Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pylibmc-python
BuildRequires : libmemcached-dev
BuildRequires : memcached
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pkgconfig(zlib)
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : zlib-dev

%description
`pylibmc` is a Python client for `memcached <http://memcached.org/>`_ written in C.

%package python
Summary: python components for the pylibmc package.
Group: Default

%description python
python components for the pylibmc package.


%prep
%setup -q -n pylibmc-1.5.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
