%define major 5
%define libname %mklibname otr %{major}
%define devname %mklibname -d otr

Summary:	Off-The-Record Messaging library and toolkit
Name:		libotr
Version:	4.0.0
Release:	9
License:	GPLv2+
Group:		Networking/Instant messaging
Url:		http://www.cypherpunks.ca/otr/
Source0:	http://www.cypherpunks.ca/otr/%{name}-%{version}.tar.gz
Source1:	http://www.cypherpunks.ca/otr/%{name}-%{version}.tar.gz.asc
BuildRequires:	pkgconfig(libgcrypt)

%description
%{name} is a library and toolkit which implements Off-the-Record (OTR)
Messaging.

OTR allows you to have private conversations over IM by providing:
 - Encryption
   - No one else can read your instant messages.
 - Authentication
   - You are assured the correspondent is who you think it is.
 - Deniability
   - The messages you send do _not_ have digital signatures that are
     checkable by a third party.  Anyone can forge messages after a
     conversation to make them look like they came from you.  However,
     _during_ a conversation, your correspondent is assured the messages
     he sees are authentic and unmodified.
 - Perfect forward secrecy
   - If you lose control of your private keys, no previous conversation
     is compromised.

#----------------------------------------------------------------------------

%package	-n %{libname}
Summary:	Off-The-Record Messaging library and toolkit
Group:		System/Libraries
License:	LGPLv2.1+

%description	-n %{libname}
%{name} is a library and toolkit which implements Off-the-Record (OTR)
Messaging.

OTR allows you to have private conversations over IM by providing:
 - Encryption
   - No one else can read your instant messages.
 - Authentication
   - You are assured the correspondent is who you think it is.
 - Deniability
   - The messages you send do _not_ have digital signatures that are
     checkable by a third party.  Anyone can forge messages after a
     conversation to make them look like they came from you.  However,
     _during_ a conversation, your correspondent is assured the messages
     he sees are authentic and unmodified.
 - Perfect forward secrecy
   - If you lose control of your private keys, no previous conversation
     is compromised.

%files -n %{libname}
%doc AUTHORS COPYING.LIB
%{_libdir}/libotr.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development related files of %{name}
Group:		Development/C
License:	LGPLv2.1+
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
%{name} is a library and toolkit which implements Off-the-Record (OTR)
Messaging. This package contains development related files of %{name}.

%files -n %{devname}
%doc ChangeLog NEWS README
%{_datadir}/aclocal/*.m4
%{_includedir}/*
%{_libdir}/libotr.so
%{_libdir}/pkgconfig/*.pc

#----------------------------------------------------------------------------

%package	utils
Summary:	Helper utilities of %{name}
Group:		Networking/Instant messaging
License:	GPLv2+
Requires:	%{libname} = %{EVRD}

%description	utils
%{name} is a library and toolkit which implements Off-the-Record (OTR)
Messaging. This package contains various helper utilities from %{name}.

%files utils
%doc AUTHORS
%{_bindir}/*
%{_mandir}/man?/*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x \
	--with-pic \
	--disable-static

%make

%install
%makeinstall_std

