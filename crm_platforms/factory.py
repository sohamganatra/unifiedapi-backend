from crm_platforms.pipedrive import Pipedrive
from crm_platforms.hubspot import Hubspot

def create_platform(platform_type, auth):
    if platform_type == "pipedrive":
        return Pipedrive("pipedrive",auth)
    elif platform_type == "hubspot":
        return Hubspot("hubspot",auth)
    else:
        return None