Name:		python-rust2rpm
Version:	25.0.3
Release:	1
Source0:	https://pagure.io/fedora-rust/rust2rpm/archive/v%{version}/rust2rpm-v%{version}.tar.gz
Patch0:		rust2rpm-25.0.3-openmandriva.patch
Patch1:		rust2rpm-25.0.3-openmandriva-notupstreamable.patch
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
