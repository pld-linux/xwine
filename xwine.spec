Summary:	Graphical User Interface for the wine emulator
Summary(pl):	Graficzny interfejs u¿ytkownika do emulatora wine
Name:		xwine
Version:	1.0
Release:	0.1
License:	GPL
Group:		Applications/Emulators
Source0:	http://darken33.free.fr/download/projets/xwine/%{name}-%{version}.tar.gz
# Source0-md5:	99c98ce8a0e91f4d3d39fbbfc4c08c41
URL:		http://darken33.free.fr/
BuildRequires:	gnome-libs-devel
Requires:	wine
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XWine is a graphical user interface for the wine emulator. You can
configure and run MS Windows applications (Windows 3.x or Win32).

XWine's functions:
- Wine's configuration
- configuration and management of MS Windows applications.

%description -l pl
XWine to graficzny interfejs u¿ytkownika do emulatora wine. Pozwala
konfigurowaæ i uruchamiaæ aplikacje MS Windows (Windows 3.x i Win32).

Funkcje XWine:
- konfiguracja Wine
- konfiguracja i zarz±dzanie aplikacjami MS Windows (3.x i Win32).

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xwine
%{_pixmapsdir}/xwine
%{_docdir}/xwine
