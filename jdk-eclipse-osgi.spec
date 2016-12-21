Name     : jdk-eclipse-osgi
Version  : 3.7.1
Release  : 1
URL      : http://repo.maven.apache.org/maven2/org/eclipse/osgi/org.eclipse.osgi/3.7.1/org.eclipse.osgi-3.7.1.jar
Source0  : http://repo.maven.apache.org/maven2/org/eclipse/osgi/org.eclipse.osgi/3.7.1/org.eclipse.osgi-3.7.1.jar
Source1  : http://repo.maven.apache.org/maven2/org/eclipse/osgi/org.eclipse.osgi/3.7.1/org.eclipse.osgi-3.7.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : EPL-1.0
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/eclipse-osgi.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/eclipse-osgi.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/eclipse-osgi.xml \
%{buildroot}/usr/share/maven-poms/eclipse-osgi.pom \
%{buildroot}/usr/share/java/eclipse-osgi.jar \

%files
%defattr(-,root,root,-)
/usr/share/java/eclipse-osgi.jar
/usr/share/maven-metadata/eclipse-osgi.xml
/usr/share/maven-poms/eclipse-osgi.pom
