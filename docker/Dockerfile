FROM registry.access.redhat.com/ubi8/ubi-minimal
LABEL maintainer="Factory 2.0"

ENV KRB5_CLIENT_KTNAME /etc/estuary-updater/estuary-updater.keytab
ENV REQUESTS_CA_BUNDLE /etc/pki/tls/certs/ca-bundle.crt
WORKDIR /src
RUN microdnf -y install \
  bash \
  krb5-devel \
  gcc \
  openssl-devel \
  python3-devel \
  && microdnf clean all
# This will allow a non-root user to install a custom root CA at run-time
RUN chmod 777 /etc/pki/tls/certs/ca-bundle.crt
# This resolves the "Invalid UID in persistent keyring name while getting default ccache" error
RUN sed -i '/default_ccache_name = KEYRING:persistent:%{uid}/d' /etc/krb5.conf
# Set this variable to build cryptography package without Rust
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1
COPY . .
# Install dependencies and the application itself
RUN pip3 install setuptools==46.1.0 \
    && pip3 install -r build-requirements.txt --require-hashes --no-deps \
    && pip3 install -r requirements.txt --require-hashes --no-deps \
    && pip3 install . --no-deps
# Remove the default fedmsg config files
RUN rm -f /etc/fedmsg.d/* && rm -rf ./fedmsg.d

# consumer.crt, consumer.key, and estuary-updater.keytab must be in this volume at runtime
VOLUME "/etc/estuary-updater"
# The fedmsg configuration files must be in this volume at runtime
VOLUME "/etc/fedmsg.d"
USER 1001
CMD ["bash", "/src/docker/run.sh"]
