#a $Revision: 1.20 $, $Date: 2005-03-13 18:36:18 $
Summary:	MIPS simulator
Summary(pl):	symulator MIPS-a
Name:		spim
Version:	7.1
Release:	0
License:	own, incompatibile with GPL
Group:		Applications/Emulators
Source0:	http://www.cs.wisc.edu/~larus/SPIM/%{name}.tar.gz
# Source0-md5:	24546da54bca92d96bf2ea284e81d6eb
Patch0:		%{name}-dirs.patch
URL:		http://www.cs.wisc.edu/~larus/spim.html
BuildRequires:	glibc-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SPIM S20 is a software simulator that runs assembly language programs
for the MIPS R2000/R3000 RISC computers. SPIM can read and immediately
run files containing assembly language statements. SPIM is a
self-contained system for running these programs and contains a
debugger and interface to the operating system.

%description -l pl
Asembler i emulator MIPS-a (R2000/R3000) pozwalaj±cy pisanie i
uruchamianie programów napisanych w asemblerze MIPS-a na dowolnej
maszynie.

%package -n xspim
Summary:	X interface to spim
Summary(pl):	Interfejs X do SPIM-a
Group:		Applications/Emulators
Requires:	spim = %{version}

%description -n xspim
X interface to SPIM -- MIPS emulator

%description -n xspim -l pl
Nak³adka na SPIM daj±ca interfejs X.

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
install -d $RPM_BUILD_ROOT%{_datadir}/spim

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README Documentation/*.ps
%attr(755,root,root) %{_bindir}/spim
%dir %{_datadir}/spim
%{_datadir}/spim/exceptions.s

%files -n xspim
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xspim
