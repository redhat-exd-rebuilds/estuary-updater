FROM fedora:30
LABEL maintainer="Factory 2.0"

ENV KRB5_CLIENT_KTNAME /etc/estuary-updater/estuary-updater.keytab
WORKDIR /src
RUN dnf -y install \
  --setopt=deltarpm=0 \
  --setopt=install_weak_deps=false \
  --setopt=tsflags=nodocs \
  bash \
  krb5-workstation \
  python3-devel \
  # Install the RPM dependencies for both estuary-api and estuary-updater
  python3-fedmsg \
  python3-flask \
  # python3-stomper requires this but doesn't install it for some reason
  python3-future \
  python3-koji \
  python3-neomodel \
  python3-pyOpenSSL \
  python3-requests \
  python3-requests-kerberos \
  python3-stomper \
  && dnf clean all
# Install estuary-api directly from GitHub since there aren't any releases yet
RUN pip3 install https://github.com/release-engineering/estuary-api/tarball/master#egg=estuary  --no-deps
# This will allow a non-root user to install a custom root CA at run-time
RUN chmod 777 /etc/pki/tls/certs/ca-bundle.crt
# This resolves the "Invalid UID in persistent keyring name while getting default ccache" error
RUN sed -i '/default_ccache_name = KEYRING:persistent:%{uid}/d' /etc/krb5.conf
COPY . .
# We install the python3-koji RPM but it doesn't register as installed according to setuptools.
# This hack keeps the application from raising a pkg_resources.DistributionNotFound exception.
RUN sed -i '/koji/d' requirements.txt
# Install the application itself
RUN pip3 install . --no-deps
# Remove the default fedmsg config files
RUN rm -f /etc/fedmsg.d/* && rm -rf ./fedmsg.d

# consumer.crt, consumer.key, and estuary-updater.keytab must be in this volume at runtime
VOLUME "/etc/estuary-updater"
# The fedmsg configuration files must be in this volume at runtime
VOLUME "/etc/fedmsg.d"
USER 1001
CMD ["bash", "/src/docker/run.sh"]
