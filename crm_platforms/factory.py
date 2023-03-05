from crm_platforms.pipedrive import Pipedrive

def create_platform(platform_type, auth):
    if platform_type == "pipedrive":
        return Pipedrive("pipedrive",auth)
    else:
        return None