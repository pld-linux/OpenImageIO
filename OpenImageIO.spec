# TODO:
# - Field3D (in progress)
# and if possible:
# - system libcineon in cineon plugin
# - system libsquish in dds plugin
# - system libdpx in dpx plugin
# - system ptex library in ptex plugin
#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
%bcond_without	tbb		# Threading Building Blocks
#
Summary:	Library for reading and writing images
Summary(pl.UTF-8):	Biblioteka do odczytu i zapisu obrazów
Name:		OpenImageIO
Version:	0.10.3
Release:	1
License:	BSD
Group:		Libraries
Source0:	https://github.com/OpenImageIO/oiio/tarball/Release-%{version}#/%{name}-%{version}.tar.gz
# Source0-md5:	20c0867864ee6b1cfccc45a0460c12bc
Patch0:		%{name}-soname.patch
Patch1:		%{name}-python.patch
URL:		https://sites.google.com/site/openimageio/home
BuildRequires:	OpenEXR-devel >= 1.6.1
BuildRequires:	OpenGL-devel
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtOpenGL-devel
# filesystem, regex, system, thread
BuildRequires:	boost-devel >= 1.35
BuildRequires:	boost-python-devel >= 1.35
BuildRequires:	cmake >= 2.6
BuildRequires:	glew-devel >= 1.5.1
# for FIELD3D (Field3D/Field.h, -lField3D)
#BuildRequires:	hdf5-devel
BuildRequires:	ilmbase-devel >= 1.0.1
BuildRequires:	jasper-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	python-devel >= 1:2.6
%{?with_tbb:BuildRequires:	tbb-devel}
BuildRequires:	zlib-devel
Requires:	ilmbase >= 1.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenImageIO is a library for reading and writing images, and a bunch
of related classes, utilities, and applications. It has extremely
simple but powerful ImageInput and ImageOutput APIs for reading and
writing 2D images that is format agnostic; specific formats are
implemented by DLL/DSO plugins.

Currently there are format plugins for: TIFF, JPEG/JFIF, OpenEXR, PNG,
HDR/RGBE, Targa, JPEG-2000, DPX, Cineon, FITS, BMP, ICO, RMan Zfile,
Softimage PIC, DDS, SGI, PNM/PPM/PGM/PBM, Field3d, WebP.

%description -l pl.UTF-8
OpenImageIO to biblioteka do odczytu i zapisu obrazów oraz wiele
powiązanych klas, narzędzi i aplikacji. Ma bardzo proste, ale mające
wiele możliwości API ImageInput i ImageOutput służące do odczytu i
zapisu obrazów 2D, które jest niezależne od formatu; konkretne formaty
są implementowane przez wtyczki DLL/DSO.

Obecnie istnieją wtyczki obsługujące formaty: TIFF, JPEG/JFIF,
OpenEXR, PNG, HDR/RGBE, Targa, JPEG-2000, DPX, Cineon, FITS, BMP, ICO,
RMan Zfile, Softimage PIC, DDS, SGI, PNM/PPM/PGM/PBM, Field3d, WebP.

%package devel
Summary:	Header files for OpenImageIO library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki OpenImageIO
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for OpenImageIO library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki OpenImageIO.

%package plugin-ico
Summary:	ICO plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka ICO dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-ico
OpenImageIO plugin to read and write ICO files.

%description plugin-ico -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca i zapisująca pliki ICO.

%package plugin-jpeg
Summary:	JPEG plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka JPEG dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-jpeg
OpenImageIO plugin to read and write JPEG files (with TIFF/EXIF
information).

%description plugin-jpeg -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca i zapisująca pliki JPEG
(wraz z informacjami TIFF/EXIF).

%package plugin-jpeg2000
Summary:	JPEG2000 plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka JPEG2000 dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-jpeg2000
OpenImageIO plugin to read and write JPEG2000 files.

%description plugin-jpeg2000 -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca i zapisująca pliki JPEG2000.

%package plugin-openexr
Summary:	OpenEXR plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka OpenEXR dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenEXR >= 1.6.1

%description plugin-openexr
OpenImageIO plugin to read and write OpenEXR files.

%description plugin-openexr -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca i zapisująca pliki OpenEXR.

%package plugin-png
Summary:	PNG plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka PNG dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-png
OpenImageIO plugin to read and write PNG files.

