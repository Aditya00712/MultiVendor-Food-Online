def registerVendor(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in!")
        return redirect("myAccount")

    elif request.method == "POST":
        form = UserForm(request.POST)
        vendorForm = VendorForm(request.POST, request.FILES)
        if form.is_valid() and vendorForm.is_valid():
            # user = form.save(commit=False)
            # user.set_password(form.cleaned_data['password'])

            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"].lower()
            password = form.cleaned_data["password"]
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
            )

            user.role = User.VENDOR
            user.save()

            # send verification email
            mail_subject = "Activate your account"
            mail_template = "accounts/emails/account_verification_email.html"
            send_verification_email(request, user, mail_subject, mail_template)

            vendor = vendorForm.save(commit=False)
            vendor.user = user
            vendor.vendor_slug = slugify(vendorForm.cleaned_data["vendor_name"]) + str(user.id)
            user_profile = UserProfile.objects.get(user=user)
            vendor.user_profile = user_profile
            vendor.save()

            messages.success(
                request, f"Signup successful for {username}! Stand by for approval."
            )
            return redirect("registerVendor")
        else:
            print(form.errors)

    else:
        form = UserForm()
        vendorForm = VendorForm()
    context = {"form": form, "vendorForm": vendorForm}
    return render(request, "accounts/registerVendor.html", context)