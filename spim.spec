# $Revision: 1.2 $
Summary:	MIPS simulator
Summary(pl):	symulator MIPS'a
Name:		spim
Version:	6.3
Release:	0
License:	own, incopatibile with GNU
Group:		Applications/Emulators
Group(pl):	Aplikacje/Emulatory
Source0:	spim.tar.gz
Patch0:		spim-dirs.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
MIPS emulator

%description -l pl
Emulator MIPS'a

%package -n xspim
Summary:	X interface to spim
Group:		Applications/Emulators
Group(pl):	Aplikacje/Emulator
Requires:	spim = %{version}

%description -n xspim
xspim

%description -n xspim -l pl
xspim

%prep
%setup -q
%patch0 -p0

%build
./Configure 
xmkmf
%{__make}
%{__make} xspim


%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT%{_datadir}/spim

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Documentation/*.ps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Documentation/*gz
%attr(755,root,root) %{_bindir}/spim
%{_datadir}/spim/trap.handler


%files -n xspim
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xspim
