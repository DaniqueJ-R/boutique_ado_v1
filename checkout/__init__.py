default_app_config = 'checkout.app.CheckoutConfig'

class CheckoutConfig(AppConfig):
    name  = 'checkout'
    
    def ready(self):
        import checkoout.signals
