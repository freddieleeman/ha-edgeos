"""
Support for Shinobi Video.
For more details about this platform, please refer to the documentation at
https://home-assistant.io/components/switch.shinobi/
"""
from datetime import datetime, timedelta

from homeassistant.components.sensor import SensorStateClass
from homeassistant.const import ATTR_NAME, ATTR_UNIT_OF_MEASUREMENT

from ...core.helpers.const import *

ENTRY_PRIMARY_KEY = CONF_NAME

SCAN_INTERVAL_WS_TIMEOUT = timedelta(seconds=60)

DEFAULT_ICON = "mdi:alarm-light"
ATTR_FRIENDLY_NAME = "friendly_name"

SCAN_INTERVAL = timedelta(seconds=60)
HEARTBEAT_INTERVAL_SECONDS = timedelta(seconds=25)
TRIGGER_INTERVAL = timedelta(seconds=1)

MAX_MSG_SIZE = 0
DISCONNECT_INTERVAL = 5
RECONNECT_INTERVAL = 30

STORAGE_DATA_MONITORED_INTERFACES = "monitored-interfaces"
STORAGE_DATA_MONITORED_DEVICES = "monitored-devices"
STORAGE_DATA_UNIT = "unit"
STORAGE_DATA_LOG_INCOMING_MESSAGES = "log-incoming-messages"
STORAGE_DATA_STORE_DEBUG_DATA = "store-debug-data"
DATA_LAST_UPDATE = "lastUpdate"

API_DATA_PRODUCT = "product"
API_DATA_SYSTEM = "system"
API_DATA_INTERFACES = "interfaces"
API_DATA_GENERAL_DATA = "general-data"
API_DATA_SESSION_ID = "session-id"
API_DATA_COOKIES = "cookies"

API_URL_DATA_TEMPLATE = "{}?data={}"
API_URL_HEARTBEAT_TEMPLATE = "{}?_={}"

EDGE_OS_VERSION_INCOMPATIBLE = "v1"
EDGE_OS_VERSION_UNKNOWN = "N/A"
EDGE_OS_API_URL = "{}/api/edge/{}.json"
EDGE_OS_API_GET = "get"
EDGE_OS_API_DATA = "data"
EDGE_OS_API_HEARTBREAT = "heartbeat"

TRUE_STR = "true"
FALSE_STR = "false"

LINK_ENABLED = "up"
LINK_CONNECTED = "l1up"

INTERFACES_STATS = "stats"

BYTE = 1
KILO_BYTE = BYTE * 1024
MEGA_BYTE = KILO_BYTE * 1024

INTERFACES_KEY = "interfaces"
SYSTEM_STATS_KEY = "system-stats"
EXPORT_KEY = "export"
STATIC_DEVICES_KEY = "static-devices"
DHCP_STATS_KEY = "dhcp_stats"
SYS_INFO_KEY = "sys_info"
DISCOVER_KEY = "discover"
UNKNOWN_DEVICES_KEY = "unknown-devices"

DHCP_LEASES_KEY = "dhcp-leases"
DHCP_SERVER_LEASES = "dhcp-server-leases"
DHCP_SERVER_STATS = "dhcp-server-stats"
LEASED = "leased"
DHCP_SERVER_LEASES_CLIENT_HOSTNAME = "client-hostname"
ROUTES_KEY = "routes"
NUM_ROUTES_KEY = "num-routes"
USERS_KEY = "users"

UPTIME = "uptime"
IS_ALIVE = "is_alive"

UPDATE_DATE_ENDPOINTS = [
    SYS_INFO_KEY,
    DHCP_STATS_KEY,
    DHCP_LEASES_KEY,
    ROUTES_KEY
]

DISCOVER_DATA_FW_VERSION = "fwversion"
DISCOVER_DATA_PRODUCT = "product"

SYSTEM_STATS_DATA_UPTIME = "uptime"
SYSTEM_STATS_DATA_CPU = "cpu"
SYSTEM_STATS_DATA_MEM = "mem"

DISCOVER_DEVICE_ITEMS = ["hostname", "product", "uptime", "fwversion", "system_status"]


ATTR_KILO = "KBytes"
ATTR_MEGA = "MBytes"
ATTR_BYTE = "Bytes"
ATTR_WEB_SOCKET_LAST_UPDATE = "WS Last Update"
ATTR_WEB_SOCKET_MESSAGES_RECEIVED = "Messages Received"
ATTR_WEB_SOCKET_MESSAGES_IGNORED = "Messages Ignored"
ATTR_WEB_SOCKET_MESSAGES_HANDLED_PERCENTAGE = "Messages Handled"
ATTR_API_LAST_UPDATE = "API Last Update"
ATTR_UNKNOWN_DEVICES = "Unknown Devices"
ATTR_SYSTEM_STATUS = "System Status"
ATTR_ENABLED = "enabled"
ATTR_FIRMWARE_UPDATE_URL = "url"
ATTR_FIRMWARE_UPDATE_VERSION = "version"

