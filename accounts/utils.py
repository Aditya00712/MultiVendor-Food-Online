def detectUser(user):
    if user.role == 1:
        redirectUrl = 'VendorDashboard'
        return redirectUrl
    elif user.role == 2:
        redirectUrl = 'custDashboard'
        return redirectUrl
    elif user.role == None and user.is_superadmin:
        redirectUrl = 'adminDashboard'
        return redirectUrl