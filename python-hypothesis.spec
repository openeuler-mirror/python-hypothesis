%{?python_enable_dependency_generator}
Name:           python-hypothesis
Version:        3.66.11
Release:        2
Summary:        based testing for python code
License:        MPLv2.0
URL:            https://github.com/HypothesisWorks/hypothesis-python
Source0:        %{url}/archive/hypothesis-python-%{version}/hypothesis-%{version}.tar.gz
Patch0:         hypothesis-3.12.0-offline.patch
BuildRequires:  python-sphinx
BuildArch:      noarch

%description
This package provides a library called hypothesis for testing Python code,
which has more examples and is based on the Haskell library, Quickcheck,
which is used to integrate directly into your existing Python unit testing work.

%package     -n python2-hypothesis
Summary:        based testing for python code
%{?python_provide:%python_provide python2-hypothesis}
BuildRequires:  python2-devel python2-setuptools python2dist(attrs)

%description -n python2-hypothesis
This package provides a library called hypothesis for testing Python code,
which has more examples and is based on the Haskell library, Quickcheck,
which is used to integrate directly into your existing Python unit testing work.
Python 2 version.

%package     -n python3-hypothesis
Summary:        based testing for python code
%{?python_provide:%python_provide python3-hypothesis}
Obsoletes:      platform-python-hypothesis < %{version}-%{release}
BuildRequires:  python3-devel python3-setuptools python3dist(attrs)

%description -n python3-hypothesis
This package provides a library called hypothesis for testing Python code,
which has more examples and is based on the Haskell library, Quickcheck,
which is used to integrate directly into your existing Python unit testing work.
Python 3 version.

%package        help
Summary:        help document for the python-hypothesis

%description    help
Help document for the python-hypothesis

%prep
%autosetup -n hypothesis-hypothesis-python-%{version}/hypothesis-python -p1

%build
%py2_build
%py3_build
PYTHONPATH=src READTHEDOCS=True sphinx-build -b man docs docs/_build/man

%install
%py2_install
%py3_install
%{__install} -Dpm0644 -t %{buildroot}%{_mandir}/man1 docs/_build/man/hypothesis.1

%files help
%{_mandir}/man1/hypothesis.1*
%doc README.rst

%files -n python2-hypothesis
%doc ../LICENSE.txt
%{python2_sitelib}/hypothesis-*.egg-info/
%{python2_sitelib}/hypothesis/

%files -n python3-hypothesis
%doc ../LICENSE.txt
%{python3_sitelib}/hypothesis-*.egg-info
%{python3_sitelib}/hypothesis/

%changelog
* Thu Nov 28 2019 likexin<likexin4@huawei.com> - 3.66.11-2
- Package init
