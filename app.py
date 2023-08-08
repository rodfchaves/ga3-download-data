from system import main as system_main
from trafficsource import main as traffic_source_main
from device import main as device_main
from eventtracking import main as event_tracking_main
from pagetracking import main as page_tracking_main
from audience import main as audience_main
from ecommerce import main as ecommerce_main
from geo import main as geo_main
import time
import sys

sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding="utf-8")


if __name__ == '__main__':
    page_tracking_main()
    time.sleep(5)

    system_main()
    time.sleep(5)

    traffic_source_main()
    time.sleep(5)
    
    device_main()
    time.sleep(5)

    event_tracking_main()
    time.sleep(5)

    ecommerce_main()
    time.sleep(5)

    geo_main()
    time.sleep(5)

