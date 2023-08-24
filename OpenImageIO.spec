# TODO:
# - Nuke >= 7.0?  https://www.foundry.com/products/nuke/ (proprietary)
# - R3DSDK? https://www.red.com/downloads/r3d-sdk (proprietary)
# - package fonts?
# /usr/share/fonts/OpenImageIO/DroidSans-Bold.ttf
# /usr/share/fonts/OpenImageIO/DroidSans.ttf
# /usr/share/fonts/OpenImageIO/DroidSansMono.ttf
# /usr/share/fonts/OpenImageIO/DroidSerif-Bold.ttf
# /usr/share/fonts/OpenImageIO/DroidSerif-BoldItalic.ttf
# /usr/share/fonts/OpenImageIO/DroidSerif-Italic.ttf
# /usr/share/fonts/OpenImageIO/DroidSerif.ttf
#
# to bootstrap: build OpenColorIO --without oiio, build OpenImageIO, rebuild OpenColorIO
#
# Conditional build:
%bcond_without	ocio		# OpenColorIO support in library
%bcond_without	opencv		# OpenCV support in library
%bcond_without	openvdb		# OpenVDB plugin
%bcond_with	qt6		# Qt6 instead of Qt5
%bcond_without	tbb		# Threading Building Blocks
#
%ifarch i386 i486
# https://github.com/OpenImageIO/oiio/issues/583
%undefine	with_tbb
%endif
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ia64 ppc ppc64
%undefine	with_tbb
%endif
%if %{without tbb}
%undefine	with_openvdb
%endif
#
Summary:	Library for reading and writing images
Summary(pl.UTF-8):	Biblioteka do odczytu i zapisu obrazów
Name:		OpenImageIO
Version:	2.4.14.0
Release:	1
License:	Apache v2.0
Group:		Libraries
#Source0Download: https://github.com/OpenImageIO/oiio/releases
Source0:	https://github.com/OpenImageIO/oiio/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	cc0e320302622783dfe16ac6ae1946b3
Patch2:		%{name}-system-libcineon.patch
Patch3:		no-clang-format.patch
URL:		https://github.com/OpenImageIO/oiio
BuildRequires:	Imath-devel >= 3.0.0
%{?with_ocio:BuildRequires:	OpenColorIO-devel}
BuildRequires:	OpenEXR-devel >= 3.0.0
BuildRequires:	OpenGL-devel
%if %{with qt6}
BuildRequires:	Qt6Core-devel >= 6
BuildRequires:	Qt6Gui-devel >= 6
BuildRequires:	Qt6OpenGLWidgets-devel >= 6
BuildRequires:	Qt6Widgets-devel >= 6
%else
BuildRequires:	Qt5Core-devel >= 5.6
BuildRequires:	Qt5Gui-devel >= 5.6
BuildRequires:	Qt5OpenGL-devel >= 5.6
BuildRequires:	Qt5Widgets-devel >= 5.6
%endif
# filesystem, regex, system, thread
BuildRequires:	boost-devel >= 1.66
BuildRequires:	boost-python3-devel >= 1.66
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 3.12
BuildRequires:	dcmtk-devel >= 3.6.1
BuildRequires:	ffmpeg-devel >= 3.0
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	giflib-devel >= 5.0
BuildRequires:	glew-devel >= 1.5.1
BuildRequires:	hdf5-devel
BuildRequires:	jasper-devel
BuildRequires:	libcineon-devel
BuildRequires:	libfmt-devel >= 9.0
BuildRequires:	libheif-devel >= 1.7
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libraw-devel >= 0.18
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtiff-devel >= 4.0
BuildRequires:	libwebp-devel
%{?with_opencv:BuildRequires:	opencv-devel >= 3.0}
BuildRequires:	openjpeg2-devel >= 2.4
%{?with_openvdb:BuildRequires:	openvdb-devel >= 5.0}
BuildRequires:	ptex-devel >= 2.1
BuildRequires:	pugixml-devel >= 1.8
BuildRequires:	python3-devel >= 1:2.7
BuildRequires:	python3-pybind11 >= 2.2.0
BuildRequires:	robin-map-devel >= 0.6.2
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	squish-devel >= 1.10
%{?with_tbb:BuildRequires:	tbb-devel >= 2018}
BuildRequires:	txt2man
BuildRequires:	zlib-devel
Requires:	OpenEXR >= 3.0.0
Obsoletes:	OpenImageIO-plugin-field3d < 2.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenImageIO is a library for reading and writing images, and a bunch
of related classes, utilities, and applications. It has extremely
simple but powerful ImageInput and ImageOutput APIs for reading and
writing 2D images that is format agnostic; specific formats are
implemented by DLL/DSO plugins.

Currently there are format plugins for: TIFF, JPEG/JFIF, OpenEXR, PNG,
HDR/RGBE, Targa, JPEG-2000, DPX, Cineon, FITS, BMP, ICO, RMan Zfile,
Softimage PIC, DDS, SGI, PNM/PPM/PGM/PBM, OpenVDB, WebP.

