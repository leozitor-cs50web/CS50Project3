/////////////////////// ready
$(document).ready(function () {
    /*----------------------------------------------------*/
    // Superfish menu.
    /*----------------------------------------------------*/
    $('.sf-menu').superfish();


    var s = $('.sliderr');
    if (s.length) {
        s.responsiveSlides({
            pager: true
        });
        $('.rslides_tabs').find('a').each(function () {
            if (parseInt($(this).html()) < 10) {
                $(this).html('0' + $(this).html());
            }
        });
    }

    /*----------------------------------------------------*/
    // Scroll
    /*----------------------------------------------------*/
    $(".scroll-to").bind('click', function (event) {

        $("html, body").animate({
            scrollTop: $($(this).attr("href")).offset().top - 50
        }, 1000);

        event.preventDefault();
    });

    /*----------------------------------------------------*/
    // Audio
    /*----------------------------------------------------*/
    var o = $('.audio1 audio');
    if (o.length > 0) {
        o.mediaelementplayer({
            features: ['prevtrack', 'playpause', 'nexttrack', 'progress', 'current', 'volume', 'playlistfeature']
        });
        $('.audio1 .mejs-prevtrack-button').addClass('mejs-cust1-button');
        $('.audio1 .mejs-nexttrack-button').addClass('mejs-cust2-button');
    }
    ;

    var o = $('.audio2 audio');
    if (o.length > 0) {
        o.mediaelementplayer({
            features: ['playpause', 'progress']
        });
    }
    ;

    var o = $('.audio3 audio');
    if (o.length > 0) {
        o.mediaelementplayer({
            features: ['playpause']
        });
    }
    ;

    var o = $('.audio4 audio');
    if (o.length > 0) {
        o.mediaelementplayer({
            features: ['playpause', 'progress']
        });
    }
    ;

    // Accordion.
    var o = $(".accordion");
    if (o.length > 0) {
        o.accordion({
            active: 0,
            heightStyle: "content"
        });
    }
    ;

    // Animate number.
    var o = $('.animated-number');
    if (o.length > 0) {
        o.appear(function () {
            var elem = $(this);
            var b = elem.text();
            var d = elem.data('duration');
            var animationDelay = elem.data('animation-delay');
            if (!animationDelay) {
                animationDelay = 0;
            }
            elem.text("0");

            setTimeout(function () {
                elem.animate({num: b}, {
                    duration: d,
                    step: function (num) {
                        this.innerHTML = (num).toFixed(0)
                    }
                });
            }, animationDelay);
        });
    }
    ;

    /*----------------------------------------------------*/
    // owlCarousel
    /*----------------------------------------------------*/

    var o = $('.owl-carousel-testimonials');
    if (o.length > 0) {
        o.owlCarousel({
            responsive: {
                0: {
                    items: 1,
                    nav: true
                },
                600: {
                    items: 2,
                    nav: false
                },
                1000: {
                    items: 2,
                    nav: true,
                    loop: false
                }
            },
            loop: true,
            navText: ['', ''],
            //margin: 30
        });
    }
    ;


    $(document).ready(function () {
        $(".owl-carousel").owlCarousel();
    });


});

/////////////////////// load
$(window).on('load', function () {


});

/*----------------------------------------------------*/
// Tabs.
/*----------------------------------------------------*/
$('.tabs a').click(function (e) {
    e.preventDefault();
    var $this = $(this),
        tabgroup = '#' + $this.parents('.tabs').data('tabgroup'),
        others = $this.closest('li').siblings(),
        target = $this.attr('href');

    others.removeClass('active');
    $this.closest('li').addClass('active');
    $(tabgroup).children('div').hide();
    $(target).show();
});
$('.tabs .active a').click();


/*----------------------------------------------------*/
// Checkboxes.
/*----------------------------------------------------*/

$('input.form-check-input').on('change', function () {
    $('input.form-check-input').not(this).prop('checked', false);
});

$('input.form-check-input-sizes').on('change', function () {
    $('input.form-check-input-sizes').not(this).prop('checked', false);
});


