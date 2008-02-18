Summary:	evilwm - a minimalist window manager
Summary(pl.UTF-8):	evilwm - minimalistyczny window manager
Name:		evilwm
Version:	0.99.17
Release:	1
License:	GPL-like
Group:		X11/Window Managers
Source0:	http://dl.sourceforge.net/evilwm/%{name}_%{version}.orig.tar.gz
# Source0-md5:	2d9ae76a172240a1ba7e359d9aae41aa
Source1:	%{name}-xsession.desktop
Patch0:		%{name}-fixed.patch
URL:		http://evilwm.sourceforge.net/
BuildRequires:	xorg-lib-libXext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A minimalist window manager for the X Window System.
'Minimalist' here doesn't mean it's too bare to be usable - it just
means it omits a lot of the stuff that make other window managers
unusable.

Features:

 * No window decorations apart from a simple 1 pixel border
 * No icons
 * Good keyboard control, including repositioning and maximise toggles
 * Solid window drags (compile time option - may be slow on old
   machines)
 * Virtual desktops (compile time option)
 * Small binary size (even with everything turned on)

%description -l pl.UTF-8
Minimalistyczny zarządca okien dla X Window System.
'Minimalistyczny' nie znaczy, że jest zbyt prymitywny, by być
użytecznym - znaczy, iż po prostu pomija wiele rzeczy, które czynią
innych zarządców okien nieużytecznymi.

Jego cechy to:

 * Brak dekoracji okien poza prostą ramką o szerokości 1 piksela
 * Brak ikon
 * Dobra kontrola z klawiatury, włączając przemieszczanie i
   przełączanie maksymalizacji
 * Wirtualne desktopy (opcja kompilacji)
 * Mały rozmiar binarki (nawet z wszystkim włączonym)

%prep
%setup -q -n %{name}-%{version}.orig
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS='$(INCLUDES) $(DEFINES) %{rpmcflags} -Wall'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/xsessions,%{_mandir}/man1}

install evilwm $RPM_BUILD_ROOT%{_bindir}
install evilwm.1 $RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README* TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xsessions/%{name}.desktop
%{_mandir}/man1/*
