# $Revision: 1.1 $
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
mkdir -p $RPM_BUILD_ROOT/usr/share/spim
%{__make} DESTDIR=$RPM_BUILD_ROOT install
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}
install Documentation/*.ps $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/spim
/usr/share/spim/trap.handler
%doc %{_docdir}/%{name}/*

%files -n xspim
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xspim
