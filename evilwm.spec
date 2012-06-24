Summary:	evilwm - a minimalist window manager
Summary(pl):	evilwm - minimalistyczny window manager
Name:		evilwm
Version:	0.99.17
Release:	0.1
License:	GPL-like
Group:		X11/Window Managers
Source0:	http://dl.sourceforge.net/evilwm/%{name}_%{version}.orig.tar.gz
# Source0-md5:	2d9ae76a172240a1ba7e359d9aae41aa
Source1:	%{name}-xsession.desktop
URL:		http://evilwm.sourceforge.net/
BuildRequires:	XFree86-devel
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

%description -l pl
Minimalistyczny zarz�dca okien dla X Window System.
'Minimalistyczny' nie znaczy, �e jest zbyt prymitywny, by by�
u�ytecznym - znaczy, i� po prostu pomija wiele rzeczy, kt�re czyni�
innych zarz�dc�w okien nieu�ytecznymi.

Jego cechy to:

 * Brak dekoracji okien poza prost� ramk� o szeroko�ci 1 piksela
 * Brak ikon
 * Dobra kontrola z klawiatury, w��czaj�c przemieszczanie i
   prze��czanie maksymalizacji
 * Wirtualne desktopy (opcja kompilacji)
 * Ma�y rozmiar binarki (nawet z wszystkim w��czonym)

%prep
%setup -q -n %{name}-%{version}.orig

%build
%{__make} allinone \
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