%description -l pl.UTF-8
OpenImageIO to biblioteka do odczytu i zapisu obrazów oraz wiele
powiązanych klas, narzędzi i aplikacji. Ma bardzo proste, ale mające
wiele możliwości API ImageInput i ImageOutput służące do odczytu i
zapisu obrazów 2D, które jest niezależne od formatu; konkretne formaty
są implementowane przez wtyczki DLL/DSO.

Obecnie istnieją wtyczki obsługujące formaty: TIFF, JPEG/JFIF,
OpenEXR, PNG, HDR/RGBE, Targa, JPEG-2000, DPX, Cineon, FITS, BMP, ICO,
RMan Zfile, Softimage PIC, DDS, SGI, PNM/PPM/PGM/PBM, OpenVDB, WebP.

%package devel
Summary:	Header files for OpenImageIO library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki OpenImageIO
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libfmt-devel >= 9.0
Requires:	libstdc++-devel >= 6:4.7

%description devel
Header files for OpenImageIO library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki OpenImageIO.

%package plugin-cineon
Summary:	Cineon plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka Cineon dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-cineon
OpenImageIO plugin to read Cineon files.

%description plugin-cineon -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca pliki Cineon.

%package plugin-dicom
Summary:	DICOM plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka DICOM dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dcmtk >= 3.6.1
Requires:	squish >= 1.10

%description plugin-dicom
OpenImageIO plugin to read DICOM files.

%description plugin-dicom -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca pliki DICOM.

%package plugin-dds
Summary:	DDS plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka DDS dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	squish >= 1.10

%description plugin-dds
OpenImageIO plugin to read DDS files.

%description plugin-dds -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca pliki DDS.

%package plugin-dpx
Summary:	DPX plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka DPX dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-dpx
OpenImageIO plugin to read and write DPX files.

%description plugin-dpx -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca i zapisująca pliki DPX.

%package plugin-ffmpeg
Summary:	FFmpeg plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka FFmpeg dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ffmpeg-libs >= 3.0

%description plugin-ffmpeg
OpenImageIO plugin to read FFmpeg files.

%description plugin-ffmpeg -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca pliki FFmpeg.

%package plugin-gif
Summary:	Gif plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka Gif dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	giflib >= 5.0

%description plugin-gif
OpenImageIO plugin to read GIF files.

%description plugin-gif -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca pliki GIF.

%package plugin-heif
Summary:	HEIF plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka HEIF dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libheif >= 1.7

%description plugin-heif
OpenImageIO plugin to read HEIF files.

%description plugin-heif -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca pliki HEIF.

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
Wtyczka biblioteki OpenImageIO czytająca i zapisująca pliki JPEG (wraz
z informacjami TIFF/EXIF).

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
Requires:	OpenEXR >= 2.0

%description plugin-openexr
OpenImageIO plugin to read and write OpenEXR files.

%description plugin-openexr -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca i zapisująca pliki OpenEXR.

%package plugin-openvdb
Summary:	OpenVDB plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka OpenVDB dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	openvdb >= 5.0

%description plugin-openvdb
OpenImageIO plugin to read OpenVDB files.

%description plugin-openvdb -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca pliki OpenVDB.

%package plugin-png
Summary:	PNG plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka PNG dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-png
OpenImageIO plugin to read and write PNG files.

%description plugin-png -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca i zapisująca pliki PNG.

%package plugin-psd
Summary:	PSD plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka PSD dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-psd
OpenImageIO plugin to read and write PSD files.

%description plugin-psd -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca i zapisująca pliki PSD.

%package plugin-ptex
Summary:	Ptex plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka Ptex dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ptex >= 2

%description plugin-ptex
OpenImageIO plugin to read Ptex files.

%description plugin-ptex -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca pliki Ptex.

%package plugin-raw
Summary:	RAW plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka RAW dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libraw >= 0.18

%description plugin-raw
OpenImageIO plugin to readTRAW files.

%description plugin-raw -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca pliki RAW.

%package plugin-webp
Summary:	WebP plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka WebP dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-webp
OpenImageIO plugin to read and write WebP files.

%description plugin-webp -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca i zapisująca pliki WebP.

%package plugin-tiff
Summary:	TIFF plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka TIFF dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libtiff >= 4.0

%description plugin-tiff
OpenImageIO plugin to read and write TIFF files.

%description plugin-tiff -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca i zapisująca pliki TIFF.

%package iv
Summary:	Qt/OpenImageIO-based Image Viewer
Summary(pl.UTF-8):	Przeglądarka obrazków (IV) oparta o Qt i OpenImageIO
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core >= 5.6
Requires:	Qt5Gui >= 5.6
Requires:	Qt5OpenGL >= 5.6
Requires:	Qt5Widgets >= 5.6
Requires:	glew >= 1.5.1

%description iv
IV is an image viewer based on ImageIO plugins; therefore it can read
images of any format for which an appropriate plugin may be found.

