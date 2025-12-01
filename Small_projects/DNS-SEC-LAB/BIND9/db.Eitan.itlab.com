
$TTL    3600                       ; Default Time-To-Live for records
@       IN      SOA     ns1.Eitan.itlab.com. admin.Eitan.itlab.com. (
                        2025011401 ; Serial (YYYYMMDD##)
                        3600       ; Refresh (1 hour)
                        1800       ; Retry (30 minutes)
                        604800     ; Expire (1 week)
                        86400 )    ; Minimum TTL (1 day)

        IN      NS      ns1.Eitan.itlab.com.  ; Authoritative name server
ns1     IN      A       192.168.255.56        ; DNS server (Ubuntu)
R1      IN      A       192.168.255.190       ; Router
Sw      IN      A       192.168.255.57        ; Switch
Ubuntu  IN      A       192.168.255.56        ; Ubuntu server (also DNS server)
dns     IN      CNAME   Ubuntu                ; DNS alias pointing to Ubuntu


$INCLUDE Keitan.itlab.com.+008+17665.key
$INCLUDE Keitan.itlab.com.+008+42696.key
