from Classes.WebPush import WebPush


class BulkPush(WebPush):

    def __init__(self, platform, optin: bool, global_frequency_capping, start_date, end_date, language, push_type,
                 send_date: int):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.send_date = send_date


class InstockPush(WebPush):

    def __init__(self, platform, optin: bool, global_frequency_capping, start_date, end_date, language, push_type,
                 stock_info: bool):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.stock_info = stock_info

    def stockUpdate(self):
        return not self.stock_info


class PriceAlertPush(WebPush):

    def __init__(self, platform, optin: bool, global_frequency_capping, start_date, end_date, language, push_type,
                 price_info: int, discount_rate: float):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.price_info = price_info
        self.discount_rate = discount_rate

    def discount_price(self):
        return self.price_info - (self.price_info * self.discount_rate)


class SegmentPush(WebPush):

    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 segment_name: str):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.segment_name = segment_name


class TriggerPush(WebPush):

    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 trigger_page: str):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.trigger_page = trigger_page
