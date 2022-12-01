from Classes.InheritClasses import *
from Classes.WebPush import WebPush

# Create objects from all classes
webPush = WebPush(platform="Test platform", optin=True, global_frequency_capping=20, start_date="30-11-2022",
                  end_date="01-12-2022", language="Python", push_type=2)

bulkPush = BulkPush(platform="Test platform", optin=True, global_frequency_capping=20, start_date="30-11-2022",
                    end_date="01-12-2022", language="Python", push_type=2, send_date=30112022)

instockPush = InstockPush(platform="Test platform", optin=True, global_frequency_capping=20, start_date="30-11-2022",
                          end_date="01-12-2022", language="Python", push_type=2, stock_info=True)

priceAlertPush = PriceAlertPush(platform="Test platform", optin=True, global_frequency_capping=20,
                                start_date="30-11-2022",
                                end_date="01-12-2022", language="Python", push_type=2, price_info=20, discount_rate=0.3)

segmentPush = SegmentPush(platform="Test platform", optin=True, global_frequency_capping=20, start_date="30-11-2022",
                          end_date="01-12-2022", language="Python", push_type=2, segment_name="Test Segment name")

triggerPush = TriggerPush(platform="Test platform", optin=True, global_frequency_capping=20, start_date="30-11-2022",
                          end_date="01-12-2022", language="Python", push_type=2, trigger_page="Test page")

# Call methods of the classes (if they have any)
discountPrice = priceAlertPush.discount_price()
stockUpdate = instockPush.stockUpdate()

print(f"Discount Price: {discountPrice} \nStock Update: {stockUpdate}")

# call send_push
webPush.send_push()

