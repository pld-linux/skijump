Summary:	Ski jumping simulation game
Summary(pl):	Symulacja skoków narciarskich
Name:		skijump
Version:	0.2.0
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	75ef3713f004567ff3511784b89a0a87
Source1:	%{name}.desktop
Patch0:		%{name}-gcc34.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-dirs.patch
Patch3:		%{name}-ac.patch
URL:		http://www.skijump.org/
BuildRequires:	allegro-devel >= 4.1.10
Buildrequires:	autoconf
Buildrequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ski jumping simulation game.

%description -l pl
Symulacja skoków narciarskich.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/Makefile.in

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FILES README
%attr(2755,root,games) %{_bindir}/*
%{_datadir}/%{name}
%attr(775,root,games) %dir %{_localstatedir}/games/%{name}
%attr(775,root,games) %dir %{_localstatedir}/games/%{name}/replays
%attr(664,root,games) %config(noreplace) %{_localstatedir}/games/%{name}/competitors.txt
%attr(664,root,games) %config %{_localstatedir}/games/%{name}/cameras.txt
%attr(664,root,games) %config %{_localstatedir}/games/%{name}/hill*.txt
%attr(664,root,games) %{_localstatedir}/games/%{name}/replays/*
%{_desktopdir}/*.desktop