%description iv -l pl.UTF-8
IV to przeglądarka obrazków oparta na wtyczkach ImageIO; dzięki temu
jest w stanie odczytać obrazy w dowolnym formacie, dla którego
istnieje właściwa wtyczka.

%package -n python3-OpenImageIO
Summary:	Python binding for OpenImageIO library
Summary(pl.UTF-8):	Wiązanie Pythona do biblioteki OpenImageIO
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python3-OpenImageIO
Python binding for OpenImageIO library.

%description -n python3-OpenImageIO -l pl.UTF-8
Wiązanie Pythona do biblioteki OpenImageIO.

%prep
%setup -q -n oiio-%{version}
%patch2 -p1
%patch3 -p1

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_MANDIR=%{_mandir}/man1 \
	-DEMBEDPLUGINS=OFF \
	-DINCLUDE_INSTALL_DIR=%{_includedir}/%{name} \
	-DINTERNALIZE_FMT=OFF \
	-DLIB_INSTALL_DIR:PATH=%{_libdir} \
	-DBUILD_TESTING=OFF \
%ifarch i386 i486
	-DNOTHREADS=1 \
%endif
	-DPYTHON_VERSION=%{py3_ver} \
	-DUSE_EXTERNAL_PUGIXML=ON \
	-DSTOP_ON_WARNING=OFF \
	%{!?with_ocio:-DUSE_OCIO=OFF} \
	%{!?with_opencv:-DUSE_OPENCV=OFF} \
	%{!?with_qt6:-DUSE_QT6=OFF} \
	%{!?with_tbb:-DUSE_TBB=OFF}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# name clash with iv
%{__mv} $RPM_BUILD_ROOT%{_bindir}/{iv,oiiv}
%{__mv} $RPM_BUILD_ROOT%{_mandir}/man1/{iv,oiiv}.1

# installed as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES.md CREDITS.md GOVERNANCE.md LICENSE-BSD.md README.md RELICENSING.md
%attr(755,root,root) %{_bindir}/iconvert
%attr(755,root,root) %{_bindir}/idiff
%attr(755,root,root) %{_bindir}/igrep
%attr(755,root,root) %{_bindir}/iinfo
%attr(755,root,root) %{_bindir}/maketx
%attr(755,root,root) %{_bindir}/oiiotool
%attr(755,root,root) %{_libdir}/libOpenImageIO.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libOpenImageIO.so.2.4
%attr(755,root,root) %{_libdir}/libOpenImageIO_Util.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libOpenImageIO_Util.so.2.4
%attr(755,root,root) %{_libdir}/bmp.imageio.so
%attr(755,root,root) %{_libdir}/fits.imageio.so
%attr(755,root,root) %{_libdir}/hdr.imageio.so
%attr(755,root,root) %{_libdir}/iff.imageio.so
%attr(755,root,root) %{_libdir}/pnm.imageio.so
%attr(755,root,root) %{_libdir}/rla.imageio.so
%attr(755,root,root) %{_libdir}/sgi.imageio.so
%attr(755,root,root) %{_libdir}/softimage.imageio.so
%attr(755,root,root) %{_libdir}/targa.imageio.so
%attr(755,root,root) %{_libdir}/zfile.imageio.so
%attr(755,root,root) %{_libdir}/null.imageio.so
%attr(755,root,root) %{_libdir}/term.imageio.so
%{_mandir}/man1/iconvert.1*
%{_mandir}/man1/idiff.1*
%{_mandir}/man1/igrep.1*
%{_mandir}/man1/iinfo.1*
%{_mandir}/man1/maketx.1*
%{_mandir}/man1/oiiotool.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libOpenImageIO.so
%attr(755,root,root) %{_libdir}/libOpenImageIO_Util.so
%{_includedir}/OpenImageIO
%{_pkgconfigdir}/OpenImageIO.pc
%{_libdir}/cmake/OpenImageIO

%files plugin-cineon
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/cineon.imageio.so

%files plugin-dicom
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/dicom.imageio.so

%files plugin-dds
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/dds.imageio.so

%files plugin-dpx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/dpx.imageio.so

%files plugin-ffmpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ffmpeg.imageio.so

%files plugin-gif
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gif.imageio.so

%files plugin-heif
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/heif.imageio.so

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

%if %{with openvdb}
%files plugin-openvdb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openvdb.imageio.so
%endif

%files plugin-png
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/png.imageio.so

%files plugin-psd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/psd.imageio.so

%files plugin-ptex
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ptex.imageio.so

%files plugin-raw
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/raw.imageio.so

%files plugin-tiff
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/tiff.imageio.so

%files plugin-webp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/webp.imageio.so

%files iv
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oiiv
%{_mandir}/man1/oiiv.1*

%files -n python3-OpenImageIO
%defattr(644,root,root,755)
%dir %{py3_sitedir}/OpenImageIO
%attr(755,root,root) %{py3_sitedir}/OpenImageIO/OpenImageIO*.so
%{py3_sitedir}/OpenImageIO/__init__.py
