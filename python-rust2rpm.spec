Name:		python-rust2rpm
Version:	24.3.1
Release:	1
Source0:	https://pagure.io/fedora-rust/rust2rpm/archive/v%{version}/rust2rpm-v%{version}.tar.gz
Summary:	Tool for packaging rust libraries in rpm packages
URL:		https://pypi.org/project/rust2rpm/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
A tool for automatically generating RPM spec files for Rust crates

%prep
%autosetup -p1 -n rust2rpm-v%{version}

%build
%py_build

%install
%py_install

%files
%{_bindir}/rust2rpm
%{py_sitedir}/rust2rpm
%{py_sitedir}/rust2rpm-*.*-info
