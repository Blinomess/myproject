ymaps.ready(init);
function init(){     
    var myMap = new ymaps.Map ('mymap', {
        center: [55.669957, 37.480224], 
        zoom: 15
    });

    var currentPlacemark = null;

    myMap.events.add('click', function (e) {
      var coords = e.get('coords');

      if (currentPlacemark) {
        myMap.geoObjects.remove(currentPlacemark);
      }

      currentPlacemark = new ymaps.Placemark(coords, {
        balloonContent: 'Ваша метка'
      });

      myMap.geoObjects.add(currentPlacemark);

      document.getElementById('id_latitude').value = coords[0];
      document.getElementById('id_longitude').value = coords[1];
    });
}

function checkThemeSelection() {
  var selectElement = document.getElementById('id_title');
  var submitButton = document.getElementById('submitButton');
  var messageElement = document.getElementById('message');

  if (selectElement.value === 'Choose theme') {
      submitButton.disabled = true;
      messageElement.style.display = 'block';
  } else {
      submitButton.disabled = false;
      messageElement.style.display = 'none';
  }
}