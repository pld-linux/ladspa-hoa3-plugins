Summary:	HOA3 (third order ambisonics) LADSPA plugins
Summary(pl.UTF-8):	Wtyczki LADSPA HOA3 (dźwięku trójwymiarowego)
Name:		ladspa-hoa3-plugins
Version:	0.3.0
Release:	1
License:	GPL v3+
Group:		Applications/Sound
Source0:	http://kokkinizita.linuxaudio.org/linuxaudio/downloads/HOA3-plugins-%{version}.tar.bz2
# Source0-md5:	37a07a7bfbdbb3ac4845256af70cb74b
Patch0:		%{name}-make.patch
URL:		http://kokkinizita.linuxaudio.org/linuxaudio/ladspa/index.html
BuildRequires:	ladspa-devel
BuildRequires:	libstdc++-devel
Requires:	ladspa-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprovfiles	%{_libdir}/ladspa

%description
HOA3 (third order ambisonics) LADSPA plugins.

%description -l pl.UTF-8
Wtyczki LADSPA HOA3 (dźwięku trójwymiarowego).

%prep
%setup -q -n HOA3-plugins-%{version}
%patch0 -p1

%build
CPPFLAGS="%{rpmcppflags}" \
CXXFLAGS="%{rpmcxxflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} -C source \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ladspa

%{__make} -C source install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_libdir}/ladspa

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/ladspa/hoa3tools.so
