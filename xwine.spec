Summary:	Graphical User Interface for the wine emulator
Summary(pl):	Graficzny interfejs u¿ytkownika do emulatora wine
Name:		xwine
Version:	1.0
Release:	2
License:	GPL
Group:		Applications/Emulators
Source0:	http://darken33.free.fr/download/projets/xwine/%{name}-%{version}.tar.gz
# Source0-md5:	99c98ce8a0e91f4d3d39fbbfc4c08c41
URL:		http://darken33.free.fr/
BuildRequires:	gnome-libs-devel
BuildRequires:	libxml2-devel
Requires:	wine
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xwine is a graphical user interface for the wine emulator. You can
configure and run MS Windows applications (Windows 3.x or Win32).

xwine's functions:
- Wine's configuration
- configuration and management of MS Windows applications.

%description -l pl
xwine to graficzny interfejs u¿ytkownika do emulatora wine. Pozwala
konfigurowaæ i uruchamiaæ aplikacje MS Windows (Windows 3.x i Win32).

Funkcje xwine:
- konfiguracja Wine
- konfiguracja i zarz±dzanie aplikacjami MS Windows (3.x i Win32).

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}/%{name} \
	$RPM_BUILD_ROOT%{_pixmapsdir}/%{name} \
	$RPM_BUILD_ROOT{/etc/%{name},/etc/%{name}/apps} \
	$RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/lang
cp -af pixmaps/* $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}
cp -a menu/* $RPM_BUILD_ROOT%{_desktopdir}/%{name}
cp -a src/xwine $RPM_BUILD_ROOT%{_bindir}
cp -a src/lang/* $RPM_BUILD_ROOT%{_datadir}/%{name}/lang

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %dir /etc/%{name}
%attr(755,root,root) %dir /etc/%{name}/apps
%{_pixmapsdir}/%{name}
%{_desktopdir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/lang
%lang(en) %{_datadir}/%{name}/lang/lang.en.xml
%lang(fr) %{_datadir}/%{name}/lang/lang.fr.xml

%doc doc/*
