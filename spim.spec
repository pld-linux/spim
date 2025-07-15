Summary:	MIPS simulator
Summary(pl.UTF-8):	symulator MIPS-a
Name:		spim
Version:	7.3
Release:	0.1
License:	own, incompatibile with GPL
Group:		Applications/Emulators
Source0:	http://www.cs.wisc.edu/~larus/SPIM/%{name}.tar.gz
# Source0-md5:	52002170982d157fd89d445b481bd223
Patch0:		%{name}-dirs.patch
URL:		http://www.cs.wisc.edu/~larus/spim.html
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	xorg-cf-files
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-util-imake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SPIM S20 is a software simulator that runs assembly language programs
for the MIPS R2000/R3000 RISC computers. SPIM can read and immediately
run files containing assembly language statements. SPIM is a
self-contained system for running these programs and contains a
debugger and interface to the operating system.

%description -l pl.UTF-8
Asembler i emulator MIPS-a (R2000/R3000) pozwalający pisanie i
uruchamianie programów napisanych w asemblerze MIPS-a na dowolnej
maszynie.

%package -n xspim
Summary:	X interface to spim
Summary(pl.UTF-8):	Interfejs X do SPIM-a
Group:		Applications/Emulators
Requires:	%{name} = %{version}-%{release}

%description -n xspim
X interface to SPIM - MIPS emulator

%description -n xspim -l pl.UTF-8
Nakładka na SPIM dająca interfejs X.

%prep
%setup -q
%patch -P0 -p1
ln -sf ../spim/configuration xspim/configuration

%build
cat << EOF > spim/configuration
%ifarch %{ix86} %{x8664}
-DLITTLEENDIAN
%else
-DBIGENDIAN
%endif
-DUSE_TERMIOS
EOF

%{__make} -C spim spim \
	CC="%{__cc} %{rpmcflags} -lm" \
	LDFLAGS="%{rpmldflags} -lm"

cd xspim
xmkmf
%{__make} -j1 xspim	\

	CC="%{__cc}" \
	LD="%{__cc} -nostdlib" \
	CCOPTIONS="%{rpmcflags}" \
	EXTRA_LDOPTIONS="%{rpmldflags}"
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/spim,%{_bindir},%{_mandir}/man1}

install spim/spim $RPM_BUILD_ROOT%{_bindir}
install xspim/xspim $RPM_BUILD_ROOT%{_bindir}
install Documentation/spim.man $RPM_BUILD_ROOT%{_mandir}/man1/spim.1
install Documentation/xspim.man $RPM_BUILD_ROOT%{_mandir}/man1/xspim.1
install CPU/exceptions.s $RPM_BUILD_ROOT%{_datadir}/spim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README VERSION Documentation/SPIM.html
%attr(755,root,root) %{_bindir}/spim
%{_datadir}/spim
%{_mandir}/man1/spim.1*

%files -n xspim
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xspim
%{_mandir}/man1/xspim.1*
