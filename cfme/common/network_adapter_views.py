from widgetastic.widget import View

class NetworkAdapterDetailsView():
    entities = View.nested(NetworkAdapterDetailsEntities)

    @property
    def is_displayed(self):
        return False

class NetworkAdapterDetailsEntities(View):
