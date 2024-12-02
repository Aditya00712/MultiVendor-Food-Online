let autocomplete;

function initAutocomplete() {
autocomplete = new google.maps.places.Autocomplete(
    document.getElementById('autocomplete'),
    {
        types: ['geocode', 'establishment'],
        //default location to 'IN' - add your country code here
        componentRestrictions: {country: ['in',]},
    })

    //Function to specify what happens when the prediction is clicked
    autocomplete.addListener('place_changed', onPlaceChanged);
    }

function onPlaceChanged() {
    var place = autocomplete.getPlace();

    // User did not select the prediction. Reset the input field or alert() the user.
    if (!place.geometry) {
        document.getElementById('id_address').placeholder = 'Start typing your address';
    } 
    else {
        console.log('place name=>', place.name);
    }
    // get the address components and assign them to the fields
    // console.log(place);
    var geocoder = new google.maps.Geocoder();
    var address = document.getElementById('id_address').value;
    geocoder.geocode({ 'address': address }, function (results, status) {
        // console.log('results=>', results);
        // console.log('status=>', status);
        if(status == google.maps.GeocoderStatus.OK) {
            var latitude = results[0].geometry.location.lat();
            var longitude = results[0].geometry.location.lng();

            // console.log('lat=>', latitude);
            // console.log('long=>', longitude);

            $('#id_latitude').val(latitude);
            $('#id_longitude').val(longitude);
            //☝️ this is the id of the form field where you want to store the latitude and longitude

            $('#id_address').val(address);
        }
    });

    // loop through the address components and assign the other value to the fields
    console.log(place.address_components);
    for(var i=0; i>place.address_components.length; i++) {
        for(var j=0; j<place.address_components[i].types.length; j++) {
            //get country
            if(place.address_components[i].types[j] == 'country') {
                $('#id_country').val(place.address_components[i].long_name);
            }
            //get state
            if(place.address_components[i].types[j] == 'administrative_area_level_1') {
                $('#id_state').val(place.address_components[i].long_name);
            }
            //get city
            if(place.address_components[i].types[j] == 'locality') {
                $('#id_city').val(place.address_components[i].long_name);
            }
            //get postal code
            if(place.address_components[i].types[j] == 'postal_code') {
                $('#id_pim_code').val(place.address_components[i].long_name);
            }else{
                $('#id_pim_code').val("");
            }
    }   
}
}