%description plugin-png -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca i zapisująca pliki PNG.

%package plugin-tiff
Summary:	TIFF plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka TIFF dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-tiff
OpenImageIO plugin to read and write TIFF files.

%description plugin-tiff -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca i zapisująca pliki TIFF.

%package apidocs
Summary:	Programmer documentation for OpenImageIO library
Summary(pl.UTF-8):	Dokumentacja programisty do biblioteki OpenImageIO
Group:		Documentation

%description apidocs
Programmer documentation for OpenImageIO library.

%description apidocs -l pl.UTF-8
Dokumentacja programisty do biblioteki OpenImageIO.

%package iv
Summary:	Qt/OpenImageIO-based Image Viewer
Summary(pl.UTF-8):	Przeglądarka obrazków (IV) oparta o Qt i OpenImageIO
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Requires:	glew >= 1.5.1

%description iv
IV is an image viewer based on ImageIO plugins; therefore it can read
images of any format for which an appropriate plugin may be found.

%description iv -l pl.UTF-8
IV to przeglądarka obrazków oparta na wtyczkach ImageIO; dzięki temu
jest w stanie odczytać obrazy w dowolnym formacie, dla którego
istnieje właściwa wtyczka.

%package -n python-OpenImageIO
Summary:	Python binding for OpenImageIO library
Summary(pl.UTF-8):	Wiązanie Pythona do biblioteki OpenImageIO
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-OpenImageIO
Python binding for OpenImageIO library.

%description -n python-OpenImageIO -l pl.UTF-8
Wiązanie Pythona do biblioteki OpenImageIO.

%prep
%setup -q -n OpenImageIO-oiio-7d98ca6
%patch0 -p1
%patch1 -p1

%build
install -d build
cd build
%cmake ../src \
	-DEMBEDPLUGINS=OFF \
	-DLIBDIR=%{_libdir} \
	-DPYLIBDIR=%{py_sitedir} \
	-DPYTHON_VERSION=%{py_ver} \
	-DSOVERSION:STRING=0 \
	%{!?with_tbb:-DUSE_TBB=OFF} \
# FIELD3D ?

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# name clash with iv
mv -f $RPM_BUILD_ROOT%{_bindir}/{iv,oiiv}

%{__rm} $RPM_BUILD_ROOT%{_prefix}/{CHANGES,INSTALL,LICENSE}
%{__rm} $RPM_BUILD_ROOT%{_prefix}/doc/{CLA-*,openimageio.pdf}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS LICENSE README
%attr(755,root,root) %{_bindir}/iconvert
%attr(755,root,root) %{_bindir}/idiff
%attr(755,root,root) %{_bindir}/igrep
%attr(755,root,root) %{_bindir}/iinfo
%attr(755,root,root) %{_bindir}/iprocess
%attr(755,root,root) %{_bindir}/maketx
%attr(755,root,root) %{_libdir}/libOpenImageIO.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libOpenImageIO.so.0
%attr(755,root,root) %{_libdir}/bmp.imageio.so
%attr(755,root,root) %{_libdir}/dds.imageio.so
%attr(755,root,root) %{_libdir}/dpx.imageio.so
%attr(755,root,root) %{_libdir}/fits.imageio.so
%attr(755,root,root) %{_libdir}/hdr.imageio.so
%attr(755,root,root) %{_libdir}/pnm.imageio.so
%attr(755,root,root) %{_libdir}/ptex.imageio.so
%attr(755,root,root) %{_libdir}/sgi.imageio.so
%attr(755,root,root) %{_libdir}/socket.imageio.so
%attr(755,root,root) %{_libdir}/softimage.imageio.so
%attr(755,root,root) %{_libdir}/targa.imageio.so
%attr(755,root,root) %{_libdir}/zfile.imageio.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libOpenImageIO.so
%{_includedir}/OpenImageIO

%files plugin-ico
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ico.imageio.so

%files plugin-jpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/jpeg.imageio.so

%files plugin-jpeg2000
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/jpeg2000.imageio.so

%files plugin-openexr
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openexr.imageio.so

%files plugin-png
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/png.imageio.so

%files plugin-tiff
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/tiff.imageio.so

%files apidocs
%defattr(644,root,root,755)
%doc src/doc/openimageio.pdf

%files iv
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oiiv

%files -n python-OpenImageIO
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/OpenImageIO.so
