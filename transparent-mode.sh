#!/usr/bin/env bash
#
# Achieves transparent mode for mitmproxy on Linux.
#
# by Paulo Feitosa <coding.paulo.feitosa@gmail.com>
# v1.0.0 2017-04-07
#

set -o errexit
set -o pipefail
set -o nounset
#set -o xtrace

usage() {
    printf "%s\n" "Usage: $0 [options]" >&2
    printf "%s\n\n" "Options:" >&2
    printf "%s\t%s\n" "-h" "Show this message and exit." >&2
    printf "%s\t%s\n" "-p" "Proxy service port." >&2
}

main() {
  if [ "${EUID}" -ne 0 ]; then
    printf "%s\n" "Run as root" >&2
    exit 1
  fi

  local port="8080"

  while getopts "h?p:" opt; do
    case "${opt}" in
      h|\?)
        usage
        exit 0
        ;;
      p)
        port="${optarg}"
        ;;
    esac
  done

  local iptables="/usr/bin/iptables"
  local mitmproxy="/usr/bin/mitmproxy"
  local sysctl="/usr/bin/sysctl"

  "${sysctl}" -w net.ipv4.ip_forward=1
  echo 0 | tee /proc/sys/net/ipv4/conf/*/send_redirects
  "${iptables}" -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port "${port}"
  "${iptables}" -t nat -A PREROUTING -p tcp --dport 443 -j REDIRECT --to-port "${port}"
}

main "$@"
exit
