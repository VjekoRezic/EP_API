from django.contrib import admin
from .models import WorkOrder, WO_Category, WO_Status   # Import the model Workorder    

admin.site.register(WO_Category)   # Register the model WO_Category in the admin site
admin.site.register(WO_Status)   # Register the model WO_Status in the admin site
admin.site.register(WorkOrder)   # Register the model Workorder in the admin site   
