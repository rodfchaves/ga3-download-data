import sys
from reports.system import main as system_main
from reports.trafficsource import main as traffic_source_main
from reports.device import main as device_main
from reports.eventtracking import main as event_tracking_main
from reports.pagetracking import main as page_tracking_main
from reports.audience import main as audience_main
from reports.ecommerce import main as ecommerce_main
from reports.geo import main as geo_main
import time

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

    audience_main()
    time.sleep(5)

    print("Done")  