/*----------------------------------------------------*/
// Touchspin.
/*----------------------------------------------------*/
// End Touchspin.
/*----------------------------------------------------*/
/*

$('.custom-control-input').on('change', function(){
    if($(this).prop('checked')){
        $('.different_shipping').css('visibility', 'visible');
    }
    else{
        $('.different_shipping').css('visibility','hidden');
    }
});
*/
$('#customCheck1').on('change', function () {
    if ($(this).prop('checked')) {
        $('.different_shipping').css('display', 'block');
    } else {
        $('.different_shipping').css('display', 'none');
    }
});

/* -----------------------  index behavior   ---------------------- */

document.addEventListener('DOMContentLoaded', () => {
    //setting button of each item to control the modal, send info and about select
    document.querySelectorAll('#toppingButton').forEach(function (button) {
        button.onclick = function () {
            let modal = document.getElementById('itemId')
            let toppingAllowance = Number(button.value)
            document.getElementById('topping2').style.display = "block"
            document.getElementById('topping3').style.display = "block"
            modal.value = button.name
            if (toppingAllowance === 1) {
                document.getElementById('topping2').style.display = "none"
                document.getElementById('topping3').style.display = "none"
            } else if (toppingAllowance === 2) {
                document.getElementById('topping3').style.display = "none"
            }
        };
    });
    // buttons plus and minus of shopping cart
    document.querySelectorAll('.plusButton').forEach(function (el) {
        let counter = el.querySelector('.counter')
        el.querySelector('.countPlus').onclick = () => {
            let increment = parseInt(counter.innerHTML) + 1
            counter.innerHTML = `${increment}`
        }
        el.querySelector('.countMinus').onclick = () => {
            let decrement = parseInt(counter.innerHTML) - 1
            counter.innerHTML = `${decrement}`
        }
    })
    // control the of badge about status
    document.querySelectorAll('.status_td').forEach(function (el) {
        let badge = el.querySelector('.badge')
        let badgeType = badge.innerHTML
        if (badgeType === 'initiated')
            badge.className = "badge badge-primary"
        else if (badgeType === 'pending')
            badge.className = "badge badge-warning"
        else if (badgeType === 'completed')
            badge.className = "badge badge-success"
    })
    document.querySelector('#selectRegPizza').onclick = () => {
        let state = document.getElementById("regPizza").style.display
        if (state === "block") {
            document.getElementById("regPizza").style.display = "none"
        } else {
            document.getElementById("regPizza").style.display = "block"
        }
    }
    document.querySelector('#selectSiciPizza').onclick = () => {
        let state = document.getElementById("siciPizza").style.display
        if (state === "block") {
            document.getElementById("siciPizza").style.display = "none"
        } else {
            document.getElementById("siciPizza").style.display = "block"
        }
    }
    document.querySelector('#selectSub').onclick = () => {
        let state = document.getElementById("sub").style.display
        if (state === "block") {
            document.getElementById("sub").style.display = "none"
        } else {
            document.getElementById("sub").style.display = "block"
        }
    }
    document.querySelector('#selectPasta').onclick = () => {
        let state = document.getElementById("pasta").style.display
        if (state === "block") {
            document.getElementById("pasta").style.display = "none"
        } else {
            document.getElementById("pasta").style.display = "block"
        }
    }
    document.querySelector('#selectSalad').onclick = () => {
        let state = document.getElementById("salad").style.display
        if (state === "block") {
            document.getElementById("salad").style.display = "none"
        } else {
            document.getElementById("salad").style.display = "block"
        }
    }
    document.querySelector('#selectDinnerPlatter').onclick = () => {
        let state = document.getElementById("dinnerPlatter").style.display
        if (state === "block") {
            document.getElementById("dinnerPlatter").style.display = "none"
        } else {
            document.getElementById("dinnerPlatter").style.display = "block"
        }
    }
});

/* -----------------------  Google Map   ----------------------*/


