%define		module	CDDB

Summary:	Module for accessing CDDB and FreeDB
Summary(pl):	Modu³ do ³±czenia z bazami CDDB i FreeDB
Name:		python-%{module}
Version:	1.4
Release:	3
License:	GPL
Group:		Development/Languages/Python
Source0:	http://cddb-py.sourceforge.net/%{module}-%{version}.tar.gz
# Source0-md5:	254698082bafe3030d07d88fb7e13fe2
URL:		http://cddb-py.sourceforge.net/
%pyrequires_eq	python-modules
BuildRequires:	python >= 1:2.3
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a set of three modules to access the CDDB and FreeDB online
databases of audio CD track titles and information. It includes a C
extension module to fetch track lengths under Linux, FreeBSD, OpenBSD,
Mac OS X, Solaris, and Win32, which is easily ported to other
operating systems.

%description -l pl
Jest to zestaw trzech modu³ów umo¿liwiaj±cych po³±czenie z bazami CDDB
i FreeDB w celu pobierania tytu³ów i informacji o ¶cie¿kach p³yt CD.
Pakiet zawiera te¿ modu³ w C do wyci±gania d³ugo¶ci ¶cie¿ek dzia³aj±cy
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

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%{py_sitedir}/*.py[co]
%attr(755,root,root) %{py_sitedir}/cdrom.so
%{_examplesdir}/%{name}-%{version}