ALLOWED_UNITS = {ATTR_BYTE: BYTE, ATTR_KILO: KILO_BYTE, ATTR_MEGA: MEGA_BYTE}
ALLOWED_UNITS_LIST = [ATTR_BYTE, ATTR_KILO, ATTR_MEGA]

DEVICE_LIST = "devices"
ADDRESS_LIST = "addresses"
FW_LATEST = "addresses"
ADDRESS_IPV4 = "ipv4"
ADDRESS_HWADDR = "hwaddr"

INTERFACES = "interfaces"
SYSTEM = "system"
SERVICE = "service"
DHCP_SERVER = "dhcp-server"
SHARED_NETWORK_NAME = "shared-network-name"
SUBNET = "subnet"
DOMAIN_NAME = "domain-name"
STATIC_MAPPING = "static-mapping"
IP_ADDRESS = "ip-address"
MAC_ADDRESS = "mac-address"
IP = "ip"
MAC = "mac"
CONNECTED = "Connected"
LAST_ACTIVITY = "Last Activity"

RESPONSE_SUCCESS_KEY = "success"
RESPONSE_ERROR_KEY = "error"
RESPONSE_OUTPUT = "output"
RESPONSE_FAILURE_CODE = "0"

HEARTBEAT_MAX_AGE = 15

WS_TOPIC_NAME = "name"
WS_TOPIC_UNSUBSCRIBE = "UNSUBSCRIBE"
WS_TOPIC_SUBSCRIBE = "SUBSCRIBE"
WS_SESSION_ID = "SESSION_ID"
WS_MESSAGE_COMPRESSION = 15

UNIT_ERRORS = "Errors"
UNIT_PACKETS = "Packets"
UNIT_TRAFFIC = "Traffic"
UNIT_RATE = "Rate"
UNIT_BPS = "bps"
UNIT_BYTES = "bytes"
UNIT_DROPPED_PACKETS = "Dropped"
UNIT_DEVICES = "Devices"

DEFAULT_DATE_FORMAT = "%x %X"

DOMAIN_LOGGER = "logger"
SERVICE_SET_LEVEL = "set_level"

INTERFACES_MAIN_MAP = {
    LINK_CONNECTED: {ATTR_NAME: "Connected", ATTR_UNIT_OF_MEASUREMENT: "Connectivity"},
    LINK_ENABLED: {ATTR_NAME: "Enabled"},
    "speed": {ATTR_NAME: "Link Speed (Mbps)"},
    "duplex": {ATTR_NAME: "Duplex"},
    "mac": {ATTR_NAME: "MAC"},
}

DEVICES_MAIN_MAP = {
    LINK_CONNECTED: {ATTR_NAME: "Connected", ATTR_UNIT_OF_MEASUREMENT: "Connectivity"},
    "ip": {ATTR_NAME: "Address"},
    "mac": {ATTR_NAME: "MAC"},
}

STATS_DIRECTION = {
    "rx": "Received",
    "tx": "Sent"
}

INTERFACES_STATS_MAP = {
    "rx_packets": SensorStateClass.TOTAL_INCREASING,
    "tx_packets": SensorStateClass.TOTAL_INCREASING,
    "rx_bytes": SensorStateClass.TOTAL_INCREASING,
    "tx_bytes": SensorStateClass.TOTAL_INCREASING,
    "rx_errors": SensorStateClass.TOTAL_INCREASING,
    "tx_errors": SensorStateClass.TOTAL_INCREASING,
    "rx_dropped": SensorStateClass.TOTAL_INCREASING,
    "tx_dropped": SensorStateClass.TOTAL_INCREASING,
    "rx_bps": SensorStateClass.MEASUREMENT,
    "tx_bps": SensorStateClass.MEASUREMENT,
    "multicast": SensorStateClass.TOTAL_INCREASING,
}

DEVICE_SERVICES_STATS_MAP = {
    "rx_bytes": SensorStateClass.TOTAL_INCREASING,
    "tx_bytes": SensorStateClass.TOTAL_INCREASING,
    "rx_rate": SensorStateClass.MEASUREMENT,
    "tx_rate": SensorStateClass.MEASUREMENT
}

STATS_MAPS = {
    INTERFACES_KEY: INTERFACES_STATS_MAP,
    STATIC_DEVICES_KEY: DEVICE_SERVICES_STATS_MAP
}

EMPTY_LAST_VALID = datetime.fromtimestamp(100000)

MAX_PENDING_PAYLOADS = 3

EMPTY_STRING = ""
NEW_LINE = "\n"
BEGINS_WITH_SIX_DIGITS = "^([0-9]{1,6})"

SENSOR_TYPE_INTERFACE = "Interface"
SENSOR_TYPE_DEVICE = "Device"
SENSOR_TYPES = {
    INTERFACES_KEY: SENSOR_TYPE_INTERFACE,
    STATIC_DEVICES_KEY: SENSOR_TYPE_DEVICE
}

STRING_DASH = "-"
STRING_UNDERSCORE = "_"
STRING_COMMA = ","
STRING_COLON = ":"

ERROR_SHUTDOWN = "Connector is closed."