// // When the window has finished loading create our google map below
// google.maps.event.addDomListener(window, 'load', init);
//
// function init() {
//     // Basic options for a simple Google Map
//     // For more options see: https://developers.google.com/maps/documentation/javascript/reference#MapOptions
//     var mapOptions = {
//         // How zoomed in you want the map to start at (always required)
//         zoom: 11,
//
//         // The latitude and longitude to center the map (always required)
//         center: new google.maps.LatLng(40.6700, -73.9400), // New York
//
//         // How you would like to style the map.
//         // This is where you would paste any style found on Snazzy Maps.
//         styles:[
//             {
//                 "featureType": "water",
//                 "elementType": "geometry",
//                 "stylers": [
//                     {
//                         "color": "#e9e9e9"
//                     },
//                     {
//                         "lightness": 17
//                     }
//                 ]
//             },
//             {
//                 "featureType": "landscape",
//                 "elementType": "geometry",
//                 "stylers": [
//                     {
//                         "color": "#f5f5f5"
//                     },
//                     {
//                         "lightness": 20
//                     }
//                 ]
//             },
//             {
//                 "featureType": "road.highway",
//                 "elementType": "geometry.fill",
//                 "stylers": [
//                     {
//                         "color": "#ffffff"
//                     },
//                     {
//                         "lightness": 17
//                     }
//                 ]
//             },
//             {
//                 "featureType": "road.highway",
//                 "elementType": "geometry.stroke",
//                 "stylers": [
//                     {
//                         "color": "#ffffff"
//                     },
//                     {
//                         "lightness": 29
//                     },
//                     {
//                         "weight": 0.2
//                     }
//                 ]
//             },
//             {
//                 "featureType": "road.arterial",
//                 "elementType": "geometry",
//                 "stylers": [
//                     {
//                         "color": "#ffffff"
//                     },
//                     {
//                         "lightness": 18
//                     }
//                 ]
//             },
//             {
//                 "featureType": "road.local",
//                 "elementType": "geometry",
//                 "stylers": [
//                     {
//                         "color": "#ffffff"
//                     },
//                     {
//                         "lightness": 16
//                     }
//                 ]
//             },
//             {
//                 "featureType": "poi",
//                 "elementType": "geometry",
//                 "stylers": [
//                     {
//                         "color": "#f5f5f5"
//                     },
//                     {
//                         "lightness": 21
//                     }
//                 ]
//             },
//             {
//                 "featureType": "poi.park",
//                 "elementType": "geometry",
//                 "stylers": [
//                     {
//                         "color": "#dedede"
//                     },
//                     {
//                         "lightness": 21
//                     }
//                 ]
//             },
//             {
//                 "elementType": "labels.text.stroke",
//                 "stylers": [
//                     {
//                         "visibility": "on"
//                     },
//                     {
//                         "color": "#ffffff"
//                     },
//                     {
//                         "lightness": 16
//                     }
//                 ]
//             },
//             {
//                 "elementType": "labels.text.fill",
//                 "stylers": [
//                     {
//                         "saturation": 36
//                     },
//                     {
//                         "color": "#333333"
//                     },
//                     {
//                         "lightness": 40
//                     }
//                 ]
//             },
//             {
//                 "elementType": "labels.icon",
//                 "stylers": [
//                     {
//                         "visibility": "off"
//                     }
//                 ]
//             },
//             {
//                 "featureType": "transit",
//                 "elementType": "geometry",
//                 "stylers": [
//                     {
//                         "color": "#f2f2f2"
//                     },
//                     {
//                         "lightness": 19
//                     }
//                 ]
//             },
//             {
//                 "featureType": "administrative",
//                 "elementType": "geometry.fill",
//                 "stylers": [
//                     {
//                         "color": "#fefefe"
//                     },
//                     {
//                         "lightness": 20
//                     }
//                 ]
//             },
//             {
//                 "featureType": "administrative",
//                 "elementType": "geometry.stroke",
//                 "stylers": [
//                     {
//                         "color": "#fefefe"
//                     },
//                     {
//                         "lightness": 17
//                     },
//                     {
//                         "weight": 1.2
//                     }
//                 ]
//             }
//         ]
//     };
//
//     // Get the HTML DOM element that will contain your map
//     // We are using a div with id="map" seen below in the <body>
//     var mapElement = document.getElementById('map');
//
//     // Create the Google Map using our element and options defined above
//     var map = new google.maps.Map(mapElement, mapOptions);
//
//     // Let's also add a marker while we're at it
//     var customMarker = 'img/map-marker.png';
//     var marker = new google.maps.Marker({
//         position: new google.maps.LatLng(40.6700, -73.9400),
//         icon: customMarker,
//         map: map,
//         title: 'Snazzy!'
//     });
// }

