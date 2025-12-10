Name:		python-rust2rpm
Version:	26.1.1
Release:	1
Source0:	https://codeberg.org/rust2rpm/rust2rpm/archive/v%{version}.tar.gz
Patch0:		rust2rpm-25.0.3-openmandriva.patch
Patch1:		rust2rpm-25.0.3-openmandriva-notupstreamable.patch
Summary:	Tool for packaging rust libraries in rpm packages
URL:		https://codeberg.org/rust2rpm/rust2rpm
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildSystem:	python
BuildArch:	noarch

%description
A tool for automatically generating RPM spec files for Rust crates

%files
%{_bindir}/rust2rpm
%{py_sitedir}/rust2rpm
%{py_sitedir}/rust2rpm-*.*-info
