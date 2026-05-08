param(
    [string]$SiteIp = "192.168.50.206",
    [string]$SiteDns = "ccna.local",
    [string]$OutputDir = "certs"
)

$ErrorActionPreference = "Stop"

New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null

$caKey = Join-Path $OutputDir "ccna-local-ca.key"
$caCert = Join-Path $OutputDir "ccna-local-ca.crt"
$siteKey = Join-Path $OutputDir "ccna-site.key"
$siteCsr = Join-Path $OutputDir "ccna-site.csr"
$siteCert = Join-Path $OutputDir "ccna-site.crt"
$extFile = Join-Path $OutputDir "ccna-site.ext"

openssl genrsa -out $caKey 4096
openssl req -x509 -new -nodes -key $caKey -sha256 -days 3650 `
    -out $caCert `
    -subj "/CN=CCNA Study Local CA"

openssl genrsa -out $siteKey 2048
openssl req -new -key $siteKey -out $siteCsr `
    -subj "/CN=$SiteIp"

@"
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
extendedKeyUsage = serverAuth
subjectAltName = @alt_names

[alt_names]
IP.1 = $SiteIp
DNS.1 = $SiteDns
"@ | Set-Content -Encoding ascii $extFile

openssl x509 -req -in $siteCsr -CA $caCert -CAkey $caKey -CAcreateserial `
    -out $siteCert -days 825 -sha256 -extfile $extFile

Write-Host "Generated:"
Write-Host "  CA certificate:   $caCert"
Write-Host "  Site certificate: $siteCert"
Write-Host "  Site private key: $siteKey"
Write-Host ""
Write-Host "Trust $caCert on your devices to avoid browser warnings."