SYSTEM_DATA_HOSTNAME = "host-name"
SYSTEM_DATA_DOMAIN_NAME = "domain-name"
SYSTEM_DATA_NTP = "ntp"
SYSTEM_DATA_NTP_SERVER = "server"
SYSTEM_DATA_OFFLOAD = "offload"
SYSTEM_DATA_OFFLOAD_HW_NAT = "hwnat"
SYSTEM_DATA_OFFLOAD_IPSEC = "ipsec"
SYSTEM_DATA_TRAFFIC_ANALYSIS = "traffic-analysis"
SYSTEM_DATA_TRAFFIC_ANALYSIS_DPI = "dpi"
SYSTEM_DATA_TRAFFIC_ANALYSIS_EXPORT = "export"
SYSTEM_DATA_TIME_ZONE = "time-zone"

SYSTEM_INFO_DATA_FW_LATEST = "fw-latest"
SYSTEM_INFO_DATA_FW_LATEST_STATE = "state"
SYSTEM_INFO_DATA_FW_LATEST_VERSION = "version"
SYSTEM_INFO_DATA_FW_LATEST_URL = "url"

FW_LATEST_STATE_CAN_UPGRADE = "can-upgrade"

SYSTEM_INFO_DATA_SW_VER = "sw_ver"

SYSTEM_DATA_ENABLED = "enable"
SYSTEM_DATA_DISABLED = "disabled"

INTERFACE_DATA_NAME = "name"
INTERFACE_DATA_DESCRIPTION = "description"
INTERFACE_DATA_INTERFACE_TYPE = "type"
INTERFACE_DATA_DUPLEX = "duplex"
INTERFACE_DATA_SPEED = "speed"
INTERFACE_DATA_BRIDGE_GROUP = "bridge-group"
INTERFACE_DATA_ADDRESS = "address"
INTERFACE_DATA_AGING = "aging"
INTERFACE_DATA_BRIDGED_CONNTRACK = "bridged-conntrack"
INTERFACE_DATA_HELLO_TIME = "hello-time"
INTERFACE_DATA_MAX_AGE = "max-age"
INTERFACE_DATA_PRIORITY = "priority"
INTERFACE_DATA_PROMISCUOUS = "promiscuous"
INTERFACE_DATA_STP = "stp"
INTERFACE_DATA_RECEIVED = "received"
INTERFACE_DATA_SENT = "sent"
INTERFACE_DATA_MULTICAST = "multicast"
INTERFACE_DATA_STATS = "stats"
INTERFACE_DATA_UP = "up"
INTERFACE_DATA_L1UP = "l1up"
INTERFACE_DATA_MAC = "mac"

DEVICE_DATA_NAME = "hostname"
DEVICE_DATA_DOMAIN = "domain"
DEVICE_DATA_IP = "ip"
DEVICE_DATA_MAC = "mac"
DEVICE_DATA_RECEIVED = "received"
DEVICE_DATA_SENT = "sent"

TRAFFIC_DATA_DIRECTION = "direction"
TRAFFIC_DATA_RATE = "rate"
TRAFFIC_DATA_TOTAL = "total"
TRAFFIC_DATA_ERRORS = "errors"
TRAFFIC_DATA_PACKETS = "packets"
TRAFFIC_DATA_DROPPED = "dropped"
TRAFFIC_DATA_LAST_ACTIVITY = "last_activity"
TRAFFIC_DATA_LAST_ACTIVITY_IN_SECONDS = "last_activity_in_seconds"

TRAFFIC_DATA_DIRECTION_SENT = "tx"
TRAFFIC_DATA_DIRECTION_RECEIVED = "rx"

TRAFFIC_DATA_DIRECTIONS = [
    TRAFFIC_DATA_DIRECTION_SENT,
    TRAFFIC_DATA_DIRECTION_RECEIVED
]

TRAFFIC_STATS_BPS_KEY = "bps"
TRAFFIC_STATS_BYTES = "bytes"

TRAFFIC_DATA_INTERFACE_ITEMS = {
    TRAFFIC_STATS_BPS_KEY: TRAFFIC_DATA_RATE,
    TRAFFIC_STATS_BYTES: TRAFFIC_DATA_TOTAL,
    TRAFFIC_DATA_ERRORS: TRAFFIC_DATA_ERRORS,
    TRAFFIC_DATA_PACKETS: TRAFFIC_DATA_PACKETS,
    TRAFFIC_DATA_DROPPED: TRAFFIC_DATA_DROPPED
}

TRAFFIC_DATA_DEVICE_ITEMS = {
    TRAFFIC_DATA_RATE: TRAFFIC_DATA_RATE,
    TRAFFIC_STATS_BYTES: TRAFFIC_DATA_TOTAL
}

INTERFACE_TYPE_BRIDGE = "bridge"
INTERFACE_TYPE_ETHERNET = "ethernet"

MONITORED_INTERFACE_TYPES = [
    INTERFACE_TYPE_BRIDGE,
    INTERFACE_TYPE_ETHERNET
]
