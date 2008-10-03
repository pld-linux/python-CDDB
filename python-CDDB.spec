%define		module	CDDB

Summary:	Module for accessing CDDB and FreeDB
Summary(pl.UTF-8):	Moduł dostępu do baz CDDB i FreeDB
Name:		python-%{module}
Version:	1.4
Release:	6
License:	GPL
Group:		Libraries/Python
Source0:	http://cddb-py.sourceforge.net/%{module}-%{version}.tar.gz
# Source0-md5:	254698082bafe3030d07d88fb7e13fe2
URL:		http://cddb-py.sourceforge.net/
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
%pyrequires_eq	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a set of three modules to access the CDDB and FreeDB online
databases of audio CD track titles and information. It includes a C
extension module to fetch track lengths under Linux, FreeBSD, OpenBSD,
Mac OS X, Solaris, and Win32, which is easily ported to other
operating systems.

%description -l pl.UTF-8
Jest to zestaw trzech modułów umożliwiających dostęp do baz CDDB i
FreeDB w celu pobierania tytułów i informacji o ścieżkach płyt CD.
Pakiet zawiera też moduł w C do wyciągania długości ścieżek, działający
pod Linuksem, FreeBSD, OpenBSD, MacOS X, Solarisem i Win32.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_examplesdir}/%{name}-%{version}}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

install cddb-info.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%{py_sitedir}/*.py[co]
%{py_sitedir}/CDDB-*.egg-info
%attr(755,root,root) %{py_sitedir}/cdrom.so
%{_examplesdir}/%{name}-%{version}
