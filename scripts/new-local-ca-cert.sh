#!/usr/bin/env sh
set -eu

SITE_IP="${SITE_IP:-192.168.50.206}"
SITE_DNS="${SITE_DNS:-ccna.local}"
OUTPUT_DIR="${OUTPUT_DIR:-certs}"

mkdir -p "$OUTPUT_DIR"

CA_KEY="$OUTPUT_DIR/ccna-local-ca.key"
CA_CERT="$OUTPUT_DIR/ccna-local-ca.crt"
SITE_KEY="$OUTPUT_DIR/ccna-site.key"
SITE_CSR="$OUTPUT_DIR/ccna-site.csr"
SITE_CERT="$OUTPUT_DIR/ccna-site.crt"
EXT_FILE="$OUTPUT_DIR/ccna-site.ext"

openssl genrsa -out "$CA_KEY" 4096
openssl req -x509 -new -nodes -key "$CA_KEY" -sha256 -days 3650 \
  -out "$CA_CERT" \
  -subj "/CN=CCNA Study Local CA"

openssl genrsa -out "$SITE_KEY" 2048
openssl req -new -key "$SITE_KEY" -out "$SITE_CSR" \
  -subj "/CN=$SITE_IP"

cat > "$EXT_FILE" <<EOF
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
extendedKeyUsage = serverAuth
subjectAltName = @alt_names

[alt_names]
IP.1 = $SITE_IP
DNS.1 = $SITE_DNS
EOF

openssl x509 -req -in "$SITE_CSR" -CA "$CA_CERT" -CAkey "$CA_KEY" -CAcreateserial \
  -out "$SITE_CERT" -days 825 -sha256 -extfile "$EXT_FILE"

printf '%s\n' "Generated:"
printf '  CA certificate:   %s\n' "$CA_CERT"
printf '  Site certificate: %s\n' "$SITE_CERT"
printf '  Site private key: %s\n' "$SITE_KEY"
printf '\nTrust %s on your devices to avoid browser warnings.\n' "$CA_CERT"
