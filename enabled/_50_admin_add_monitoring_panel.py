# The name of the panel to be added to HORIZON_CONFIG. Required.
PANEL = 'monitoring'
# The name of the dashboard the PANEL associated with. Required.
PANEL_DASHBOARD = 'admin'
# The name of the panel group the PANEL is associated with.
PANEL_GROUP = 'admin'

# Python panel class of the PANEL to be added.
ADD_PANEL = \
    'monitoring.panel.Monitoring'

# A list of applications to be added to INSTALLED_APPS.
ADD_INSTALLED_APPS = ['monitoring']

